import sqlite3
import streamlit as st

# Connect to SQLite database (will create if it does not exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hall_ticket TEXT,
    email TEXT,
    notified INTEGER DEFAULT 0
)
""")
conn.commit()
