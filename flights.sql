CREATE TABLE Airport (
    airport_code VARCHAR(3) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL
);

CREATE TABLE Aircraft (
    plane_type VARCHAR(30) PRIMARY KEY,
    capacity INT NOT NULL
);

CREATE TABLE FlightService (
    flight_number VARCHAR(10) PRIMARY KEY,
    airline_name VARCHAR(50) NOT NULL,
    origin_code VARCHAR(3) NOT NULL,
    dest_code VARCHAR(3) NOT NULL,
    departure_time TEXT NOT NULL,
    duration TEXT NOT NULL
);

CREATE TABLE Flight (
    flight_number VARCHAR(10) NOT NULL,
    departure_date TEXT NOT NULL,
    plane_type VARCHAR(30) NOT NULL,
    PRIMARY KEY (flight_number, departure_date)
);

CREATE TABLE Passenger (
    pid INT PRIMARY KEY,
    passenger_name VARCHAR(100) NOT NULL
);

CREATE TABLE Booking (
    pid INT NOT NULL,
    flight_number VARCHAR(10) NOT NULL,
    departure_date TEXT NOT NULL,
    seat_number INT NOT NULL,
    PRIMARY KEY (pid, flight_number, departure_date)
);

INSERT INTO Airport VALUES ('JFK','John F Kennedy International','New York','United States');
INSERT INTO Airport VALUES ('LAX','Los Angeles International','Los Angeles','United States');
INSERT INTO Airport VALUES ('ORD','O''Hare International','Chicago','United States');
INSERT INTO Airport VALUES ('MDW','Midway International','Chicago','United States');
INSERT INTO Airport VALUES ('LHR','Heathrow Airport','London','United Kingdom');
INSERT INTO Airport VALUES ('CDG','Charles de Gaulle Airport','Paris','France');
INSERT INTO Airport VALUES ('ORY','Paris Orly Airport','Paris','France');
INSERT INTO Airport VALUES ('SFO','San Francisco International','San Francisco','United States');
INSERT INTO Airport VALUES ('MIA','Miami International','Miami','United States');
INSERT INTO Airport VALUES ('ATL','Hartsfield-Jackson International','Atlanta','United States');
INSERT INTO Airport VALUES ('NRT','Narita International','Tokyo','Japan');
INSERT INTO Airport VALUES ('SIN','Changi Airport','Singapore','Singapore');

INSERT INTO Aircraft VALUES ('CRJ-200',10);
INSERT INTO Aircraft VALUES ('Boeing 737',20);
INSERT INTO Aircraft VALUES ('Airbus A320',15);
INSERT INTO Aircraft VALUES ('Boeing 787',25);

INSERT INTO FlightService VALUES ('AA101','American Airlines','JFK','LAX','08:00','3h 30m');
INSERT INTO FlightService VALUES ('AA205','American Airlines','JFK','LAX','14:00','3h 30m');
INSERT INTO FlightService VALUES ('UA302','United Airlines','SFO','ORD','09:00','6h');
INSERT INTO FlightService VALUES ('DL410','Delta Air Lines','ATL','MIA','10:00','2h 30m');
INSERT INTO FlightService VALUES ('BA178','British Airways','LHR','JFK','10:00','3h');
INSERT INTO FlightService VALUES ('AF023','Air France','CDG','NRT','22:00','19h');
INSERT INTO FlightService VALUES ('SQ321','Singapore Airlines','SIN','LHR','23:00','7h');
INSERT INTO FlightService VALUES ('AA550','American Airlines','ORD','MIA','07:00','4h');
INSERT INTO FlightService VALUES ('DL620','Delta Air Lines','JFK','ATL','16:00','2h 30m');
INSERT INTO FlightService VALUES ('UA789','United Airlines','LAX','SFO','12:00','1h 30m');

INSERT INTO Flight VALUES ('AA101','2025-12-29','Boeing 737');
INSERT INTO Flight VALUES ('AA101','2025-12-31','Boeing 737');
INSERT INTO Flight VALUES ('AA205','2025-12-31','Boeing 737');
INSERT INTO Flight VALUES ('UA302','2025-12-31','CRJ-200');
INSERT INTO Flight VALUES ('DL410','2025-12-31','Airbus A320');
INSERT INTO Flight VALUES ('BA178','2025-12-31','Boeing 787');
INSERT INTO Flight VALUES ('AF023','2025-12-30','Boeing 787');
INSERT INTO Flight VALUES ('SQ321','2025-12-30','Boeing 787');
INSERT INTO Flight VALUES ('DL620','2025-12-30','Airbus A320');
INSERT INTO Flight VALUES ('DL620','2025-12-31','Airbus A320');
INSERT INTO Flight VALUES ('AA550','2025-12-31','CRJ-200');
INSERT INTO Flight VALUES ('UA789','2025-12-31','Airbus A320');

INSERT INTO Passenger VALUES (1,'John Adams');
INSERT INTO Passenger VALUES (2,'Sarah Miller');
INSERT INTO Passenger VALUES (3,'Michael Chen');
INSERT INTO Passenger VALUES (4,'Emily Wong');
INSERT INTO Passenger VALUES (5,'David Park');
INSERT INTO Passenger VALUES (6,'Lisa Johnson');
INSERT INTO Passenger VALUES (7,'James Brown');
INSERT INTO Passenger VALUES (8,'Maria Garcia');
INSERT INTO Passenger VALUES (9,'Robert Kim');
INSERT INTO Passenger VALUES (10,'Jennifer Lee');
INSERT INTO Passenger VALUES (11,'Thomas Wilson');
INSERT INTO Passenger VALUES (12,'Amanda Clark');
INSERT INTO Passenger VALUES (13,'Christopher Davis');
INSERT INTO Passenger VALUES (14,'Jessica Martinez');
INSERT INTO Passenger VALUES (15,'Daniel Taylor');
INSERT INTO Passenger VALUES (16,'Rachel Anderson');
INSERT INTO Passenger VALUES (17,'William Thomas');
INSERT INTO Passenger VALUES (18,'Nicole White');
INSERT INTO Passenger VALUES (19,'Kevin Harris');
INSERT INTO Passenger VALUES (20,'Stephanie Moore');
INSERT INTO Passenger VALUES (21,'Andrew Jackson');
INSERT INTO Passenger VALUES (22,'Michelle Robinson');
INSERT INTO Passenger VALUES (23,'Brian Lewis');
INSERT INTO Passenger VALUES (24,'Laura Walker');
INSERT INTO Passenger VALUES (25,'Steven Hall');

