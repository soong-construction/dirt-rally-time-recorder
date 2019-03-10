PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Tracks
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
