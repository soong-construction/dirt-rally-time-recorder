-- PRELIMINARY, USE WITH CARE. Please check migrate.sql each time you update this tool

-- Table: Tracks
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

CREATE TABLE Tracks (id INTEGER PRIMARY KEY UNIQUE, name text, length real, startz real);

-- Hawkes Bay, New Zealand:100
INSERT INTO Tracks (id, name, length, startz) VALUES (100, 'Te Awanga Forward', 11507.4404296875, -4415.01025390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (101, 'Waimarama Point Forward', 16057.8505859375, 2892.6748046875);
INSERT INTO Tracks (id, name, length, startz) VALUES (102, 'Ocean Beach', 11437.0703125, 1788.5035400390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (103, 'Waimarama Point Reverse', 15844.529296875, 2074.9248046875);
INSERT INTO Tracks (id, name, length, startz) VALUES (104, 'Elsthorpe Sprint Forward', 7137.81005859375, 2893.062744140625);
INSERT INTO Tracks (id, name, length, startz) VALUES (105, 'Te Awanga Sprint Forward', 4799.84033203125, -4415.01025390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (106, 'Ocean Beach Sprint Forward', 6624.0302734375, 1788.5035400390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (107, 'Waimarama Sprint Forward', 8807.490234375, 2074.85498046875);
INSERT INTO Tracks (id, name, length, startz) VALUES (108, 'Waimarama Sprint Reverse', 8733.98046875, 5268.06494140625);
INSERT INTO Tracks (id, name, length, startz) VALUES (109, 'Ocean Beach Sprint Reverse', 6584.10009765625, -1950.1280517578125);
INSERT INTO Tracks (id, name, length, startz) VALUES (110, 'Te Awanga Sprint Reverse', 4688.52978515625, -2004.3233642578125);
INSERT INTO Tracks (id, name, length, startz) VALUES (111, 'Elsthorpe Sprint Reverse', 6643.490234375, 5161.2197265625);

-- Powys, Wales:300 
INSERT INTO Tracks (id, name, length, startz) VALUES (300, 'Bidno Moorland Reverse', 5165.96044921875, 2481.20458984375);
INSERT INTO Tracks (id, name, length, startz) VALUES (301, 'River Severn Valley', 11435.5107421875, -551.7058715820312);
INSERT INTO Tracks (id, name, length, startz) VALUES (302, 'Dyffryn Afon', 5718.0996, -26.0434);
INSERT INTO Tracks (id, name, length, startz) VALUES (303, 'Sweet Lamb', 9911.66015625, 2220.907958984375);
INSERT INTO Tracks (id, name, length, startz) VALUES (304, 'Geufron Forest', 10063.6005859375, 2481.204345703125);
INSERT INTO Tracks (id, name, length, startz) VALUES (305, 'Pant Mawr', 4788.669921875, 2220.905029296875);

--TODO Record for all DR1 tracks
--INSERT INTO Tracks (id, name, length, startz) VALUES (ID, 'Pant Mawr Reverse', 4821.6499, 2034.5620);
--INSERT INTO Tracks (id, name, length, startz) VALUES (ID, 'Bidno Moorland', 4993.2597, 1928.69);
--INSERT INTO Tracks (id, name, length, startz) VALUES (ID, 'Bronfelen', 11435.5508, 11435.6);
--INSERT INTO Tracks (id, name, length, startz) VALUES (ID, 'Fferm Wynt', 5717.3999, -553.112);
--INSERT INTO Tracks (id, name, length, startz) VALUES (ID, 'Fferm Wynt Reverse', 5717.3896, -21.5283);
--INSERT INTO Tracks (id, name, length, startz) VALUES (ID, 'Dyffryn Afon Reverse', 5718.1001, 156.4742);

-- Leczna County, Poland:400
INSERT INTO Tracks (id, name, length, startz) VALUES (400, 'Borysik', 9194.3203125, 7393.10205078125);
INSERT INTO Tracks (id, name, length, startz) VALUES (401, 'Zarobka', 16475.009765625, 4674.81787109375);
INSERT INTO Tracks (id, name, length, startz) VALUES (402, 'Zagorze', 16615.0, 1972.2744140625);
INSERT INTO Tracks (id, name, length, startz) VALUES (403, 'Kopina', 7840.1796875, 4674.8505859375);
INSERT INTO Tracks (id, name, length, startz) VALUES (404, 'Marynka', 9254.900390625, 1972.655029296875);
INSERT INTO Tracks (id, name, length, startz) VALUES (405, 'Czarny Las', 6622.080078125, 4644.47900390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (406, 'Lejno', 6698.81005859375, -3314.945556640625);
INSERT INTO Tracks (id, name, length, startz) VALUES (407, 'Józefin', 8159.81982421875, 7583.14111328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (408, 'Jagodno', 6655.5400390625, -402.5574951171875);
INSERT INTO Tracks (id, name, length, startz) VALUES (409, 'Zienki', 13180.3798828125, -3314.868408203125);
INSERT INTO Tracks (id, name, length, startz) VALUES (410, 'Jezioro Rotcze', 13295.6796875, 4644.48193359375);

-- Ribadelles, Spain:500
INSERT INTO Tracks (id, name, length, startz) VALUES (500, 'Comienzo de Bellriu', 14348.3603515625, 190.2432861328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (501, 'Descenso por carretera', 4562.80029296875, -2326.102783203125);
INSERT INTO Tracks (id, name, length, startz) VALUES (502, 'Vinedos Dardenya Inversa', 6194.7099609375, -2979.6708984375);
INSERT INTO Tracks (id, name, length, startz) VALUES (503, 'Vinedos Dardenya', 6547.39990234375, -2001.9224853515625);
INSERT INTO Tracks (id, name, length, startz) VALUES (504, 'Vinedos dentro del valle Parra', 6815.4501953125, -2404.659423828125);
INSERT INTO Tracks (id, name, length, startz) VALUES (505, 'Camino a Centenera', 10584.6796875, -2001.93310546875);
INSERT INTO Tracks (id, name, length, startz) VALUES (506, 'Ascenso bosque Montverd', 7297.27001953125, 2593.37646484375);
INSERT INTO Tracks (id, name, length, startz) VALUES (507, 'Final de Bellriu', 13164.330078125, -2404.716552734375);
INSERT INTO Tracks (id, name, length, startz) VALUES (508, 'Subida por carretera', 4380.740234375, -3003.61083984375);
INSERT INTO Tracks (id, name, length, startz) VALUES (509, 'Salida desde Montverd', 6143.5703125, 2607.35400390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (510, 'Ascenso por valle el Gualet', 7005.68994140625, 190.19236755371094);
INSERT INTO Tracks (id, name, length, startz) VALUES (511, 'Centenera', 10568.4296875, -2326.286865234375);

-- Monaro, Australia:600
INSERT INTO Tracks (id, name, length, startz) VALUES (600, 'Mountain Kaye Pass', 13301.109375, -2352.93017578125);
INSERT INTO Tracks (id, name, length, startz) VALUES (601, 'Yambulla Mountain Descent', 6221.490234375, -2353.200439453125);
INSERT INTO Tracks (id, name, length, startz) VALUES (602, 'Mountain Kaye Pass Reverse', 13301.109375, -2353.1884765625);

-- Baumholder, Germany:700
INSERT INTO Tracks (id, name, length, startz) VALUES (700, 'Frauenberg', 11551.16015625, 539.3903198242188);
INSERT INTO Tracks (id, name, length, startz) VALUES (701, 'Innerer Feld-Sprint (umgekehrt)', 4937.85009765625, 656.4170532226562);
INSERT INTO Tracks (id, name, length, startz) VALUES (702, 'Kreuzungsring', 6121.8701171875, -718.7255249023438);
INSERT INTO Tracks (id, name, length, startz) VALUES (703, 'Verbundsring Reverse', 5550.85009765625, 657.0391235351562);
INSERT INTO Tracks (id, name, length, startz) VALUES (704, 'Verbundsring', 5855.6796875, 513.0369873046875);
INSERT INTO Tracks (id, name, length, startz) VALUES (705, 'Hammerstein', 10805.23046875, 513.0381469726562);
INSERT INTO Tracks (id, name, length, startz) VALUES (706, 'Innerer Feld-Sprint', 5129.0400390625, 814.1966552734375);
INSERT INTO Tracks (id, name, length, startz) VALUES (707, 'Ruschberg', 10699.9599609375, 813.9644165039062);
INSERT INTO Tracks (id, name, length, startz) VALUES (708, 'Waldabstieg', 5882.1796875, -948.1590576171875);

-- Catamarca, Argentina:800
INSERT INTO Tracks (id, name, length, startz) VALUES (800, 'San Isidro', 4171.5, -3227.052001953125); -- TODO Check if Z value is correct
INSERT INTO Tracks (id, name, length, startz) VALUES (801, 'Valle de los puentes', 7667.31982421875, 131.24305725097656);
INSERT INTO Tracks (id, name, length, startz) VALUES (802, 'Las Juntas', 8256.8603515625, 2581.4658203125);
INSERT INTO Tracks (id, name, length, startz) VALUES (803, 'Camino de acantilados y rocas', 5303.7900390625, 2581.419189453125);
INSERT INTO Tracks (id, name, length, startz) VALUES (804, 'Camino de acantilados y rocas inverso', 5294.81982421875, 1379.3668212890625);
INSERT INTO Tracks (id, name, length, startz) VALUES (805, 'Camino a Coneta', 4082.2998046875, -1864.53857421875);
INSERT INTO Tracks (id, name, length, startz) VALUES (806, 'El Rodeo', 2845.6298828125, 205.79042053222656);
INSERT INTO Tracks (id, name, length, startz) VALUES (807, 'La Merced', 2779.489990234375, 1344.740478515625);

-- New England, USA:900
INSERT INTO Tracks (id, name, length, startz) VALUES (900, 'Tolt Valley Sprint Forward', 6575.8701171875, -408.7677917480469);
INSERT INTO Tracks (id, name, length, startz) VALUES (901, 'Beaver Creek Trail Forward', 12856.66015625, 519.74462890625);
INSERT INTO Tracks (id, name, length, startz) VALUES (902, 'Fuller Mountain Ascent', 6468.2998046875, 2768.20947265625);
INSERT INTO Tracks (id, name, length, startz) VALUES (903, 'Hancock Creek Burst', 6701.61962890625, 1521.3895263671875);
INSERT INTO Tracks (id, name, length, startz) VALUES (904, 'Hancock Hill Sprint Reverse', 6109.5400390625, -353.2311096191406);
INSERT INTO Tracks (id, name, length, startz) VALUES (905, 'North Fork Pass', 12228.830078125, 1521.4326171875);
INSERT INTO Tracks (id, name, length, startz) VALUES (906, 'Beaver Creek Trail Reverse', 12765.919921875, -4618.1796875);
INSERT INTO Tracks (id, name, length, startz) VALUES (907, 'Tolt Valley Sprint Reverse', 6604.0302734375, -4618.16796875);
INSERT INTO Tracks (id, name, length, startz) VALUES (908, 'Hancock Hill Sprint Forward', 6229.10986328125, 519.571533203125);

-- Monte Carlo, Monaco:1000
INSERT INTO Tracks (id, name, length, startz) VALUES (1000, 'Pra d´Alart', 9831.4501953125, -467.3258361816406);
INSERT INTO Tracks (id, name, length, startz) VALUES (1001, 'Vallee descendante', 10866.8603515625, -2362.048095703125);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

-- Table: Cars
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

CREATE TABLE cars (id INTEGER PRIMARY KEY UNIQUE, name text, maxrpm real, startrpm real);

-- H1 FWD class
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (100, 'Mini Cooper S', 733.0382690429688, 83.77580261230469);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (101, 'DS Automobiles DS 21', 628.3185424804688, 104.71975708007812);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (102, 'Lancia Fulvia HF', 680.678466796875, 99.48377227783203);

-- H2 FWD class
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (200, 'Volkswagen Golf GTI 16V', 785.398193359375, 442.6036682128906);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (201, 'Peugeot 205 GTI', 733.0382690429688, 125.66371154785156);

-- H2 RWD class
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (300, 'Ford Escort MK II', 994.8377075195312, 125.66371154785156);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (301, 'Alpine Renault A110 1600 S', 837.758056640625, 167.55160522460938);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (302, 'Fiat 131 Abarth Rally', 837.758056640625, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (303, 'Opel Kadett C GT/E', 942.477783203125, 157.0796356201172);

-- H3 RWD class
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (400, 'BMW E30 M3 Evo Rally', 932.005859375, 115.19173431396484);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (401, 'Opel Ascona 400', 785.398193359375, 136.13568115234375);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (402, 'Lancia Stratos', 890.1179809570312, 104.71975708007812);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (403, 'Renault 5 Turbo', 837.758056640625, 151.84414672851562);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (404, 'Datsun 240Z', 779.7432861328125, 80.42477416992188);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (405, 'Ford Sierra Cosworth RS500', 785.398193359375, 115.19197845458984);

-- Group B RWD
-- Group B 4WD
-- R2

-- Group A
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (800, 'Mitsubishi Lancer Evolution VI', 733.0382690429688, 144.932861328125);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (801, 'Subaru Impreza 1995', 733.0382690429688, 115.19197845458984);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (802, 'Lancia Delta HF Integrale', 785.398193359375, 104.71987915039062);
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (803, 'Ford Escort RS Cosworth', 733.0382690429688, 145.17236328125);

-- NR4/R4
-- 4WD/2000cc
-- R5

-- Rally GT 
INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (1200, 'Porsche 911 RGT Rally Spec', 942.477783203125, 188.4955596923828);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

-- Table: Controls
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

CREATE TABLE controls(id INTEGER PRIMARY KEY UNIQUE, handbrake integer, shifting text, manualclutch integer, forwardgears integer);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
