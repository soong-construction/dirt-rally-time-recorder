PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Tracks
CREATE TABLE Tracks (id INTEGER PRIMARY KEY UNIQUE, name text, length real, startz real);

-- Argolis, Greece
INSERT INTO Tracks (id, name, length, startz) VALUES (1, 'Ampelonas Ormi', 4860.1904, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (2, 'Kathodo Leontiou', 9665.9902, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (3, 'Pomono Ekrixi', 5086.8301, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (4, 'Koryfi Dafni', 4582.0098, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (5, 'Fourketa Kourva', 4515.4, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (6, 'Perasma Platani', 10688.0899, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (7, 'Tsiristra Theo', 10357.8799, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (8, 'Ourea Spevsi', 5739.0996, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (9, 'Ypsna tou Dasos', 5383.0098, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (10, 'Abies Koilada', 7089.4102, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (11, 'Pedines Epidaxi', 6595.3101, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (12, 'Anodou Farmakas', 9666.5, '');

-- Baumholder, Germany
INSERT INTO Tracks (id, name, length, startz) VALUES (21, 'Waldaufstieg', 5393.2197, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (22, 'Waldabstieg', 6015.0796, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (23, 'Kreuzungsring', 6318.71, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (24, 'Kreuzungsring reverse', 5685.2798, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (25, 'Ruschberg', 10699.96, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (26, 'Verbundsring', 5855.6802, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (27, 'Verbundsring reverse', 5550.8599, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (28, 'Flugzeugring', 4937.8501, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (29, 'Flugzeugring Reverse', 5129.04, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (30, 'Oberstein', 11684.1699, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (31, 'Hammerstein', 10805.2393, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (32, 'Frauenberg', 11684.2207, '');

-- Monte Carlo, Monaco
-- TODO Z mismatch: Failed to identify track: 10805.220703125 (Z: 1275.6722412109375)
INSERT INTO Tracks (id, name, length, startz) VALUES (41, 'Route de Turini', 10805.2207, 1290.45);
INSERT INTO Tracks (id, name, length, startz) VALUES (42, 'Vallee descendante', 10866.8604, -2358.05);
INSERT INTO Tracks (id, name, length, startz) VALUES (43, 'Col de Turini – Sprint en descente', 4730.02, 298.587);
INSERT INTO Tracks (id, name, length, startz) VALUES (44, 'Col de Turini sprint en Montee', 4729.54, -209.405);
INSERT INTO Tracks (id, name, length, startz) VALUES (45, 'Col de Turini – Descente', 5175.9102, -120.206);
INSERT INTO Tracks (id, name, length, startz) VALUES (46, 'Gordolon – Courte montee', 5175.9102, -461.134);
INSERT INTO Tracks (id, name, length, startz) VALUES (47, 'Route de Turini (Descente)', 4015.3599, -1005.69);
INSERT INTO Tracks (id, name, length, startz) VALUES (48, 'Approche du Col de Turini – Montee', 3952.1501, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (49, 'Pra dAlart', 9831.4502, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (50, 'Col de Turini Depart', 9831.9707, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (51, 'Route de Turini (Montee)', 6843.3203, -977.825);
INSERT INTO Tracks (id, name, length, startz) VALUES (52, 'Col de Turini – Depart en descente', 6846.8301, -2357.89);

-- Powys, Wales
INSERT INTO Tracks (id, name, length, startz) VALUES (61, 'Pant Mawr Reverse', 4821.6499, NULL);
INSERT INTO Tracks (id, name, length, startz) VALUES (62, 'Bidno Moorland', 4993.2597, 1928.69);
INSERT INTO Tracks (id, name, length, startz) VALUES (63, 'Bidno Moorland Reverse', 5165.9501, 2470.99);
INSERT INTO Tracks (id, name, length, startz) VALUES (64, 'River Severn Valley', 11435.5107, -553.109);
INSERT INTO Tracks (id, name, length, startz) VALUES (65, 'Bronfelen', 11435.5508, 11435.6);
INSERT INTO Tracks (id, name, length, startz) VALUES (66, 'Fferm Wynt', 5717.3999, -553.112);
INSERT INTO Tracks (id, name, length, startz) VALUES (67, 'Fferm Wynt Reverse', 5717.3896, -21.5283);
INSERT INTO Tracks (id, name, length, startz) VALUES (68, 'Dyffryn Afon', 5718.0996, -26.0434);
INSERT INTO Tracks (id, name, length, startz) VALUES (69, 'Dyffryn Afon Reverse', 5718.1001, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (70, 'Sweet Lamb', 9944.8701, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (71, 'Geufron Forest', 10063.5898, '');
INSERT INTO Tracks (id, name, length, startz) VALUES (72, 'Pant Mawr', 4788.6699, NULL);

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

-- Pikes Peak, USA
INSERT INTO Tracks (id, name, length, startz) VALUES (1001, 'Pikes Peak - Full Course', 19476.4688, -4701.25);
INSERT INTO Tracks (id, name, length, startz) VALUES (1002, 'Pikes Peak - Sector 1', 6327.6899, -4700.96);
INSERT INTO Tracks (id, name, length, startz) VALUES (1003, 'Pikes Peak - Sector 2', 6456.3604, -1122.07);
INSERT INTO Tracks (id, name, length, startz) VALUES (1004, 'Pikes Peak - Sector 3', 7077.2002, 1397.84);
INSERT INTO Tracks (id, name, length, startz) VALUES (1005, 'Pikes Peak (Mixed Surface) - Full Course', 19476.5, -4701.11);
INSERT INTO Tracks (id, name, length, startz) VALUES (1006, 'Pikes Peak (Mixed Surface) - Sector 1', 6327.7002, -4700.94);
INSERT INTO Tracks (id, name, length, startz) VALUES (1007, 'Pikes Peak (Mixed Surface) - Sector 2', 6456.3702, -1122.23);
INSERT INTO Tracks (id, name, length, startz) VALUES (1008, 'Pikes Peak (Mixed Surface) - Sector 3', 7077.21, 1397.82);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
