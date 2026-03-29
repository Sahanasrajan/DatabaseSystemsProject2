# CS 6083 Spring 2026 — Question 2: Flight Web Application

A Flask web application providing a browser-based interface to the flight database.

## Setup & Run

```bash
# 1. Install dependencies
pip install flask psycopg2-binary   # psycopg2-binary only needed for PostgreSQL

# 2. Run (auto-initializes SQLite DB on first launch)
python app.py
```

Then open **http://localhost:5000** in your browser.

---

## Features (matching assignment spec)

### (a) Start Page — Search Form
- Dropdown selectors for **origin** and **destination** airport codes
- **Date range** pickers (from / to)
- Submit button

### (b) Flight Results
After submitting, displays all matching flights with:
- Flight number
- Departure date
- Origin & destination codes (and full airport names)
- Departure time (GMT)
- Airline name
- Aircraft type
- Duration

### (c) Flight Detail — Click any flight row
Clicking a flight row shows:
- **Capacity** of the aircraft
- **Number of booked seats**
- **Available seats** (capacity − booked)
- Visual occupancy progress bar
- Full passenger manifest with seat numbers

---

## Switching to PostgreSQL

In `app.py`, replace `get_db()` with:

```python
import psycopg2, psycopg2.extras

def get_db():
    con = psycopg2.connect(
        host="localhost", dbname="flights",
        user="postgres", password="yourpassword"
    )
    con.cursor_factory = psycopg2.extras.RealDictCursor
    return con
```

Then change all `?` placeholders in queries to `%s` (PostgreSQL style).
Load the schema from `flights.sql` directly:

```bash
psql -U postgres -d flights -f flights.sql
```

---

## Project Structure

```
flights_app/
├── app.py          # Flask routes
├── db_init.py      # SQLite schema + seed data
├── flights.db      # Auto-created on first run
├── README.md
└── templates/
    ├── base.html   # Shared layout / nav
    ├── index.html  # (a) Search form
    ├── results.html# (b) Flight list
    └── detail.html # (c) Seat availability
```

## Test Data

The app is pre-loaded with the data from the homework SQL file:
- 12 airports, 4 aircraft types, 10 flight services
- 12 flight instances across 2025-12-29 to 2025-12-31
- 25 passengers, ~75 bookings

**Quick test:** Search JFK → LAX, dates 2025-12-29 to 2025-12-31.
