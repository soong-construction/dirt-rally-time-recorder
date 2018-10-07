-- Follow these migration steps if you already recorded data before updating to the mentioned commits

-- Commit 2cd7011ca0f84d3d2a4986363ac58d0bd2d65cc4
ALTER TABLE laptimes ADD COLUMN timestamp INTEGER DEFAULT NULL;

-- Commit 25b7b34602271e651d1ba6f7fd40a8e8a3c297b4
.open dirtrally-lb.db
DROP TABLE tracks;
.read tracks.sql