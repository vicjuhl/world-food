from flask import render_template, request, Blueprint
from app.models import update_plot, get_all_regions, get_all_preset_names, get_preset
from app import app
from app.utils.exceptions import NoDataException

Router = Blueprint('Router', __name__)

# Initialize states
subregions_state = {region: False for region in get_all_regions()}
presets_names = get_all_preset_names()

def update_subregions(checked_subs: list[str]):
    """Set and remember values of subregion checkboxes."""
    for sub in subregions_state.keys():
        subregions_state[sub] = sub in checked_subs

@app.route("/")
def index():
    return render_template(
        "index.html",
        subregions=subregions_state,
        preset_names=presets_names
    )

@app.route("/load", methods=["POST"])
def on_load():
    p_name = request.form.get("presets")
    if p_name != "":
        chosen_preset = get_preset(p_name)
        update_subregions(chosen_preset["sub_regions"])
    return render_template(
        "index.html",
        subregions=subregions_state,
        preset_names=presets_names
    )

@app.route('/submit', methods=["POST"])
def on_submit():
    checked_subs = request.form.getlist("subregions")
    update_subregions(checked_subs)
    if checked_subs != []:
        try:
            update_plot(checked_subs)
            return render_template(
                'submitted.html',
                subregions=subregions_state,
                preset_names=presets_names
            )
        except NoDataException:
            pass
    return render_template(
        'no_countries.html',
        subregions=subregions_state,
        preset_names=presets_names
    )

@app.route('/save', methods=['POST'])
def on_save():
    checked_subs = request.form.getlist('subregions')
    update_subregions(checked_subs)
    print(checked_subs)
    # return render_template(
    #     'index.html',

    # )

