import sqlite3
import time

db_path = "queue.db"

conn = sqlite3.connect(db_path)
try:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
finally:
    conn.close()

while True:
    time.sleep(5)
    task_id = None

    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tasks
            SET status = 'in_progress'
            WHERE id = (
                SELECT id FROM tasks WHERE status = 'pending' LIMIT 1
            )
            RETURNING id
        """)
        rows = cursor.fetchall()
        if rows:
            task_id = rows[0][0]
        conn.commit()
    finally:
        conn.close()

    if task_id is not None:
        print(f"Przyjęto zadanie - {task_id}")
        time.sleep(30)

        conn = sqlite3.connect(db_path)
        try:
            conn.execute(
                "UPDATE tasks SET status = 'done' where id = ?",
                (task_id,)
            )
            conn.commit()
            print(f"Wykonano zadanie - {task_id}")
        finally:
            conn.close()
