from flask import render_template, request, Blueprint
from app.models import fetch_test, fetch_region, update_plot, get_all_regions
from app import app

Router = Blueprint('Router', __name__)

@app.route("/")
def index():
    return render_template("index.html", sub_regions=get_all_regions())

@app.route('/submit', methods=["POST"])
def on_submit():
    update_plot(request.form["subregion"])
    return render_template('submitted.html')