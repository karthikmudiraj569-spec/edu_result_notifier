import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hall_ticket TEXT,
    email TEXT,
    notified INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()
