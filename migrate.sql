-- Follow these migration steps if you already recorded data before updating to the mentioned commits. The ".<cmd>" instructions are for sqlite3, please adapt to the SQL interface you are using

-- Commit 2cd7011ca0f84d3d2a4986363ac58d0bd2d65cc4
.open dirtrally-laptimes.db
ALTER TABLE laptimes ADD COLUMN timestamp INTEGER DEFAULT NULL;

-- Commit 34b85930f16a9e0022ffe006a699786af454189b
.open dirtrally-lb.db
DROP TABLE cars;
.read cars.sql;
