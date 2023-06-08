from flask import render_template, request, Blueprint

from app.models import (
    update_plot,
    get_all_regions,
    get_all_preset_names,
    get_preset,
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
        self.rural_urban = "average"

    def update_subregions(self, checked_subs: list[str]) -> None:
        """Set and remember values of subregion checkboxes."""
        for sub in self.subregions.keys():
            self.subregions[sub] = sub in checked_subs

    def update_presets_names(self) -> None:
        """Update names of presets based on database."""
        self.presets_names = get_all_preset_names()

state = State()

def render(html_name: str) -> str:
    return render_template(
        html_name,
        subregions=state.subregions,
        preset_names=state.presets_names
    )

@app.route("/")
def index():
    return render("index.html")

@app.route("/load", methods=["POST"])
def on_load():
    p_name = request.form.get("presets")
    if p_name != "":
        chosen_preset = get_preset(p_name)
        state.update_subregions(chosen_preset["sub_regions"])
    return render("index.html")

@app.route('/save', methods=['POST'])
def on_save():
    checked_subs = request.form.getlist('subregions')
    preset_name  = request.form.get("preset_input")
    state.update_subregions(checked_subs)
    if checked_subs != []:
        save_preset(preset_name, checked_subs)
        state.update_presets_names()
        return render('saved_preset.html')
    else:
        return render('no_preset_saved.html')

@app.route("/delete", methods=["POST"])
def on_delete():
    p_name = request.form.get("presets")
    if p_name != "":
        delete_preset(p_name)
    state.update_presets_names()
    return render("index.html")

@app.route('/submit', methods=["POST"])
def on_submit():
    checked_subs = request.form.getlist("subregions")
    state.update_subregions(request.form.getlist("subregions"))
    state.rural_urban = request.form.get("rural_urban")
    if checked_subs != []:
        try:
            update_plot(checked_subs, state.rural_urban)
            return render('submitted.html')
        except NoDataException:
            pass
    return render("no_countries.html")

