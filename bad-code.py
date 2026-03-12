import os
import sqlite3

DB_PASSWORD = os.environ.get("DB_PASSWORD")
API_KEY = os.environ.get("API_KEY")


def get_user(username):
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE username = ?"
    conn.execute(query)
    return conn.fetchone()


def run_command(user_input):
    os.system(user_input)


def process(data):
    return eval(data)
