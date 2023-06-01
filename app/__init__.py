from flask import Flask, render_template, request
# from app.models import fetch_test
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="worldfood",
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432"
)


def fetch_test():
    cur = conn.cursor()
    sql = """
        SELECT *
        FROM Affordability
    """
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    return str(result[0])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def on_submit():
    print(request.form["fname"])
    return render_template("submitted.html", data=fetch_test())