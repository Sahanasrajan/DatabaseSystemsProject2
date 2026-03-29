"""
db_init.py — Creates and seeds the SQLite database from the flights schema.
Swap get_db() in app.py with a psycopg2 connection to use PostgreSQL.
"""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), "flights.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS Airport (
    airport_code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Aircraft (
    plane_type TEXT PRIMARY KEY,
    capacity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS FlightService (
    flight_number TEXT PRIMARY KEY,
    airline_name TEXT NOT NULL,
    origin_code TEXT NOT NULL,
    dest_code TEXT NOT NULL,
    departure_time TEXT NOT NULL,
    duration TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Flight (
    flight_number TEXT NOT NULL,
    departure_date TEXT NOT NULL,
    plane_type TEXT NOT NULL,
    PRIMARY KEY (flight_number, departure_date)
);

CREATE TABLE IF NOT EXISTS Passenger (
    pid INTEGER PRIMARY KEY,
    passenger_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Booking (
    pid INTEGER NOT NULL,
    flight_number TEXT NOT NULL,
    departure_date TEXT NOT NULL,
    seat_number INTEGER NOT NULL,
    PRIMARY KEY (pid, flight_number, departure_date)
);
"""

DATA = """
INSERT OR IGNORE INTO Airport VALUES
('JFK','John F Kennedy International','New York','United States'),
('LAX','Los Angeles International','Los Angeles','United States'),
('ORD','O''Hare International','Chicago','United States'),
('MDW','Midway International','Chicago','United States'),
('LHR','Heathrow Airport','London','United Kingdom'),
('CDG','Charles de Gaulle Airport','Paris','France'),
('ORY','Paris Orly Airport','Paris','France'),
('SFO','San Francisco International','San Francisco','United States'),
('MIA','Miami International','Miami','United States'),
('ATL','Hartsfield-Jackson International','Atlanta','United States'),
('NRT','Narita International','Tokyo','Japan'),
('SIN','Changi Airport','Singapore','Singapore');

INSERT OR IGNORE INTO Aircraft VALUES
('CRJ-200',10),('Boeing 737',20),('Airbus A320',15),('Boeing 787',25);

INSERT OR IGNORE INTO FlightService VALUES
('AA101','American Airlines','JFK','LAX','08:00','3h 30m'),
('AA205','American Airlines','JFK','LAX','14:00','3h 30m'),
('UA302','United Airlines','SFO','ORD','09:00','6h'),
('DL410','Delta Air Lines','ATL','MIA','10:00','2h 30m'),
('BA178','British Airways','LHR','JFK','10:00','3h'),
('AF023','Air France','CDG','NRT','22:00','19h'),
('SQ321','Singapore Airlines','SIN','LHR','23:00','7h'),
('AA550','American Airlines','ORD','MIA','07:00','4h'),
('DL620','Delta Air Lines','JFK','ATL','16:00','2h 30m'),
('UA789','United Airlines','LAX','SFO','12:00','1h 30m');

INSERT OR IGNORE INTO Flight VALUES
('AA101','2025-12-29','Boeing 737'),
('AA101','2025-12-31','Boeing 737'),
('AA205','2025-12-31','Boeing 737'),
('UA302','2025-12-31','CRJ-200'),
('DL410','2025-12-31','Airbus A320'),
('BA178','2025-12-31','Boeing 787'),
('AF023','2025-12-30','Boeing 787'),
('SQ321','2025-12-30','Boeing 787'),
('DL620','2025-12-30','Airbus A320'),
('DL620','2025-12-31','Airbus A320'),
('AA550','2025-12-31','CRJ-200'),
('UA789','2025-12-31','Airbus A320');

INSERT OR IGNORE INTO Passenger VALUES
(1,'John Adams'),(2,'Sarah Miller'),(3,'Michael Chen'),(4,'Emily Wong'),
(5,'David Park'),(6,'Lisa Johnson'),(7,'James Brown'),(8,'Maria Garcia'),
(9,'Robert Kim'),(10,'Jennifer Lee'),(11,'Thomas Wilson'),(12,'Amanda Clark'),
(13,'Christopher Davis'),(14,'Jessica Martinez'),(15,'Daniel Taylor'),
(16,'Rachel Anderson'),(17,'William Thomas'),(18,'Nicole White'),
(19,'Kevin Harris'),(20,'Stephanie Moore'),(21,'Andrew Jackson'),
(22,'Michelle Robinson'),(23,'Brian Lewis'),(24,'Laura Walker'),(25,'Steven Hall');

INSERT OR IGNORE INTO Booking VALUES
(1,'AA101','2025-12-29',1),(2,'AA101','2025-12-29',2),(3,'AA101','2025-12-29',3),
(4,'AA101','2025-12-29',4),(5,'AA101','2025-12-29',5),
(1,'AA101','2025-12-31',1),(2,'AA101','2025-12-31',2),(3,'AA101','2025-12-31',3),
(4,'AA101','2025-12-31',4),(5,'AA101','2025-12-31',5),(6,'AA101','2025-12-31',6),
(7,'AA101','2025-12-31',7),(8,'AA101','2025-12-31',8),(9,'AA101','2025-12-31',9),
(10,'AA101','2025-12-31',10),(11,'AA101','2025-12-31',11),(12,'AA101','2025-12-31',12),
(13,'AA101','2025-12-31',13),(14,'AA101','2025-12-31',14),(15,'AA101','2025-12-31',15),
(16,'AA205','2025-12-31',1),(17,'AA205','2025-12-31',2),(18,'AA205','2025-12-31',3),
(19,'AA205','2025-12-31',4),
(1,'UA302','2025-12-31',1),(2,'UA302','2025-12-31',2),(3,'UA302','2025-12-31',3),
(4,'UA302','2025-12-31',4),(5,'UA302','2025-12-31',5),(6,'UA302','2025-12-31',6),
(7,'UA302','2025-12-31',7),(8,'UA302','2025-12-31',8),(9,'UA302','2025-12-31',9),
(10,'UA302','2025-12-31',10),
(5,'DL410','2025-12-31',1),(6,'DL410','2025-12-31',2),(7,'DL410','2025-12-31',3),
(8,'DL410','2025-12-31',4),(9,'DL410','2025-12-31',5),(10,'DL410','2025-12-31',6),
(11,'DL410','2025-12-31',7),(12,'DL410','2025-12-31',8),(13,'DL410','2025-12-31',9),
(14,'DL410','2025-12-31',10),(15,'DL410','2025-12-31',11),(16,'DL410','2025-12-31',12),
(17,'DL410','2025-12-31',13),(18,'DL410','2025-12-31',14),
(20,'BA178','2025-12-31',1),(21,'BA178','2025-12-31',2),(22,'BA178','2025-12-31',3),
(23,'BA178','2025-12-31',4),(24,'BA178','2025-12-31',5),(25,'BA178','2025-12-31',6),
(1,'AF023','2025-12-30',1),(2,'AF023','2025-12-30',2),(3,'AF023','2025-12-30',3),
(4,'AF023','2025-12-30',4),
(5,'SQ321','2025-12-30',1),(6,'SQ321','2025-12-30',2),(7,'SQ321','2025-12-30',3),
(10,'DL620','2025-12-30',1),(11,'DL620','2025-12-30',2),(12,'DL620','2025-12-30',3),
(13,'DL620','2025-12-30',4),
(20,'DL620','2025-12-31',1),(21,'DL620','2025-12-31',2),(22,'DL620','2025-12-31',3),
(23,'DL620','2025-12-31',4),(24,'DL620','2025-12-31',5),
(8,'AA550','2025-12-31',1),(9,'AA550','2025-12-31',2),(10,'AA550','2025-12-31',3),
(11,'AA550','2025-12-31',4),(12,'AA550','2025-12-31',5),(13,'AA550','2025-12-31',6),
(14,'AA550','2025-12-31',7),
(22,'UA789','2025-12-31',1),(23,'UA789','2025-12-31',2),(24,'UA789','2025-12-31',3);
"""

def init_db():
    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA + DATA)
    con.commit()
    con.close()
    print(f"Database initialized at {DB_PATH}")

if __name__ == "__main__":
    init_db()
