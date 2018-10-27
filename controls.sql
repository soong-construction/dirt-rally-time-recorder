PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: cars
CREATE TABLE controls(id INTEGER PRIMARY KEY UNIQUE, handbrake integer);

-- TODO #6 Clarify for older cars: http://forums.codemasters.com/discussion/7071/dirt-rally-handbrake-and-transmission-information
-- 1960s
-- INSERT INTO controls(id, handbrake) VALUES (2, 'Lancia Fulvia HF', 783.304, 98.4366);
-- INSERT INTO controls(id, handbrake) VALUES (103, 'Renault Alpine A110', 785.398193359375, 167.55160522460938);
-- INSERT INTO controls(id, handbrake) VALUES (1, 'Mini Cooper S', 733.038, 104.72);

-- 1970s
INSERT INTO controls(id, handbrake) VALUES (3, 1);
INSERT INTO controls(id, handbrake) VALUES (4, 1);
INSERT INTO controls(id, handbrake) VALUES (5, 1);
INSERT INTO controls(id, handbrake) VALUES (6, 1);

-- 1980s
INSERT INTO controls(id, handbrake) VALUES (7, 1);
INSERT INTO controls(id, handbrake) VALUES (8, 1);
INSERT INTO controls(id, handbrake) VALUES (209, 1);

-- Group B (4WD)
INSERT INTO controls(id, handbrake) VALUES (9, 0);
INSERT INTO controls(id, handbrake) VALUES (10, 0);
INSERT INTO controls(id, handbrake) VALUES (11, 0);
INSERT INTO controls(id, handbrake) VALUES (12, 0);
INSERT INTO controls(id, handbrake) VALUES (13, 0);

-- Group A
INSERT INTO controls(id, handbrake) VALUES (14, 1);
INSERT INTO controls(id, handbrake) VALUES (15, 1);
INSERT INTO controls(id, handbrake) VALUES (316, 1);

-- F2 Kit Car
INSERT INTO controls(id, handbrake) VALUES (17, 1);
INSERT INTO controls(id, handbrake) VALUES (18, 1);

-- R4
INSERT INTO controls(id, handbrake) VALUES (501, 1);
INSERT INTO controls(id, handbrake) VALUES (502, 1);

-- 2000s
INSERT INTO controls(id, handbrake) VALUES (40, 1);
INSERT INTO controls(id, handbrake) VALUES (601, 1);
INSERT INTO controls(id, handbrake) VALUES (602, 1);
INSERT INTO controls(id, handbrake) VALUES (603, 1);

-- 2010s
INSERT INTO controls(id, handbrake) VALUES (19, 1);
INSERT INTO controls(id, handbrake) VALUES (20, 1);
INSERT INTO controls(id, handbrake) VALUES (821, 1);
INSERT INTO controls(id, handbrake) VALUES (822, 1);

-- Group B (RWD)
INSERT INTO controls(id, handbrake) VALUES (21, 1);
INSERT INTO controls(id, handbrake) VALUES (902, 1);

-- Hillclimb
INSERT INTO controls(id, handbrake) VALUES (1000, 0);
INSERT INTO controls(id, handbrake) VALUES (1001, 0);
INSERT INTO controls(id, handbrake) VALUES (1002, 0);
INSERT INTO controls(id, handbrake) VALUES (1003, 0);



COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
