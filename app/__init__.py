from flask import Flask
import psycopg2
import pathlib as pl

# Prepare Directories
plot_dir = pl.Path(__file__).parent.resolve() / "static/images/"
plot_dir.mkdir(parents=True, exist_ok=True)

# Open app and connections
app = Flask(__name__)

conn = psycopg2.connect(
    dbname="worldfood",
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432"
)

from app.routes import Router
app.register_blueprint(Router)