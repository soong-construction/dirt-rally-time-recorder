PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: cars
CREATE TABLE cars (id INTEGER PRIMARY KEY UNIQUE, name text, maxrpm real, startrpm real);

-- 1960s
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (1, 'Mini Cooper S', 733.038, 104.72);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (2, 'Lancia Fulvia HF', 783.304, 98.4366);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (103, 'Renault Alpine A110', 785.398193359375, 167.55160522460938);

-- 1970s
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (3, 'Opel Kadett GT/E 16v', 869.174, 125.664);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (4, 'Fiat 131 Abarth', 884.882, 150.796);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (5, 'Ford Escort Mk II', 942.478, 104.72);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (6, 'Lancia Stratos', 837.758, 188.496);

-- 1980s
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (7, 'BMW E30 Evo Rally', 942.478, 125.664);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (8, 'Ford Sierra Cosworth RS500', 785.398, 125.664);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (209, 'Renault 5 Turbo', 806.3421630859375, 130.89968872070312);

-- Group B (4WD)
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (9, 'MG Metro 6R4', 1099.56, 157.08);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (10, 'Audi Sport Quattro Rallye', 733.038, 115.192);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (11, 'Ford RS200 / Lancia 037 Evo 2', 890.118, 125.664);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (12, 'Peugeot 205 T16 Evo 2 ', 837.758, 209.439);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (13, 'Lancia Delta S4', 890.118, 104.72);

-- Group A
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (14, 'Delta HF Integrale', 785.398193359375, 183.25953674316406);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (15, 'Subaru Impreza 1995', 785.398, 125.664);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (316, 'Ford Escort RS Cosworth', 785.398193359375, 178.0236053466797);

INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (17, 'Seat Ibiza Kitcar', 942.478, 136.136);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (18, 'Peugeot 306 Maxi', 1151.92, 146.607);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (19, 'Mini Countryman Rally Edition', 785.398, 157.08);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (20, 'Ford Fiesta 2010', 785.398, 146.607);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (21, 'Opel Manta 400', 837.758, 146.607);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (1000, 'Peugeot 205 T16 Pikes Peak', 837.758, 209.439);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (1001, 'Peugeot 405 T16 Pikes Peak', 837.758, 157.08);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (1002, 'Audi Sport Quattro S1 PP', 863.938, 141.372);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
