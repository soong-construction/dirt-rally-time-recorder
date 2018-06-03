Steps to run:
- Clone repo
- Install Python3 plus pip
- Install dependencies
  - ``pip install PyYAML==3.11``
- Setup car and track tables, e.g. with sqlite shell: https://www.sqlite.org/cli.html
  - ``.read tracks.sql`` 
  - ``.read cars.sql``
- Start timetracking
  - ``python timerecord.py``

OUTDATED:
This software records your stage times for Dirt Rally online (and locally in a sqlite db). You can see an example here: http://dirtrally.marcoz.org/showTimes.php?u=f62bfefb1035

To install:
- Download: http://dirtrally.marcoz.org/timerecord.zip
- Extract anywhere
- Configure Dirt Rally's config at My Documents\My Games\DiRT Rally\hardwaresettings\hardware_settings_config.xml to: 
<motion enabled="true" ip="127.0.0.1" port="20777" delay="1" extradata="3" />

- Start timerecord.exe
- Start Dirt Rally
- The first line should give you your personal link with your stage times as you go

Requirements:
Python 3 (tested with 3.4)
PyYAML==3.11

Credits to Billiam for original code:
https://github.com/Billiam/pygauge
