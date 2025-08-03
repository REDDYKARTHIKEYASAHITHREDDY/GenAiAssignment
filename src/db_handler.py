import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'tournaments.db')

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Tournaments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    level TEXT,
                    start_date TEXT,
                    end_date TEXT,
                    official_url TEXT,
                    streaming_links TEXT,
                    image_url TEXT,
                    summary TEXT
                )''')
    conn.commit()
    conn.close()

def insert_tournament(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO Tournaments (name, level, start_date, end_date, official_url, streaming_links, image_url, summary)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', data)
    conn.commit()
    conn.close()

def get_all_tournaments():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM Tournaments')
    rows = c.fetchall()
    columns = [column[0] for column in c.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows]