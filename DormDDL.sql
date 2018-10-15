CREATE TABLE dorm (
dorm_id INT NOT NULL,
dorm_name VARCHAR(100) NOT NULL, year_built DATE NOT NULL,
PRIMARY KEY (dorm_id)
);
CREATE TABLE room (
room_id INT NOT NULL,
sqaure_footage FLOAT NOT NULL,
floor INT NOT NULL,
dorm_id INT NOT NULL,
PRIMARY KEY (room_id),
FOREIGN KEY (dorm_id) REFERENCES dorm(dorm_id) ON DELETE CASCADE
);
CREATE TABLE resident (
resident_id INT NOT NULL,
resident_name VARCHAR(50) NOT NULL,
room_id INT NOT NULL,
PRIMARY KEY (resident_id),
FOREIGN KEY (room_id) REFERENCES room(room_id)
);
CREATE TABLE resides (
resident_id INT NOT NULL, room_id INT NOT NULL, date_beginning DATE NOT NULL, date_end DATE NOT NULL,
cost DECIMAL(7,2) NOT NULL,
PRIMARY KEY (room_id, resident_id),
FOREIGN KEY (room_id) REFERENCES room(room_id) ON DELETE CASCADE, FOREIGN KEY (resident_id) REFERENCES resident(resident_id) ON DELETE CASCADE
);