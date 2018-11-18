PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: cars
CREATE TABLE controls(id INTEGER PRIMARY KEY UNIQUE, handbrake integer, shifting text, forwardgears integer);

-- TODO #6 Clarify for older cars: http://forums.codemasters.com/discussion/7071/dirt-rally-handbrake-and-transmission-information
-- 1960s
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (1, 1, 'H-PATTERN', 4);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (2, 1, 'H-PATTERN', 4);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (103, 1, 'H-PATTERN', 5);

-- 1970s
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (3, 1, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (4, 1, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (5, 1, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (6, 1, 'H-PATTERN', 5);

-- 1980s
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (7, 1, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (8, 1, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (209, 1, 'H-PATTERN', 5);

-- Group B (4WD)
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (9, 0, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (10, 0, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (11, 0, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (12, 0, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (13, 0, 'H-PATTERN', 5);

-- Group A
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (14, 1, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (15, 1, 'H-PATTERN', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (316, 1, 'H-PATTERN', 7);

-- F2 Kit Car
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (17, 1, 'SEQUENTIAL', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (18, 1, 'SEQUENTIAL', 6);

-- R4
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (501, 1, 'H-PATTERN', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (502, 1, 'H-PATTERN', 5);

-- 2000s
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (40, 1, 'PADDLE', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (601, 1, 'SEQUENTIAL', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (602, 1, 'PADDLE', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (603, 1, 'PADDLE', 6);

-- 2010s
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (19, 1, 'SEQUENTIAL', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (20, 1, 'SEQUENTIAL', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (821, 1, 'SEQUENTIAL', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (822, 1, 'PADDLE', 6);

-- Group B (RWD)
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (21, 1, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (902, 1, 'H-PATTERN', 5);

-- Hillclimb
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (1000, 0, 'H-PATTERN', 5);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (1001, 0, 'H-PATTERN', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (1002, 0, 'H-PATTERN', 6);
INSERT INTO controls(id, handbrake, shifting, forwardgears) VALUES (1003, 0, '2 PADDLES', 6);



COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
