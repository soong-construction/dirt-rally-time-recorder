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

-- Värmland, Sweden:200
INSERT INTO Tracks (id, name, length, startz) VALUES (200, 'Älgsjön', 7055.9501953125, -1618.4476318359375);
INSERT INTO Tracks (id, name, length, startz) VALUES (201, 'Östra Hinnsjön', 4911.68017578125, -1742.0498046875);
INSERT INTO Tracks (id, name, length, startz) VALUES (202, 'Stor-jangen Sprint', 6666.89013671875, -2143.403076171875);
INSERT INTO Tracks (id, name, length, startz) VALUES (203, 'Stor-jangen Sprint Reverse', 6693.43994140625, 563.3468017578125);
INSERT INTO Tracks (id, name, length, startz) VALUES (204, 'Björklangen', 4931.990234375, -5101.59619140625);
INSERT INTO Tracks (id, name, length, startz) VALUES (205, 'Ransbysäter', 11922.6201171875, -4328.87158203125);
INSERT INTO Tracks (id, name, length, startz) VALUES (206, 'Hamra', 12123.740234375, 2697.36279296875);
INSERT INTO Tracks (id, name, length, startz) VALUES (207, 'Lysvik', 12123.5908203125, -5101.78369140625);
INSERT INTO Tracks (id, name, length, startz) VALUES (208, 'Norraskoga', 11503.490234375, 562.8009033203125);
INSERT INTO Tracks (id, name, length, startz) VALUES (209, 'Älgsjön Sprint', 5248.35986328125, -4328.87158203125);
INSERT INTO Tracks (id, name, length, startz) VALUES (210, 'Elgsjön', 7058.47998046875, 2696.98291015625);
INSERT INTO Tracks (id, name, length, startz) VALUES (211, 'Skogsrallyt', 4804.0302734375, -2143.44384765625);

