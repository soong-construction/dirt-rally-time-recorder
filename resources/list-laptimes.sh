#!/bin/bash
sqlite3 -init list-laptimes.sql dirtrally-laptimes.db .exit
read -s -n 1 -p "Press any key..."