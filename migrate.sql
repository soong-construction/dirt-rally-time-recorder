-- Follow these migration steps if you already recorded data before updating to the mentioned commits

-- Commit 2cd7011ca0f84d3d2a4986363ac58d0bd2d65cc4
ALTER TABLE laptimes ADD COLUMN timestamp INTEGER DEFAULT NULL;

-- TODO Drop & recreate?
-- Commit b86935b29e40311d79d0fb628a16633b96abe2f3
UPDATE cars SET name="Delta HF Integrale", startrpm=183.25953674316406 WHERE id=14;