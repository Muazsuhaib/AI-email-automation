import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    task TEXT
)
""")

conn.commit()


def save_task(task):

    cursor.execute("INSERT INTO tasks(task) VALUES (?)", (task,))
    conn.commit()
