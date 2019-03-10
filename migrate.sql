-- Follow these migration steps if you already recorded data before updating to the mentioned commits. The ".<cmd>" instructions are for sqlite3, please adapt to the SQL interface you are using

-- ONLY if you used this tool prior to version 1.0.0
 
-- Commit 2cd7011ca0f84d3d2a4986363ac58d0bd2d65cc4
.open dirtrally-laptimes.db
ALTER TABLE laptimes ADD COLUMN timestamp INTEGER DEFAULT NULL;

-- Commit 34b85930f16a9e0022ffe006a699786af454189b
.open dirtrally-lb.db
DROP TABLE cars;
.read cars.sql

-- If you used this tool prior to version 1.1.0

-- Commit d9574d73f07efde6dc98502cdc628164cbcd444c
.open dirtrally-lb.db
.read controls.sql

-- Commit b78fcfaedfad1814c57242dace6a4b84e8a143ea
.open dirtrally-lb.db
DROP TABLE controls;
.read controls.sql

-- Commit 2a3071e64ae986c51873f68b000ca475375afed6
.open dirtrally-lb.db
DROP TABLE tracks;
.read tracks.sql

