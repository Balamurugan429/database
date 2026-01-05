import sqlite3
from datetime import datetime
import requests

def save_weather(temp, wind):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO weather (temperature, wind, time) VALUES (?, ?, ?)",
                (temp, wind, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"
    data = requests.get(url).json()
    w = data["current_weather"]
    print("Temp:", w["temperature"], "Wind:", w["windspeed"])
    save_weather(w["temperature"], w["windspeed"])

def show_history():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM weather ORDER BY id DESC LIMIT 5").fetchall()
    conn.close()

    print("\nLast 5 Weather Records:")
    for r in rows:
        print(r)

while True:
    print("\n1. Fetch Weather\n2. View History\n3. Exit")
    c = input("Choose: ")
    if c == "1": get_weather()
    elif c == "2": show_history()
    elif c == "3": break
