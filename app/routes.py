from flask import render_template, request, Blueprint
from psycopg2.errors import InFailedSqlTransaction

from app.models import (
    update_plot,
    get_all_regions,
    get_all_preset_names,
    get_preset_settings,
    save_preset,
    delete_preset
)
from app import app
from app.utils.exceptions import NoDataException

Router = Blueprint('Router', __name__)

# Initialize states
class State:
    def __init__(self) -> None:
        self.subregions = {region: False for region in get_all_regions()}
        self.presets_names = get_all_preset_names()
        self.rural_urban = "Average"
        self.male_female = "Average"

    def update_settings(self, sub_regions: list[str], rural_urban: str, male_female: str) -> None:
            """Set and remember values subregion checkboxes, of rural/urban and of male/female views."""
            self.rural_urban = rural_urban
            self.male_female = male_female
            for sub in self.subregions.keys():
                self.subregions[sub] = sub in sub_regions

    def update_presets_names(self) -> None:
        """Update names of presets based on database."""
        self.presets_names = get_all_preset_names()

state = State()

def render(html_name: str) -> str:
    return render_template(
        html_name,
        subregions=state.subregions,
        preset_names=state.presets_names,
        rural_urban_state=state.rural_urban,
        male_female_state=state.male_female
    )

@app.route("/")
def index():
    return render("index.html")

@app.route("/load", methods=["POST"])
def on_load():
    p_name = request.form.get("presets")
    if p_name != "":
        chosen_settings = get_preset_settings(p_name)
        state.update_settings(**chosen_settings)
    return render("index.html")

@app.route('/save', methods=['POST'])
def on_save():
    preset_name  = request.form.get("preset_input")
    checked_subs = request.form.getlist('subregions')
    rural_urban  = request.form.get("rural_urban")
    male_female  = request.form.get("male_female")
    
    state.update_settings(checked_subs, rural_urban, male_female)
    if checked_subs != []:
        try:
            save_preset(preset_name, checked_subs, rural_urban, male_female)
            state.update_presets_names()
            return render('saved_preset.html')
        except InFailedSqlTransaction as e:
            print(e)
            return render('no_preset_saved.html')
    else:
        return render('no_preset_saved.html')

@app.route("/delete", methods=["POST"])
def on_delete():
    p_name = request.form.get("presets")
    if p_name != "":
        delete_preset(p_name)
        state.update_presets_names()
        return render('deleted_preset.html')
    else:
        return render('no_preset_deleted.html')

@app.route('/submit', methods=["POST"])
def on_submit():
    checked_subs = request.form.getlist("subregions")
    rural_urban = request.form.get("rural_urban")
    male_female = request.form.get("male_female")
    
    state.update_settings(checked_subs, rural_urban, male_female)
    if checked_subs != []:
        try:
            update_plot(checked_subs, rural_urban, male_female)
            return render('submitted.html')
        except NoDataException:
            pass
    return render("no_countries.html")