-- Powys, Wales:300 
INSERT INTO Tracks (id, name, length, startz) VALUES (300, 'Pant Mawr Reverse', 4821.64990234375, 2047.56201171875);
INSERT INTO Tracks (id, name, length, startz) VALUES (301, 'Bidno Moorland', 4960.06005859375, 1924.06884765625);
INSERT INTO Tracks (id, name, length, startz) VALUES (302, 'Bidno Moorland Reverse', 5165.96044921875, 2481.105224609375);
INSERT INTO Tracks (id, name, length, startz) VALUES (303, 'River Severn Valley', 11435.5107421875, -557.0780029296875);
INSERT INTO Tracks (id, name, length, startz) VALUES (304, 'Bronfelen', 11435.5400390625, 169.15403747558594);
INSERT INTO Tracks (id, name, length, startz) VALUES (305, 'Fferm Wynt', 5717.39990234375, -557.11328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (306, 'Fferm Wynt Reverse', 5717.3896484375, -22.597640991210938);
INSERT INTO Tracks (id, name, length, startz) VALUES (307, 'Dyffryn Afon', 5718.099609375, -23.46375274658203);
INSERT INTO Tracks (id, name, length, startz) VALUES (308, 'Dyffryn Afon Reverse', 5718.10009765625, 169.0966033935547);
INSERT INTO Tracks (id, name, length, startz) VALUES (309, 'Sweet Lamb', 9911.66015625, 2220.982177734375);
INSERT INTO Tracks (id, name, length, startz) VALUES (310, 'Geufron Forest', 10063.6005859375, 2481.169677734375);
INSERT INTO Tracks (id, name, length, startz) VALUES (311, 'Pant Mawr', 4788.669921875, 2221.004150390625);

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
INSERT INTO Tracks (id, name, length, startz) VALUES (411, 'Jezioro Lukie', 6437.80029296875, -396.3538513183594);

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
INSERT INTO Tracks (id, name, length, startz) VALUES (603, 'Taylor Farm Sprint', 7007.02001953125, -1261.5372314453125);
INSERT INTO Tracks (id, name, length, startz) VALUES (604, 'Chandlers Creek', 12341.25, 2065.60888671875);
INSERT INTO Tracks (id, name, length, startz) VALUES (605, 'Rockton Plains', 6951.15966796875, 2224.94921875);
INSERT INTO Tracks (id, name, length, startz) VALUES (606, 'Yambulla Mountain Ascent', 6398.90966796875, 2519.379150390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (607, 'Rockton Plains Reverse', 7116.14990234375, 2456.95458984375);
INSERT INTO Tracks (id, name, length, startz) VALUES (608, 'Chandlers Creek Reverse', 12305.0400390625, -1279.528564453125);
INSERT INTO Tracks (id, name, length, startz) VALUES (609, 'Noorinbee Ridge Ascent', 5277.02978515625, 2050.32373046875);
INSERT INTO Tracks (id, name, length, startz) VALUES (610, 'Bondi Forest', 7052.2998046875, -604.4165649414062);
INSERT INTO Tracks (id, name, length, startz) VALUES (611, 'Noorinbee Ridge Descent', 5236.91015625, -564.4724731445312);

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
INSERT INTO Tracks (id, name, length, startz) VALUES (709, 'Oberstein', 11487.189453125, -2661.260986328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (710, 'Kreuzungsring Reverse', 5666.25, 539.3837890625);
INSERT INTO Tracks (id, name, length, startz) VALUES (711, 'Waldaufstieg', 5361.90966796875, -2668.8408203125);

-- Catamarca, Argentina:800
INSERT INTO Tracks (id, name, length, startz) VALUES (800, 'San Isidro', 4171.5, -3227.052001953125);
INSERT INTO Tracks (id, name, length, startz) VALUES (801, 'Valle de los puentes', 7667.31982421875, 131.24305725097656);
INSERT INTO Tracks (id, name, length, startz) VALUES (802, 'Las Juntas', 8256.8603515625, 2581.4658203125);
INSERT INTO Tracks (id, name, length, startz) VALUES (803, 'Camino de acantilados y rocas', 5303.7900390625, 2581.419189453125);
INSERT INTO Tracks (id, name, length, startz) VALUES (804, 'Camino de acantilados y rocas inverso', 5294.81982421875, 1379.3668212890625);
INSERT INTO Tracks (id, name, length, startz) VALUES (805, 'Camino a Coneta', 4082.2998046875, -1864.53857421875);
INSERT INTO Tracks (id, name, length, startz) VALUES (806, 'El Rodeo', 2845.6298828125, 205.79042053222656);
INSERT INTO Tracks (id, name, length, startz) VALUES (807, 'La Merced', 2779.489990234375, 1344.740478515625);
INSERT INTO Tracks (id, name, length, startz) VALUES (808, 'Huillaprima', 3494.010009765625, -1876.92578125);
INSERT INTO Tracks (id, name, length, startz) VALUES (809, 'Camino a La Puerta', 8265.9501953125, 205.77462768554688);
INSERT INTO Tracks (id, name, length, startz) VALUES (810, 'Valle de los puentes a la inversa', 7929.18994140625, -3223.035400390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (811, 'Miraflores', 3353.0400390625, 131.09925842285156);

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
INSERT INTO Tracks (id, name, length, startz) VALUES (909, 'North Fork Pass Reverse', 12276.1201171875, 27.196266174316406);
INSERT INTO Tracks (id, name, length, startz) VALUES (910, 'Fuller Mountain Descent', 6488.330078125, 27.112668991088867);
INSERT INTO Tracks (id, name, length, startz) VALUES (911, 'Fury Lake Depart', 6681.60986328125, 2951.18115234375);

-- Monte Carlo, Monaco:1000
INSERT INTO Tracks (id, name, length, startz) VALUES (1000, 'Route de Turini', 10805.220703125, 1276.76611328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1001, 'Vallee descendante', 10866.8603515625, -2344.705810546875);
INSERT INTO Tracks (id, name, length, startz) VALUES (1002, 'Col de Turini – Sprint en descente', 4730.02001953125, 283.7648620605469);
INSERT INTO Tracks (id, name, length, startz) VALUES (1003, 'Col de Turini sprint en Montee', 4729.5400390625, -197.3816375732422);
INSERT INTO Tracks (id, name, length, startz) VALUES (1004, 'Col de Turini – Descente', 5175.91015625, -131.84573364257812);
INSERT INTO Tracks (id, name, length, startz) VALUES (1005, 'Gordolon – Courte montee', 5175.91015625, -467.3677062988281);
INSERT INTO Tracks (id, name, length, startz) VALUES (1006, 'Route de Turini (Descente)', 4015.35986328125, -991.9784545898438);
INSERT INTO Tracks (id, name, length, startz) VALUES (1007, 'Approche du Col de Turini – Montee', 3952.150146484375, 1276.780517578125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1008, 'Pra d´Alart', 9831.4501953125, -467.483154296875);
INSERT INTO Tracks (id, name, length, startz) VALUES (1009, 'Col de Turini Depart', 9832.0205078125, 283.4727478027344);
INSERT INTO Tracks (id, name, length, startz) VALUES (1010, 'Route de Turini (Montee)', 6843.3203125, -991.945068359375);
INSERT INTO Tracks (id, name, length, startz) VALUES (1011, 'Col de Turini – Depart en descente', 6846.830078125, -2344.592529296875);

-- Argolis, Greece:1100
INSERT INTO Tracks (id, name, length, startz) VALUES (1100, 'Ampelonas Ormi', 4860.1904296875, 91.54808044433594);
INSERT INTO Tracks (id, name, length, startz) VALUES (1101, 'Anodou Farmakas', 9666.5, -2033.0767822265625);
INSERT INTO Tracks (id, name, length, startz) VALUES (1102, 'Kathodo Leontiou', 9665.990234375, 457.1891784667969);
INSERT INTO Tracks (id, name, length, startz) VALUES (1103, 'Pomono Ékrixi', 5086.830078125, -2033.0767822265625);
INSERT INTO Tracks (id, name, length, startz) VALUES (1104, 'Koryfi Dafni', 4582.009765625, 164.40521240234375);
INSERT INTO Tracks (id, name, length, startz) VALUES (1105, 'Fourketa Kourva', 4515.39990234375, 457.18927001953125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1106, 'Perasma Platani', 10487.060546875, 504.3974609375);
INSERT INTO Tracks (id, name, length, startz) VALUES (1107, 'Tsiristra Théa', 10357.8798828125, -3672.5810546875);
INSERT INTO Tracks (id, name, length, startz) VALUES (1108, 'Ourea Spevsi', 5739.099609375, 504.3973693847656);
INSERT INTO Tracks (id, name, length, startz) VALUES (1109, 'Ypsona tou Dasos', 5383.009765625, -2277.10986328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1110, 'Abies Koiláda', 6888.39990234375, -1584.236083984375);
INSERT INTO Tracks (id, name, length, startz) VALUES (1111, 'Pedines Epidaxi', 6595.31005859375, -3672.58154296875);

-- Jämsä, Finland:1200
INSERT INTO Tracks (id, name, length, startz) VALUES (1200, 'Kailajärvi', 7515.40966796875, 39.52613830566406);
INSERT INTO Tracks (id, name, length, startz) VALUES (1201, 'Paskuri', 7461.65966796875, 881.0377197265625);
INSERT INTO Tracks (id, name, length, startz) VALUES (1202, 'Naarajärvi', 7310.5400390625, 846.68701171875);
INSERT INTO Tracks (id, name, length, startz) VALUES (1203, 'Jyrkysjärvi', 7340.3798828125, -192.40794372558594);
INSERT INTO Tracks (id, name, length, startz) VALUES (1204, 'Kakaristo', 16205.1904296875, 3751.42236328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1205, 'Pitkäjärvi', 16205.259765625, 833.2575073242188);
INSERT INTO Tracks (id, name, length, startz) VALUES (1206, 'Iso Oksjärvi', 8042.5205078125, 3751.42236328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1207, 'Oksala', 8057.52978515625, -3270.775390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (1208, 'Kotajärvi', 8147.560546875, -3263.315185546875);
INSERT INTO Tracks (id, name, length, startz) VALUES (1209, 'Järvenkylä', 8147.419921875, 833.2575073242188);
INSERT INTO Tracks (id, name, length, startz) VALUES (1210, 'Kontinjärvi', 14929.7998046875, 39.52613067626953);
INSERT INTO Tracks (id, name, length, startz) VALUES (1211, 'Hämelahti', 14866.08984375, -192.407958984375);

-- Perth and Kinross, Scotland:1300
INSERT INTO Tracks (id, name, length, startz) VALUES (1300, 'South Morningside', 12583.41015625, -1157.8094482421875);
INSERT INTO Tracks (id, name, length, startz) VALUES (1301, 'South Morningside Reverse', 12670.58984375, -1657.54736328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1302, 'Old Butterstone Muir', 5822.77001953125, -1157.8094482421875);
INSERT INTO Tracks (id, name, length, startz) VALUES (1303, 'Rosebank Farm', 7144.69970703125, -1657.54736328125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1304, 'Rosebank Farm Reverse', 6967.89990234375, 3383.734130859375);
INSERT INTO Tracks (id, name, length, startz) VALUES (1305, 'Old Butterstone Muir Reverse', 5659.8203125, 3338.64306640625);
INSERT INTO Tracks (id, name, length, startz) VALUES (1306, 'Newhouse Bridge', 12857.0703125, 1386.6217041015625);
INSERT INTO Tracks (id, name, length, startz) VALUES (1307, 'Newhouse Bridge Reverse', 12969.2109375, -403.2851867675781);
INSERT INTO Tracks (id, name, length, startz) VALUES (1308, 'Glencastle Farm', 5245.4501953125, 1386.62158203125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1309, 'Annbank Station', 7703.72021484375, -403.28497314453125);
INSERT INTO Tracks (id, name, length, startz) VALUES (1310, 'Annbank Station Reverse', 7587.64013671875, -1838.8472900390625);
INSERT INTO Tracks (id, name, length, startz) VALUES (1311, 'Glencastle Farm Reverse', 5238.43994140625, -1860.947021484375);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

-- Table: Cars
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

CREATE TABLE cars (id INTEGER PRIMARY KEY UNIQUE, name text, maxrpm real, idlerpm real);

-- H1 FWD class
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (100, 'Mini Cooper S', 733.03826904296875, 83.77580261230469);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (101, 'DS Automobiles DS 21', 628.31854248046875, 104.71975708007812);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (102, 'Lancia Fulvia HF', 680.678466796875, 99.48377227783203);

-- H2 FWD class
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (200, 'Volkswagen Golf GTI 16V', 785.398193359375, 94.24777984619141);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (201, 'Peugeot 205 GTI', 733.03826904296875, 125.66371154785156);

-- H2 RWD class
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (300, 'Ford Escort Mk II', 994.8377075195312, 125.66371154785156);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (301, 'Renault Alpine A110 1600 S', 837.758056640625, 167.55160522460938);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (302, 'Fiat 131 Abarth Rally', 837.758056640625, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (303, 'Opel Kadett C GT/E', 942.477783203125, 157.07963562011719);

-- H3 RWD class
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (400, 'BMW E30 Evo Rally', 932.005859375, 115.19173431396484);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (401, 'Opel Ascona 400', 785.398193359375, 136.13568115234375);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (402, 'Lancia Stratos', 890.1179809570312, 104.71975708007812);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (403, 'Renault 5 Turbo', 837.758056640625, 151.84365844726562);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (404, 'Datsun 240Z', 779.7432861328125, 80.42477416992188);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (405, 'Ford Sierra Cosworth RS500', 785.398193359375, 115.19173431396484);

-- Group B RWD
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (500, 'Lancia 037 Evo 2', 890.1179809570312, 125.66371154785156);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (501, 'Opel Manta 400', 816.81414794921875, 146.607666015625);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (502, 'BMW M1 Procar Rally', 968.6577758789062, 157.07963562011719);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (503, 'Porsche 911 SC RS', 837.758056640625, 136.13568115234375);

-- Group B 4WD
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (600, 'Audi Sport quattro S1 E2', 942.477783203125, 136.13568115234375);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (601, 'Peugeot 205 T16 Evo 2', 837.758056640625, 209.43951416015625);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (602, 'Lancia Delta S4', 890.1179809570312, 167.55160522460938);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (603, 'Ford RS200', 942.477783203125, 125.66371154785156);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (604, 'MG Metro 6R4', 994.8377075195312, 109.95574188232422);

-- R2
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (700, 'Ford Fiesta R2', 816.81414794921875, 157.07963562011719);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (701, 'Opel Adam R2', 905.825927734375, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (702, 'Peugeot 208 R2', 890.1179809570312, 167.55160522460938);

-- Group A
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (800, 'Mitsubishi Lancer Evolution VI', 733.03826904296875, 146.607666015625);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (801, 'Subaru Impreza 1995', 733.03826904296875, 115.19173431396484);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (802, 'Lancia Delta HF Integrale', 785.398193359375, 104.71975708007812);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (803, 'Ford Escort RS Cosworth', 733.03826904296875, 146.607666015625);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (804, 'Subaru Legacy RS', 791.1577758789062, 202.4232940673828);

-- NR4/R4
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (900, 'Subaru Impreza WRX STI NR4', 837.758056640625, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (901, 'Mitsubishi Lancer Evolution X', 785.398193359375, 178.02359008789062);

-- 4WD/2000cc
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1000, 'Citroen C4 Rally', 774.92620849609375, 188.49555969238281);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1001, 'ζkoda Fabia Rally', 774.92620849609375, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1002, 'Ford Focus RS Rally', 769.69024658203125, 186.92477416992188);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1003, 'Subaru Impreza 2008', 785.398193359375, 219.91148376464844);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1004, 'Ford Focus RS Rally 2001', 785.398193359375, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1005, 'Subaru Impreza (2001)', 837.758056640625, 204.2035369873047);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1006, 'Peugeot 206 Rally', 680.678466796875, 157.0796356201172);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1007, 'Subaru Impreza S4 Rally', 816.8141479492188, 207.34512329101562);

-- R5
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1100, 'Ford Fiesta R5', 774.92620849609375, 188.49555969238281);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1101, 'Peugeot 208 T16 R5', 785.398193359375, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1102, 'Mitsubishi Space Star R5', 837.758056640625, 219.91148376464844);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1103, 'ζkoda Fabia R5', 774.92620849609375, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1104, 'Volkswagen Polo GTI R5', 774.92620849609375, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1105, 'Citroen C3 R5', 743.51031494140625, 185.87757873535156);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1106, 'Ford Fiesta R5 MKII', 774.9262084960938, 183.2595672607422);