INSERT INTO Booking VALUES (1,'AA101','2025-12-29',1);
INSERT INTO Booking VALUES (2,'AA101','2025-12-29',2);
INSERT INTO Booking VALUES (3,'AA101','2025-12-29',3);
INSERT INTO Booking VALUES (4,'AA101','2025-12-29',4);
INSERT INTO Booking VALUES (5,'AA101','2025-12-29',5);
INSERT INTO Booking VALUES (1,'AA101','2025-12-31',1);
INSERT INTO Booking VALUES (2,'AA101','2025-12-31',2);
INSERT INTO Booking VALUES (3,'AA101','2025-12-31',3);
INSERT INTO Booking VALUES (4,'AA101','2025-12-31',4);
INSERT INTO Booking VALUES (5,'AA101','2025-12-31',5);
INSERT INTO Booking VALUES (6,'AA101','2025-12-31',6);
INSERT INTO Booking VALUES (7,'AA101','2025-12-31',7);
INSERT INTO Booking VALUES (8,'AA101','2025-12-31',8);
INSERT INTO Booking VALUES (9,'AA101','2025-12-31',9);
INSERT INTO Booking VALUES (10,'AA101','2025-12-31',10);
INSERT INTO Booking VALUES (11,'AA101','2025-12-31',11);
INSERT INTO Booking VALUES (12,'AA101','2025-12-31',12);
INSERT INTO Booking VALUES (13,'AA101','2025-12-31',13);
INSERT INTO Booking VALUES (14,'AA101','2025-12-31',14);
INSERT INTO Booking VALUES (15,'AA101','2025-12-31',15);
INSERT INTO Booking VALUES (16,'AA205','2025-12-31',1);
INSERT INTO Booking VALUES (17,'AA205','2025-12-31',2);
INSERT INTO Booking VALUES (18,'AA205','2025-12-31',3);
INSERT INTO Booking VALUES (19,'AA205','2025-12-31',4);
INSERT INTO Booking VALUES (1,'UA302','2025-12-31',1);
INSERT INTO Booking VALUES (2,'UA302','2025-12-31',2);
INSERT INTO Booking VALUES (3,'UA302','2025-12-31',3);
INSERT INTO Booking VALUES (4,'UA302','2025-12-31',4);
INSERT INTO Booking VALUES (5,'UA302','2025-12-31',5);
INSERT INTO Booking VALUES (6,'UA302','2025-12-31',6);
INSERT INTO Booking VALUES (7,'UA302','2025-12-31',7);
INSERT INTO Booking VALUES (8,'UA302','2025-12-31',8);
INSERT INTO Booking VALUES (9,'UA302','2025-12-31',9);
INSERT INTO Booking VALUES (10,'UA302','2025-12-31',10);
INSERT INTO Booking VALUES (5,'DL410','2025-12-31',1);
INSERT INTO Booking VALUES (6,'DL410','2025-12-31',2);
INSERT INTO Booking VALUES (7,'DL410','2025-12-31',3);
INSERT INTO Booking VALUES (8,'DL410','2025-12-31',4);
INSERT INTO Booking VALUES (9,'DL410','2025-12-31',5);
INSERT INTO Booking VALUES (10,'DL410','2025-12-31',6);
INSERT INTO Booking VALUES (11,'DL410','2025-12-31',7);
INSERT INTO Booking VALUES (12,'DL410','2025-12-31',8);
INSERT INTO Booking VALUES (13,'DL410','2025-12-31',9);
INSERT INTO Booking VALUES (14,'DL410','2025-12-31',10);
INSERT INTO Booking VALUES (15,'DL410','2025-12-31',11);
INSERT INTO Booking VALUES (16,'DL410','2025-12-31',12);
INSERT INTO Booking VALUES (17,'DL410','2025-12-31',13);
INSERT INTO Booking VALUES (18,'DL410','2025-12-31',14);
INSERT INTO Booking VALUES (20,'BA178','2025-12-31',1);
INSERT INTO Booking VALUES (21,'BA178','2025-12-31',2);
INSERT INTO Booking VALUES (22,'BA178','2025-12-31',3);
INSERT INTO Booking VALUES (23,'BA178','2025-12-31',4);
INSERT INTO Booking VALUES (24,'BA178','2025-12-31',5);
INSERT INTO Booking VALUES (25,'BA178','2025-12-31',6);
INSERT INTO Booking VALUES (1,'AF023','2025-12-30',1);
INSERT INTO Booking VALUES (2,'AF023','2025-12-30',2);
INSERT INTO Booking VALUES (3,'AF023','2025-12-30',3);
INSERT INTO Booking VALUES (4,'AF023','2025-12-30',4);
INSERT INTO Booking VALUES (5,'SQ321','2025-12-30',1);
INSERT INTO Booking VALUES (6,'SQ321','2025-12-30',2);
INSERT INTO Booking VALUES (7,'SQ321','2025-12-30',3);
INSERT INTO Booking VALUES (10,'DL620','2025-12-30',1);
INSERT INTO Booking VALUES (11,'DL620','2025-12-30',2);
INSERT INTO Booking VALUES (12,'DL620','2025-12-30',3);
INSERT INTO Booking VALUES (13,'DL620','2025-12-30',4);
INSERT INTO Booking VALUES (20,'DL620','2025-12-31',1);
INSERT INTO Booking VALUES (21,'DL620','2025-12-31',2);
INSERT INTO Booking VALUES (22,'DL620','2025-12-31',3);
INSERT INTO Booking VALUES (23,'DL620','2025-12-31',4);
INSERT INTO Booking VALUES (24,'DL620','2025-12-31',5);
INSERT INTO Booking VALUES (8,'AA550','2025-12-31',1);
INSERT INTO Booking VALUES (9,'AA550','2025-12-31',2);
INSERT INTO Booking VALUES (10,'AA550','2025-12-31',3);
INSERT INTO Booking VALUES (11,'AA550','2025-12-31',4);
INSERT INTO Booking VALUES (12,'AA550','2025-12-31',5);
INSERT INTO Booking VALUES (13,'AA550','2025-12-31',6);
INSERT INTO Booking VALUES (14,'AA550','2025-12-31',7);
INSERT INTO Booking VALUES (22,'UA789','2025-12-31',1);
INSERT INTO Booking VALUES (23,'UA789','2025-12-31',2);
INSERT INTO Booking VALUES (24,'UA789','2025-12-31',3);
