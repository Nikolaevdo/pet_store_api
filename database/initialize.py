import os
import sqlite3
from datetime import datetime
from pathlib import Path

BD_NAME = "pets.db"
DIR = Path(__file__).parent.absolute()
DB_FILE = os.path.join(DIR, BD_NAME)


def initialize_database():
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
             CREATE TABLE pets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                type TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """)
            pets = [
                ("Oscar", 2, "cat", datetime.now().isoformat()),
                ("Kitty", 2, "cat", datetime.now().isoformat()),
                ("Benson", 3, "dog", datetime.now().isoformat()),
                ("hachiko", 1, "dog", datetime.now().isoformat())
            ]
            cursor.executemany("INSERT INTO pets "
                               "(name, age, type, created_at) VALUES (?, ?, ?, ?)", pets)
            conn.commit()
            print("{INFO} Database initialized successfully")

    except sqlite3.Error as e:
        if "table pets already exists" in str(e):
            print("[INFO] Database already initialized")
        else:
            print(f"[Warring]: Error initializing database: {e}")
