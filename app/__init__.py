from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="worldfood",
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432"
)

@app.route("/")
def index():
    return render_template("index.html")
