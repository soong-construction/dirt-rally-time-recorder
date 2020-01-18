-- Follow these migration steps if you already recorded data before updating to the mentioned commits. 
-- The ".<cmd>" instructions are for sqlite3, please adapt if you are using another SQL interface  

-- TODO #15 Remove migrate.sql from bundle as migration is automated
-- NOTE If you use the bundled version of dirt-rally-time-recorder, you can skip migration of dirtrally-lb.db

-- ONLY if you used this tool prior to version 1.0.0
 
-- Commit 2cd7011ca0f84d3d2a4986363ac58d0bd2d65cc4
.open dirtrally-laptimes.db
ALTER TABLE laptimes ADD COLUMN timestamp INTEGER DEFAULT NULL;

-- If you used this tool prior to version 2.1.0

-- Commit 5846c3dae24554d017a17d7e48fb3cea18d9144e
.open --new dirtrally-lb.db

.read setup-dr1.sql
-- OR
.read setup-dr2.sql

-- TODO #15 Migration should only be necessary with a new minor version (e.g. 1.2.0), no need to refer to commit hashes.
-- If only dirtrally-lb.db changes, recommend migration for _every_ new version?
