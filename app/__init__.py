from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="worldfood",
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432"
)
