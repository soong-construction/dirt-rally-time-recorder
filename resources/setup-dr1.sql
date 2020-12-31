-- Table: Tracks
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

CREATE TABLE Tracks (id INTEGER PRIMARY KEY UNIQUE, name text, length real, startz real);

-- Argolis, Greece
INSERT INTO Tracks (id, name, length, startz) VALUES (1, 'Ampelonas Ormi', 4860.1904, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (2, 'Kathodo Leontiou', 9665.9902, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (3, 'Pomono Ekrixi', 5086.8301, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (4, 'Koryfi Dafni', 4582.0098, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (5, 'Fourketa Kourva', 4515.4, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (6, 'Perasma Platani', 10688.0899, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (7, 'Tsiristra Theo', 10357.8799, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (8, 'Ourea Spevsi', 5739.0996, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (9, 'Ypsna tou Dasos', 5383.0098, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (10, 'Abies Koilada', 7089.4102, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (11, 'Pedines Epidaxi', 6595.3101, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (12, 'Anodou Farmakas', 9666.5, null);

-- Baumholder, Germany
INSERT INTO Tracks (id, name, length, startz) VALUES (21, 'Waldaufstieg', 5393.2197, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (22, 'Waldabstieg', 6015.0796, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (23, 'Kreuzungsring', 6318.71, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (24, 'Kreuzungsring reverse', 5685.2798, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (25, 'Ruschberg', 10699.96, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (26, 'Verbundsring', 5855.6802, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (27, 'Verbundsring reverse', 5550.8599, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (28, 'Flugzeugring', 4937.8501, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (29, 'Flugzeugring Reverse', 5129.04, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (30, 'Oberstein', 11684.1699, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (31, 'Hammerstein', 10805.2393, null);
INSERT INTO Tracks (id, name, length, startz) VALUES (32, 'Frauenberg', 11684.2207, null);

-- Monte Carlo, Monaco
INSERT INTO Tracks (id, name, length, startz) VALUES (41, 'Route de Turini', 10805.2207, 1289.7208);
INSERT INTO Tracks (id, name, length, startz) VALUES (42, 'Vallee descendante', 10866.8604, -2358.05);
INSERT INTO Tracks (id, name, length, startz) VALUES (43, 'Col de Turini – Sprint en descente', 4730.02, 298.587);
INSERT INTO Tracks (id, name, length, startz) VALUES (44, 'Col de Turini sprint en Montee', 4729.54, -209.405);
INSERT INTO Tracks (id, name, length, startz) VALUES (45, 'Col de Turini – Descente', 5175.9102, -120.206);
INSERT INTO Tracks (id, name, length, startz) VALUES (46, 'Gordolon – Courte montee', 5175.9102, -461.134);
INSERT INTO Tracks (id, name, length, startz) VALUES (47, 'Route de Turini (Descente)', 4015.3599, -1005.69);
INSERT INTO Tracks (id, name, length, startz) VALUES (48, 'Approche du Col de Turini – Montee', 3952.1501, 1289.7462);
INSERT INTO Tracks (id, name, length, startz) VALUES (49, 'Pra d´Alart', 9831.4502, -461.6663);
INSERT INTO Tracks (id, name, length, startz) VALUES (50, 'Col de Turini Depart', 9831.9707, 297.6757);
INSERT INTO Tracks (id, name, length, startz) VALUES (51, 'Route de Turini (Montee)', 6843.3203, -977.825);
INSERT INTO Tracks (id, name, length, startz) VALUES (52, 'Col de Turini – Depart en descente', 6846.8301, -2357.89);

-- Powys, Wales
INSERT INTO Tracks (id, name, length, startz) VALUES (61, 'Pant Mawr Reverse', 4821.6499, 2034.5620);
INSERT INTO Tracks (id, name, length, startz) VALUES (62, 'Bidno Moorland', 4993.2597, 1928.69);
INSERT INTO Tracks (id, name, length, startz) VALUES (63, 'Bidno Moorland Reverse', 5165.9501, 2470.99);
INSERT INTO Tracks (id, name, length, startz) VALUES (64, 'River Severn Valley', 11435.5107, -553.109);
INSERT INTO Tracks (id, name, length, startz) VALUES (65, 'Bronfelen', 11435.5508, 11435.6);
INSERT INTO Tracks (id, name, length, startz) VALUES (66, 'Fferm Wynt', 5717.3999, -553.112);
INSERT INTO Tracks (id, name, length, startz) VALUES (67, 'Fferm Wynt Reverse', 5717.3896, -21.5283);
INSERT INTO Tracks (id, name, length, startz) VALUES (68, 'Dyffryn Afon', 5718.0996, -26.0434);
INSERT INTO Tracks (id, name, length, startz) VALUES (69, 'Dyffryn Afon Reverse', 5718.1001, 156.4742);
INSERT INTO Tracks (id, name, length, startz) VALUES (70, 'Sweet Lamb', 9944.8701, 2216.3730);
INSERT INTO Tracks (id, name, length, startz) VALUES (71, 'Geufron Forest', 10063.5898, 2470.7358);
INSERT INTO Tracks (id, name, length, startz) VALUES (72, 'Pant Mawr', 4788.6699, 2216.2036);

-- Jämsä, Finland
INSERT INTO Tracks (id, name, length, startz) VALUES (81, 'Kailajärvi', 7509.3798828125, 30.892242431640625);
INSERT INTO Tracks (id, name, length, startz) VALUES (82, 'Paskuri', 7553.4599609375, 895.6185913085938);
INSERT INTO Tracks (id, name, length, startz) VALUES (83, 'Naarajärvi', 7427.68994140625, 831.8955078125);
INSERT INTO Tracks (id, name, length, startz) VALUES (84, 'Jyrkysjärvi', 7337.35986328125, -208.6328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (85, 'Kakaristo', 16205.1904296875, 3767.812744140625);
INSERT INTO Tracks (id, name, length, startz) VALUES (86, 'Pitkäjärvi', 16205.259765625, 819.3272705078125);
INSERT INTO Tracks (id, name, length, startz) VALUES (87, 'Iso Oksjärvi', 8042.5205078125, 3767.791015625);
INSERT INTO Tracks (id, name, length, startz) VALUES (88, 'Oksala', 8057.52978515625, -3283.9921875);
INSERT INTO Tracks (id, name, length, startz) VALUES (89, 'Kotajärvi', 8147.560546875, -3250.078125);
INSERT INTO Tracks (id, name, length, startz) VALUES (90, 'Järvenkylä', 8147.419921875, 819.4571533203125);
INSERT INTO Tracks (id, name, length, startz) VALUES (91, 'Kontinjärvi', 15041.48046875, 30.879966735839844);
INSERT INTO Tracks (id, name, length, startz) VALUES (92, 'Hämelahti', 14954.6796875, -208.6311798095703);

-- Värmland, Sweden
INSERT INTO Tracks (id, name, length, startz) VALUES (101, 'Älgsjön', 7054.830078125, -1633.27197265625);
INSERT INTO Tracks (id, name, length, startz) VALUES (102, 'Östra Hinnsjön', 4911.22998046875, -1730.606689453125);
INSERT INTO Tracks (id, name, length, startz) VALUES (103, 'Stor-jangen Sprint', 6666.27978515625, -2144.06689453125);
INSERT INTO Tracks (id, name, length, startz) VALUES (104, 'Stor-jangen Sprint Reverse', 6692.23974609375, 552.0279541015625);
INSERT INTO Tracks (id, name, length, startz) VALUES (105, 'Björklangen', 4932.33984375, -5107.74365234375);
INSERT INTO Tracks (id, name, length, startz) VALUES (106, 'Ransbysäter', 11920.2802734375, -4330.77490234375);
INSERT INTO Tracks (id, name, length, startz) VALUES (107, 'Hamra', 12122.2001953125, 2713.06494140625);
INSERT INTO Tracks (id, name, length, startz) VALUES (108, 'Lysvik', 12122.009765625, -5107.564453125);
INSERT INTO Tracks (id, name, length, startz) VALUES (109, 'Norraskoga', 11500.720703125, 552.0166625976562);
INSERT INTO Tracks (id, name, length, startz) VALUES (110, 'Älgsjön Sprint', 5247.4599609375, -4330.759765625);
INSERT INTO Tracks (id, name, length, startz) VALUES (111, 'Elgsjön', 7057.25, 2713.06494140625);
INSERT INTO Tracks (id, name, length, startz) VALUES (112, 'Skogsrallyt', 4802.4599609375, -2143.044677734375);

-- Pikes Peak, USA
INSERT INTO Tracks (id, name, length, startz) VALUES (1001, 'Pikes Peak - Full Course', 19476.4688, -4701.25);
INSERT INTO Tracks (id, name, length, startz) VALUES (1002, 'Pikes Peak - Sector 1', 6327.6899, -4700.96);
INSERT INTO Tracks (id, name, length, startz) VALUES (1003, 'Pikes Peak - Sector 2', 6456.3604, -1122.07);
INSERT INTO Tracks (id, name, length, startz) VALUES (1004, 'Pikes Peak - Sector 3', 7077.2002, 1397.84);
INSERT INTO Tracks (id, name, length, startz) VALUES (1009, 'Pikes Peak (Mixed Surface) - Full Course', 19476.5, -4701.11);
INSERT INTO Tracks (id, name, length, startz) VALUES (1010, 'Pikes Peak (Mixed Surface) - Sector 1', 6327.7002, -4700.94);
INSERT INTO Tracks (id, name, length, startz) VALUES (1011, 'Pikes Peak (Mixed Surface) - Sector 2', 6456.3702, -1122.23);
INSERT INTO Tracks (id, name, length, startz) VALUES (1012, 'Pikes Peak (Mixed Surface) - Sector 3', 7077.21, 1397.82);
INSERT INTO Tracks (id, name, length, startz) VALUES (1013, 'Pikes Peak (Gravel) - Full Course', 19476.5, -4701.11);
INSERT INTO Tracks (id, name, length, startz) VALUES (1014, 'Pikes Peak (Gravel) - Sector 1', 6327.7002, -4700.94);
INSERT INTO Tracks (id, name, length, startz) VALUES (1015, 'Pikes Peak (Gravel) - Sector 2', 6456.3702, -1122.23);
INSERT INTO Tracks (id, name, length, startz) VALUES (1016, 'Pikes Peak (Gravel) - Sector 3', 7077.21, 1397.82);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

-- Table: Cars
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

CREATE TABLE cars (id INTEGER PRIMARY KEY UNIQUE, name text, maxrpm real, idlerpm real);

-- 1960s
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1, 'Mini Cooper S', 733.038, 104.72);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (2, 'Lancia Fulvia HF', 783.304, 98.4366);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (103, 'Renault Alpine A110', 785.398193359375, 167.55160522460938);

-- 1970s
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (3, 'Opel Kadett GT/E 16v', 869.174, 125.664);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (4, 'Fiat 131 Abarth', 884.882, 150.796);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (5, 'Ford Escort Mk II', 942.478, 104.72);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (6, 'Lancia Stratos', 837.758056640625, 167.55160522460938);

-- 1980s
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (7, 'BMW E30 Evo Rally', 942.478, 125.664);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (8, 'Ford Sierra Cosworth RS500', 785.398193359375, 172.7875213623047);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (209, 'Renault 5 Turbo', 806.3421630859375, 130.89968872070312);

-- Group B (4WD)
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (9, 'MG Metro 6R4', 1099.56, 157.08);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (10, 'Audi Sport Quattro Rallye', 733.038, 115.192);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (11, 'Ford RS200', 890.118, 125.664);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (12, 'Peugeot 205 T16 Evo 2', 837.758, 209.439);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (13, 'Lancia Delta S4', 890.118, 104.72);

-- Group A
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (14, 'Delta HF Integrale', 785.398193359375, 183.25953674316406);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (15, 'Subaru Impreza 1995', 785.398193359375, 204.2035369873047);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (316, 'Ford Escort RS Cosworth', 785.398193359375, 178.0236053466797);

-- F2 Kit Car
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (17, 'Seat Ibiza Kitcar', 942.478, 136.136);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (18, 'Peugeot 306 Maxi', 1151.92, 146.607);

-- R4
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (501, 'Subaru Impreza WRX STI 2011', 774.9262084960938, 167.55160522460938);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (502, 'Mitsubishi Lancer Evolution X', 785.398193359375, 178.0236053466797);

-- 2000s
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (40, 'Subaru Impreza 2001', 785.398193359375, 157.07962036132812);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (601, 'Ford Focus RS Rally 2001', 785.398193359375, 178.0236053466797);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (602, 'Ford Focus RS Rally 2007', 733.038330078125, 209.43943786621094);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (603, 'Citroen C4 Rally 2010', 733.038330078125, 209.43943786621094);

-- 2010s
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (19, 'Mini Countryman Rally Edition', 785.398193359375, 167.55160522460938);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (20, 'Ford Fiesta 2010', 785.398, 146.607);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (821, 'Hyundai Rally', 733.038330078125, 209.43943786621094);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (822, 'Volkswagen Polo Rally', 733.038, 198.968);

-- Group B (RWD)
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (21, 'Opel Manta 400', 837.758, 146.607);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (902, 'Lancia 037 Evo 2', 890.118, 125.664);

-- Hillclimb
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1000, 'Peugeot 205 T16 Pikes Peak', 837.758, 209.439);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1001, 'Peugeot 405 T16 Pikes Peak', 837.758, 157.08);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1002, 'Audi Sport Quattro S1 PP', 863.938, 141.372);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1003, 'Peugeot 208 T16 Pikes Peak', 816.81396484375, 188.49559020996094);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

-- Table: Controls
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

CREATE TABLE controls(id INTEGER PRIMARY KEY UNIQUE, handbrake integer, shifting text, manualclutch integer, topgear integer);

-- 1960s
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1, 1, 'H-PATTERN', 1, 4);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (2, 1, 'H-PATTERN', 1, 4);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (103, 1, 'H-PATTERN', 1, 5);

-- 1970s
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (3, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (4, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (5, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (6, 1, 'H-PATTERN', 1, 5);

-- 1980s
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (7, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (8, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (209, 1, 'H-PATTERN', 1, 5);

-- Group B (4WD)
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (9, 0, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (10, 0, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (11, 0, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (12, 0, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (13, 0, 'H-PATTERN', 1, 5);

-- Group A
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (14, 1, 'H-PATTERN', 1, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (15, 1, 'H-PATTERN', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (316, 1, 'H-PATTERN', 0, 7);

-- F2 Kit Car
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (17, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (18, 1, 'SEQUENTIAL', 0, 6);

-- R4
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (501, 1, 'H-PATTERN', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (502, 1, 'H-PATTERN', 0, 5);

-- 2000s
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (40, 1, 'PADDLE', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (601, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (602, 1, 'PADDLE', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (603, 1, 'PADDLE', 0, 6);

-- 2010s
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (19, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (20, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (821, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (822, 1, 'PADDLE', 0, 6);

-- Group B (RWD)
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (21, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (902, 1, 'H-PATTERN', 1, 5);

-- Hillclimb
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1000, 0, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1001, 0, 'H-PATTERN', 1, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1002, 0, 'H-PATTERN', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1003, 0, '2 PADDLES', 0, 6);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
