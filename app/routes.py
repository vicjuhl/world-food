from flask import render_template, request, Blueprint
from app.models import fetch_test
from app import app

Router = Blueprint('Router', __name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def on_submit():
    return render_template("submitted.html", data=fetch_test(request.form["fname"]))