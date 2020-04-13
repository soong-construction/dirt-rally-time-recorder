@echo OFF
sqlite3 -init resources/export-laptimes.sql dirtrally-laptimes.db .exit
echo Exported to snapshot.csv
pause