#!/bin/bash
sqlite3 -init export-laptimes.sql dirtrally-laptimes.db .exit
echo Exported to snapshot.csv
read -s -n 1 -p "Press any key..."