## Goal
This tool allows you to track your stage times in DiRT Rally and browse them, which the game itself does not allow.  

Time tracking works for stage rallies and the Pikes Peak events (for now, Asphalt only).   

## First time set up
*These steps refer to Windows, Linux users will know how to use their package manager appropriately*

- Clone this repo or download and unpack its zip file to your disk
  - this creates your work folder, e.g. ``C:\dirtrally-time-recorder-master``
- Install Python3: https://wiki.python.org/moin/BeginnersGuide/Download
  - If Python was installed already, ensure [pip is set up properly](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) 
- Install dependencies
  - in a command prompt, run ``pip install PyYAML==3.12``
- Install SQLite: https://www.sqlite.org/cli.html  
  - choose the ``sqlite-tools-win32-x86-XXXXXX.zip`` package
  - extract ``sqlite3.exe`` to your work folder, i.e. next to ``timerecord.py``    
- Setup database with car and track tables with SQLite  
  - ``.open --new dirtrally-lb.db`` 
  - ``.read tracks.sql`` 
  - ``.read cars.sql``
  - ``.read controls.sql``
- Configure UDP telemetry in *[home-or-documents-dir]\My Games\DiRT Rally\hardwaresettings\hardware_settings_config.xml*
  - Enable telemetry and request extradata by adapting the appropriate line as follows: ``<udp enabled="true" extradata="3" ...``
  
## Record stage times
- Start time tracking  
  - open a command prompt (e.g. via the work folder context menu, this saves you from moving to this directory manually) and run ``python timerecord.py``
  - It should tell you to be *Waiting for data...*, otherwise check the set up or take a look at the Troubleshooting section   
- Start DiRT Rally and finish a stage  
  - the tool runs in the background, reporting the car and the track it identifies from the telemetry
  - on stage completion, it reports your top speed and saves your time 
- List your times with SQLite  
  - ``.open dirtrally-laptimes.db``
  - ``attach 'dirtrally-lb.db' as base;``
  - to create a CSV file consumable by your favorite spreadsheet editor, run ``.once snapshot.csv`` (don't if you prefer direct output)
  - ``select t.name, c.name, strftime('%Y-%m-%d %H:%M:%S', datetime(l.timestamp, 'unixepoch', 'localtime')), l.time from base.tracks t, base.cars c, laptimes l where t.id=l.track and c.id=l.car;``

## Troubleshooting
Since DiRT Rally telemetry data doesn't allow to clearly identify every available car, this tool will sometimes ask you to resolve this after completing a stage.  
In order to do so, use SQLite to 
- ``.open dirtrally-laptimes.db``
- and run the ``UPDATE laptimes...`` statement that matches the actual car you drove

When you import the CSV snapshot file as a spreadsheet, make sure to select UTF-8 encoding.   

If you encounter an error message talking about sockets, understand that this tool cannot run in parallel, but only in a single instance at the same time.  

In case you modified the telemetry ip or port in *hardware_settings_config.xml*, adapt ``config.yml`` to these.

Note: Since this is still WIP, have a look at ``migrate.sql`` to find instructions how to migrate your data when updating this tool.    
Consider dropping your ``*.db`` files if you encounter errors, thus starting over (time tracking data is lost).  

Feel free to open an issue.  


## Resources
UDP telemetry documentation:  
[https://docs.google.com/spreadsheets/d/1O2_I-lGVDpDrhzcAlWCiVTHonUvn3rXfQGOVjOYLeB8/edit?usp=sharing]

## Remainder
Tested with DiRT Rally v1.22

Thanks to Slocan for the initial version: https://github.com/Slocan/timerecord

Credits to Billiam for the core code: https://github.com/Billiam/pygauge
