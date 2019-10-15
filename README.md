[![Build Status](https://travis-ci.com/soong-construction/dirt-rally-time-recorder.svg?branch=master)](https://travis-ci.com/soong-construction/dirt-rally-time-recorder)
## Goal
This tool allows you to track your stage times in DiRT Rally and DiRT Rally 2.0 and browse them, which the game itself does not allow.  

Time tracking works for stage rallies and the Pikes Peak events of the original DiRT Rally.   

## Enable game telemetry
- Configure UDP telemetry in *[home-or-documents-dir]\My Games\DiRT Rally [2.0]\hardwaresettings\hardware_settings_config.xml*
  - Enable telemetry and request extradata by adapting the appropriate line as follows: ``<udp enabled="true" extradata="3" ...``
  
## First time set up
You can choose to download and unzip a ready-to-use bundle (tested to work on Windows 10 x64). If you don't trust pre-built .exe files, set up *dirt-rally-time-recorder* from scratch 

### Ready-to-use bundle
- Download the latest release for either the original DiRT Rally or 2.0 and unzip it somewhere
- Start ``timerecord.exe``
  - It should tell you to be *Waiting for data...*, otherwise take a look at the Troubleshooting section

### Set up from scratch  
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
  - ``.read setup-dr1.sql`` (or ``setup-dr2.sql``)
- Start time tracking  
  - open a command prompt (e.g. via the work folder context menu, this saves you from moving to this directory manually) and run ``python timerecord.py``
  - It should tell you to be *Waiting for data...*, otherwise check the set up or take a look at the Troubleshooting section   
  
## Record stage times
- Start DiRT Rally [2.0] and finish a stage  
  - the tool runs in the background, reporting the car and the track it identifies from the telemetry  
  - for cars, it will display control interface information such as the transmission type (based on [this discussion](http://forums.codemasters.com/discussion/7071/dirt-rally-handbrake-and-transmission-information)) (TODO Toggle off for DR2)  
  - on stage completion, it reports your top speed and saves your time 
- to quickly list your times with SQLite, run ``list-laptimes.bat``  
  - to create a CSV file consumable by your favorite spreadsheet editor, run ``export-laptimes.bat``  

## Troubleshooting
Since DiRT Rally [2.0] telemetry data doesn't allow to clearly identify every available car and track, this tool will sometimes ask you to resolve this after completing a stage.  
In order to do so, use SQLite to 
- ``.open dirtrally-laptimes.db``
- and run the ``UPDATE laptimes...`` statement that matches the actual car or track you drove

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
Tested with DiRT Rally v1.22 and DiRT Rally 2.0 v1.9

Thanks to Slocan for the initial version: https://github.com/Slocan/timerecord

Credits to Billiam for the core code: https://github.com/Billiam/pygauge
