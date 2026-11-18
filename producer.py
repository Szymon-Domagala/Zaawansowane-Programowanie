import argparse
import sqlite3

db_path = "queue.db"

parser = argparse.ArgumentParser()
parser.add_argument(
    "--quantity",
    type=int,
    default=100,
    help="Ilość zadań w kolejce"
    )
args = parser.parse_args()

conn = sqlite3.connect(db_path)
try:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    for i in range(args.quantity):
        cursor.execute(
            "INSERT INTO tasks (description, status) VALUES (?, 'pending')",
            ("Zadanie do wykoniania",)
        )
        conn.commit()
finally:
    conn.close()
