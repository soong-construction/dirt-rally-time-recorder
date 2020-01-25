-- The ".<cmd>" instructions are to be executed with sqlite3.exe  

-- Follow step A) only if you used dirt-rally-time-recorder PRIOR TO VERSION 1.0.0

-- Follow step B) if you DON'T use the bundled version of dirt-rally-time-recorder (.exe). Except for patch releases 
-- (e.g. 1.0.1, last number not 0) you should always update dirtrally-lb.db to include new cars and tracks

-- step A)
-- Commit 2cd7011ca0f84d3d2a4986363ac58d0bd2d65cc4
.open dirtrally-laptimes.db
ALTER TABLE laptimes ADD COLUMN timestamp INTEGER DEFAULT NULL;

-- step B)
.open --new dirtrally-lb.db

.read setup-dr1.sql
-- OR
.read setup-dr2.sql
