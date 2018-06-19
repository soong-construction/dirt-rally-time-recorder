-- Follow these migration steps if you already recorded data before updating to the mentioned commits

-- Commit 27bf24f9c4db47e3c82627828396e9b43509f937
ALTER TABLE laptimes ADD COLUMN timestamp INTEGER DEFAULT NULL;