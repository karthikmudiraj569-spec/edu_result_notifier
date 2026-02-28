import requests
from bs4 import BeautifulSoup
import sqlite3
import smtplib
from email.mime.text import MIMEText

RESULT_PAGE = "http://results.jntuh.ac.in/results/"

def check_results():
    response = requests.get(RESULT_PAGE)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Example: check if specific keyword exists
    if "B.Tech 4-2 Results Released" in soup.text:
        send_notifications()

def send_notifications():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT email FROM students WHERE notified=0")
    students = cursor.fetchall()
    
    for student in students:
        send_email(student[0])
    
    cursor.execute("UPDATE students SET notified=1")
    conn.commit()
    conn.close()

def send_email(receiver_email):
    sender_email = "your_email@gmail.com"
    password = "your_app_password"

    msg = MIMEText("🎓 Results are released! Check the university website.")
    msg["Subject"] = "Results Released!"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()

check_results()
