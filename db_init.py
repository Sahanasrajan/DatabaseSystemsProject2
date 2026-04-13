import sqlite3, os, re

DB_PATH = os.path.join(os.path.dirname(__file__), "flights.db")
SQL_PATH = os.path.join(os.path.dirname(__file__), "flights.sql")

def init_db():
    # Read the SQL file
    with open(SQL_PATH, "r") as f:
        sql = f.read()

    # Remove PostgreSQL-specific syntax that SQLite doesn't understand
    sql = re.sub(r"INTERVAL\s+'[^']*'", lambda m: "'" + m.group(0).split("'")[1] + "'", sql)
    sql = re.sub(r"\bTIME\b", "TEXT", sql)
    sql = re.sub(r"\bDATE\b", "TEXT", sql)
    sql = re.sub(r"\bINTERVAL\b", "TEXT", sql)

    con = sqlite3.connect(DB_PATH)
    con.executescript(sql)
    con.commit()
    con.close()
    print(f"Database created at {DB_PATH}")

if __name__ == "__main__":
    init_db()
