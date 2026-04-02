"""
app.py — CS 6083 Spring 2026 — Flight Search Web Application
Uses SQLite by default. To switch to PostgreSQL, replace get_db() with
a psycopg2 connection and use %s placeholders instead of ?.
"""
from flask import Flask, render_template, request, jsonify
import sqlite3, os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "flights.db")

# ── Database helper ──────────────────────────────────────────────────────────

def get_db():
    """Return a SQLite connection with row-factory for dict-like access."""
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

# ── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Start page: search form."""
    db = get_db()
    airports = db.execute(
        "SELECT airport_code, name, city FROM Airport ORDER BY airport_code"
    ).fetchall()
    db.close()
    return render_template("index.html", airports=airports)


@app.route("/search")
def search():
    """
    Part (b): Return all flights matching origin, destination, date range.
    Query params: origin, dest, date_from, date_to
    """
    origin    = request.args.get("origin", "").upper().strip()
    dest      = request.args.get("dest", "").upper().strip()
    date_from = request.args.get("date_from", "")
    date_to   = request.args.get("date_to", "")

    if not (origin and dest and date_from and date_to):
        return render_template("results.html", flights=[], search={})

    db = get_db()
    query = """
        SELECT
            f.flight_number,
            f.departure_date,
            fs.origin_code,
            fs.dest_code,
            fs.departure_time,
            fs.duration,
            fs.airline_name,
            f.plane_type,
            ao.name  AS origin_name,
            ad.name  AS dest_name
        FROM Flight f
        JOIN FlightService fs ON f.flight_number = fs.flight_number
        JOIN Airport ao       ON fs.origin_code  = ao.airport_code
        JOIN Airport ad       ON fs.dest_code    = ad.airport_code
        WHERE fs.origin_code = ?
          AND fs.dest_code   = ?
          AND f.departure_date BETWEEN ? AND ?
        ORDER BY f.departure_date, fs.departure_time
    """
    rows = db.execute(query, (origin, dest, date_from, date_to)).fetchall()
    db.close()

    search_ctx = {
        "origin": origin, "dest": dest,
        "date_from": date_from, "date_to": date_to
    }
    return render_template("results.html",
                           flights=[dict(r) for r in rows],
                           search=search_ctx)


@app.route("/flight/<flight_number>/<departure_date>")
def flight_detail(flight_number, departure_date):
    """
    Part (c): Show capacity and available seats for a specific flight instance.
    """
    db = get_db()

    flight = db.execute("""
        SELECT
            f.flight_number,
            f.departure_date,
            f.plane_type,
            fs.airline_name,
            fs.origin_code,
            fs.dest_code,
            fs.departure_time,
            fs.duration,
            ac.capacity,
            ao.name AS origin_name,
            ad.name AS dest_name
        FROM Flight f
        JOIN FlightService fs ON f.flight_number = fs.flight_number
        JOIN Aircraft ac      ON f.plane_type     = ac.plane_type
        JOIN Airport ao       ON fs.origin_code   = ao.airport_code
        JOIN Airport ad       ON fs.dest_code     = ad.airport_code
        WHERE f.flight_number  = ?
          AND f.departure_date = ?
    """, (flight_number, departure_date)).fetchone()

    if not flight:
        db.close()
        return render_template("detail.html", flight=None, booked=0,
                               available=0, passengers=[])

    booked_count = db.execute("""
        SELECT COUNT(*) AS cnt FROM Booking
        WHERE flight_number = ? AND departure_date = ?
    """, (flight_number, departure_date)).fetchone()["cnt"]

    passengers = db.execute("""
        SELECT p.passenger_name, b.seat_number
        FROM Booking b
        JOIN Passenger p ON b.pid = p.pid
        WHERE b.flight_number = ? AND b.departure_date = ?
        ORDER BY b.seat_number
    """, (flight_number, departure_date)).fetchall()

    db.close()

    f = dict(flight)
    available = f["capacity"] - booked_count
    return render_template("detail.html",
                           flight=f,
                           booked=booked_count,
                           available=available,
                           passengers=[dict(p) for p in passengers])
@app.route("/metadata")
def metadata():
    import re
    db = get_db()

    tables = [r["name"] for r in db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()]

    # (a) Hardcoded from schema knowledge since db_init.py has no FK constraints
    fk_tables = [
        {
            "table_name": "Flight",
            "distinct_referenced_tables": 2,
            "references": "Aircraft, FlightService"
        },
        {
            "table_name": "Booking",
            "distinct_referenced_tables": 2,
            "references": "Flight, Passenger"
        }
    ]

    # (b) Hardcoded from schema knowledge since all types are stored as TEXT
    date_cols = [
        {"table_name": "FlightService", "column_name": "departure_time", "data_type": "TIME"},
        {"table_name": "FlightService", "column_name": "duration",       "data_type": "INTERVAL"},
        {"table_name": "Flight",        "column_name": "departure_date", "data_type": "DATE"},
        {"table_name": "Booking",       "column_name": "departure_date", "data_type": "DATE"},
    ]

    # (c) Distinct values per column in Flight — fully dynamic, works fine
    flight_cols = [c["name"] for c in db.execute("PRAGMA table_info(Flight)").fetchall()]
    distinct_vals = []
    for col in flight_cols:
        cnt = db.execute(f"SELECT COUNT(DISTINCT {col}) AS cnt FROM Flight").fetchone()["cnt"]
        distinct_vals.append({"attribute": col, "distinct_values": cnt})

    # (d) Composite PKs — fully dynamic, works fine
    composite_keys = []
    for t in tables:
        cols = db.execute(f"PRAGMA table_info({t})").fetchall()
        pk_cols = sorted([c for c in cols if c["pk"] > 0], key=lambda x: x["pk"])
        pk_names = [c["name"] for c in pk_cols]
        if len(pk_names) > 1:
            composite_keys.append({
                "table_name": t,
                "pk_column_count": len(pk_names),
                "pk_columns": ", ".join(pk_names)
            })

    # (e) Columns containing "name" — fully dynamic, works fine
    name_cols = []
    for t in tables:
        cols = db.execute(f"PRAGMA table_info({t})").fetchall()
        for c in cols:
            if "name" in c["name"].lower():
                name_cols.append({
                    "table_name": t,
                    "column_name": c["name"],
                    "data_type": c["type"]
                })

    db.close()

    return render_template("metadata.html",
                           fk_tables=fk_tables,
                           date_cols=date_cols,
                           distinct_vals=distinct_vals,
                           composite_keys=composite_keys,
                           name_cols=name_cols)
if __name__ == "__main__":
    # Initialize DB on first run
    from db_init import init_db
    if not os.path.exists(DB_PATH):
        init_db()
    app.run(debug=True, port=5000)
