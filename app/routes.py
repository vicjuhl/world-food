from flask import render_template, request, Blueprint
from app.models import update_plot, get_all_regions
from app import app
from app.utils.exceptions import NoDataException

Router = Blueprint('Router', __name__)

subregions_state = {region: False for region in get_all_regions()}

def update_subregions(checked_subs: list[str]):
    """Set and remember values of subregion checkboxes."""
    for sub in subregions_state.keys():
        subregions_state[sub] = sub in checked_subs

@app.route("/")
def index():
    return render_template("index.html", subregions=subregions_state)

@app.route('/submit', methods=["POST"])
def on_submit():
    checked_subs = request.form.getlist("subregions")
    update_subregions(checked_subs)
    if checked_subs != []:
        try:
            update_plot(checked_subs)
            return render_template('submitted.html', subregions=subregions_state)
        except NoDataException:
            pass
    return render_template('no_countries.html', subregions=subregions_state)