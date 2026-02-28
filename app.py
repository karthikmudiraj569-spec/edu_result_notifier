import streamlit as st
import sqlite3

st.title("🎓 EduResult Notifier")

hall_ticket = st.text_input("Enter Hall Ticket Number")
email = st.text_input("Enter Email")

if st.button("Notify Me"):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO students (hall_ticket, email) VALUES (?, ?)",
                   (hall_ticket, email))
    
    conn.commit()
    conn.close()
    
    st.success("You will be notified when results are released!")
