-- The ".<cmd>" instructions are to be executed with SQLite3

-- Follow step A) if you used dirt-rally-time-recorder PRIOR TO VERSION 1.0.0

-- Follow step B) if you used dirt-rally-time-recorder prior to version 2.6.2, but DID NOT use the bundled version (.exe).

-- step A)
-- Commit 2cd7011ca0f84d3d2a4986363ac58d0bd2d65cc4
.open dirtrally-laptimes.db
ALTER TABLE laptimes ADD COLUMN timestamp INTEGER DEFAULT NULL;

-- step B)
-- Back up dirtrally-laptimes.db and config.yml
-- Follow the setup instructions in README.md
-- Copy dirtrally-laptimes.db and config.yml to the installation folder
