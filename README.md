# Day 3 — SQLite Persistence 🗄️

This project extends the API dashboard by adding a local SQLite database to store and retrieve weather data.

Instead of just displaying live data, the application now saves each fetch into a database and allows the user to view past records.

---

## Features

* Fetches live weather data from Open-Meteo API
* Stores temperature, wind speed, and timestamp in SQLite
* Displays the last 5 saved weather records
* Uses a menu-based CLI interface
* Automatically creates the database and table if not present

---

## Technologies Used

* Python 3
* SQLite (via sqlite3 module)
* requests library
* REST APIs

---

## File Structure

```
day3/
 ├── api_dashboard.py
 ├── database.py
 ├── data.db
 └── README.md
```

---

## How to Run

1. Install dependencies:

```
pip install requests
```

2. Initialize the database:

```
python database.py
```

3. Run the dashboard:

```
python api_dashboard.py
```

---

## Example Output

```
Last 5 Weather Records:
(2, 28.0, 12.8, '2026-01-05T11:37:46.329148')
(1, 28.0, 12.8, '2026-01-05T11:36:18.603086')
```

---

## Learning Outcome

Through this project I learned:

* How to use SQLite with Python
* How to perform INSERT and SELECT queries
* How to store persistent application data
* How to structure backend logic cleanly

---

## Author

Balamurugan
