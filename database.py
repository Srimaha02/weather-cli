import sqlite3
from datetime import datetime

DB_FILE = "weather.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS searches (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            city      TEXT,
            country   TEXT,
            temperature REAL,
            humidity  INTEGER,
            condition TEXT,
            searched_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_search(city, country, temp, humidity, condition):
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT INTO searches (city, country, temperature, humidity, condition, searched_at) VALUES (?,?,?,?,?,?)",
        (city, country, temp, humidity, condition, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()
    print("📅  Saved to history!")

def get_history():
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute(
        "SELECT city, country, temperature, condition, searched_at FROM searches ORDER BY id DESC LIMIT 5"
    ).fetchall()
    conn.close()
    return rows