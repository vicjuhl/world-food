from flask import render_template, request, Blueprint
from app.models import (
    update_plot,
    get_all_regions,
    get_all_preset_names,
    get_preset,
    save_preset
)
from app import app
from app.utils.exceptions import NoDataException

Router = Blueprint('Router', __name__)

# Initialize states
class State:
    def __init__(self) -> None:
        self.subregions_state = {region: False for region in get_all_regions()}
        self.presets_names = get_all_preset_names()

    def update_subregions(self, checked_subs: list[str]) -> None:
        """Set and remember values of subregion checkboxes."""
        for sub in self.subregions_state.keys():
            self.subregions_state[sub] = sub in checked_subs

    def update_presets_names(self) -> None:
        """Update names of presets based on database."""
        self.presets_names = get_all_preset_names()

state = State()

def render(html_name: str) -> str:
    return render_template(
        html_name,
        subregions=state.subregions_state,
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

@app.route('/submit', methods=["POST"])
def on_submit():
    checked_subs = request.form.getlist("subregions")
    state.update_subregions(checked_subs)
    if checked_subs != []:
        try:
            update_plot(checked_subs)
            return render_template(
                'submitted.html',
                subregions=state.subregions_state,
                preset_names=state.presets_names
            )
        except NoDataException:
            pass
    return render("no_countries.html")

@app.route('/save', methods=['POST'])
def on_save():
    checked_subs = request.form.getlist('subregions')
    preset_name  = request.form.get("preset_input")
    state.update_subregions(checked_subs)
    save_preset(preset_name, checked_subs)
    state.update_presets_names()
    return render('saved_preset.html')