-- Rally GT 
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1200, 'Porsche 911 RGT Rally Spec', 942.477783203125, 188.4955596923828);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1201, 'BMW M2 Competition', 733.03826904296875, 146.607666015625);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1202, 'Chevrolet Camaro GT4.R', 759.21820068359375, 178.02359008789062);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1203, 'Aston Martin V8 Vantage GT4', 733.03826904296875, 104.71975708007812);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1204, 'Ford Mustang GT4 Ford RS200', 863.9380493164062, 146.607666015625);

-- F2 Kit Car
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1300, 'Peugeot 306 Maxi', 1151.9173583984375, 198.96754455566406);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1301, 'Seat Ibiza Kit Car', 942.477783203125, 136.13568115234375);
INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (1302, 'Volkswagen Golf Kitcar', 942.477783203125, 125.66371154785156);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

-- Table: Controls
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

CREATE TABLE controls(id INTEGER PRIMARY KEY UNIQUE, handbrake integer, shifting text, manualclutch integer, topgear integer);

-- H1 FWD
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (100, 1, 'H-PATTERN', 1, 4);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (101, 1, 'H-PATTERN', 1, 4);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (102, 1, 'H-PATTERN', 1, 4);

-- H2 FWD
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (200, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (201, 1, 'H-PATTERN', 1, 5);

-- H2 RWD
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (300, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (301, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (302, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (303, 1, 'H-PATTERN', 1, 5);

-- H3 RWD
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (400, 1, 'H-PATTERN', 1, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (401, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (402, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (403, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (404, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (405, 1, 'H-PATTERN', 1, 5);

-- Group B RWD
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (500, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (501, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (502, 1, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (503, 1, 'H-PATTERN', 1, 5);

-- Group B 4WD
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (600, 0, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (601, 0, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (602, 0, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (603, 0, 'H-PATTERN', 1, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (604, 0, 'H-PATTERN', 1, 5);

-- R2
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (700, 1, 'SEQUENTIAL', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (701, 1, 'SEQUENTIAL', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (702, 1, 'SEQUENTIAL', 0, 5);

-- Group A
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (800, 1, 'H-PATTERN', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (801, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (802, 1, 'H-PATTERN', 1, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (803, 1, 'H-PATTERN', 0, 7);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (804, 1, 'H-PATTERN', 0, 6);

-- NR4/R4
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (900, 1, 'H-PATTERN', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (901, 1, 'H-PATTERN', 0, 5);

-- 4WD/2000c
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1000, 1, 'PADDLE', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1001, 1, 'PADDLE', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1002, 1, 'PADDLE', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1003, 1, 'PADDLE', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1004, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1005, 1, 'PADDLE', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1006, 1, 'PADDLE', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1007, 1, 'H-PATTERN', 0, 6);

-- R5
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1100, 1, 'SEQUENTIAL', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1101, 1, 'SEQUENTIAL', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1102, 1, 'SEQUENTIAL', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1103, 1, 'SEQUENTIAL', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1104, 1, 'SEQUENTIAL', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1105, 1, 'SEQUENTIAL', 0, 5);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1106, 1, 'SEQUENTIAL', 0, 5);

-- Rally GT
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1200, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1201, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1202, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1203, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1204, 1, 'SEQUENTIAL', 0, 6);

-- F2 Kit Car
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1300, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1301, 1, 'SEQUENTIAL', 0, 6);
INSERT INTO controls(id, handbrake, shifting, manualclutch, topgear) VALUES (1302, 1, 'SEQUENTIAL', 0, 6);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
