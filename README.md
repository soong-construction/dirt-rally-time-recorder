## Set up
- Clone this repo
- Install Python3 plus pip
- Install dependencies
  - ``pip install PyYAML==3.11``
- Setup SQLite database with car and track tables, e.g. using sqlite shell: https://www.sqlite.org/cli.html
  - ``.open --new dirtrally-lb.db`` 
  - ``.read tracks.sql`` 
  - ``.read cars.sql``
- Enable UDP telemetry in [home-or-documents-dir]\My Games\DiRT Rally\hardwaresettings\hardware_settings_config.xml
  - ``<udp enabled="true" ...``
  
## Record stage times
- Start timetracking
  - ``python timerecord.py``
- Start DiRT Rally and finish a stage
- List your times from SQLite database
  - ``.open dirtrally-laptimes.db``
  - ``select t.name, c.name, l.time from tracks t, cars c, laptimes l where t.id=l.track and c.id=l.car;``

## Troubleshooting
Note: Since this is still WIP, consider dropping your *.db files if you encounter errors, thus starting over.  

## Resources
UDP telemetry documentation:  
[https://docs.google.com/spreadsheets/d/1O2_I-lGVDpDrhzcAlWCiVTHonUvn3rXfQGOVjOYLeB8/edit?usp=sharing]

## Remainder
Tested with DiRT Rally v1.22

Based on https://github.com/Slocan/timerecord

Credits to Billiam for original code:
https://github.com/Billiam/pygauge
