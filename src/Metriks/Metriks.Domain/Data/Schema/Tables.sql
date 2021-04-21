CREATE TABLE WeightMeasurements (
	wm_key INTEGER PRIMARY KEY,
	id VARCHAR(100) NOT NULL,
	entry_date DATETIME,
	weight DECIMAL(10,2),
	unit VARCHAR(15)
);
GO



