![CI](https://github.com/soong-construction/dirt-rally-time-recorder/workflows/CI/badge.svg)

## Goal
This tool allows you to track your stage times in DiRT Rally and DiRT Rally 2.0 and browse them, which the game itself does not allow.  

Time tracking works for stage rallies and the Pikes Peak events of the original DiRT Rally.  

> To check if the latest DiRT Rally 2.0 DLC is supported, look for or create an [issue.](https://github.com/soong-construction/dirt-rally-time-recorder/issues?q=label%3ADLC) 

## First time set up

You can choose to download *dirt-rally-time-recorder* as a ready-to-use bundle (tested to work on Windows 10 x64). If you don't trust pre-built .exe files, you can set it up from scratch. 

### Ready-to-use bundle
- Download the [latest release](https://github.com/soong-construction/dirt-rally-time-recorder/releases/latest) for either the original DiRT Rally or 2.0
  - Unzip the installation folder somewhere
- Start time tracking  
  - in your installation folder, start `timerecord.exe` 
  - It should tell you to be *Waiting for data...*, otherwise take a look at [Troubleshooting](#troubleshooting)  

### ... or set up from scratch  
*These steps refer to Windows. Linux users should take a look at this [issue.](https://github.com/soong-construction/dirt-rally-time-recorder/issues/33#issue-606797917)*

- From the [latest release](https://github.com/soong-construction/dirt-rally-time-recorder/releases/latest), download and unpack the sources zip file to your disk. Instead, you can also clone the repository.
  - this creates your *work folder*, e.g. `C:\dirtrally-time-recorder-dr2`
- Install Python 3.7: https://wiki.python.org/moin/BeginnersGuide/Download
  - If Python was installed already, ensure [pip is set up properly](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) 
- Follow the bundling instructions in [develop.md](https://github.com/soong-construction/dirt-rally-time-recorder/blob/master/develop.md#bundling) 
  - this creates your bundle in `dist`. You can move the *installation folder* `timerecorder` anywhere you like
  - you can delete the work folder afterwards
- Start time tracking  
  - in your installation folder, start `timerecord.exe` 
  - It should tell you to be *Waiting for data...*, otherwise check the set up or take a look at [Troubleshooting](#troubleshooting)

### Updating
To update to a new version, simply download the new release or create a new bundle as instructed above. To be safe, backup your `dirtrally-laptimes.db`. You can overwrite your existing installation folder with the new `timerecorder` folder.  

Make sure to start `timerecord.exe` once to allow to migrate the database and config. 

### Configuration
If you prefer imperial units (mph), you can change the `speed_unit` in `config.yml` (default: kph). Afterwards, restart *dirt-rally-time-recorder*. If you change this later on, you will falsify top speeds of recorded stages (unless you migrate your database).  

Before starting DiRT Rally [2.0] you need to enable UDP telemetry like so:
- Navigate to the settings directory of [DiRT Rally](https://www.pcgamingwiki.com/wiki/DiRT_Rally#Configuration_file.28s.29_location) or [DiRT Rally 2.0](https://www.pcgamingwiki.com/wiki/DiRT_Rally_2.0#Configuration_file.28s.29_location) (e.g. `%USERPROFILE%\Documents\My Games\DiRT Rally 2.0\hardwaresettings\`)
- Open `hardware_settings_config.xml` with a text editor
- Enable telemetry and request extradata by adapting the appropriate line as follows: `<udp enabled="true" extradata="3" ...`  
- Note for VR users: For the VR mode, the above setting has to be adapted in  `hardware_settings_config_vr.xml` as well
  
## Record stage times
- Start DiRT Rally [2.0] and finish a stage  
  - *dirt-rally-time-recorder* runs in the background, reporting the car and the track it identifies from the telemetry  
  - for cars, it will display control interface information such as the transmission type (based on [this discussion](http://forums.codemasters.com/discussion/7071/dirt-rally-handbrake-and-transmission-information)) 
  - it will look something like this:
```
TRACK: Sweet Lamb
CAR: Volkswagen Golf GTI 16V
Volkswagen Golf GTI 16V: H-PATTERN shifting, 5 speed, with manual CLUTCH, with HANDBRAKE
```
- On stage completion, it reports your top speed and time and saves it to the database 
  - to quickly list your recorded times with SQLite, run `list-laptimes.bat`  
  - to dump the database into a CSV file consumable by your favorite spreadsheet editor, run `export-laptimes.bat`  

## Limitations
Since DiRT Rally [2.0] telemetry data doesn't allow to clearly identify every available car and track, this tool will sometimes ask you to resolve this after completing a stage.  

In order to consolidate the database, the tool prepares update scripts for you, e.g. `1573403766_ElRodeo_PoloGTIR5.bat`
- open your installation folder  
- run the update script that matches the car or track you chose (e.g. double-click it)  
- you will barely notice a window opening and closing, and that's it
- each time you start *dirt-rally-time-recorder*, it automatically removes update scripts older than a week

## Troubleshooting
Starting:
- if you encounter an error message about sockets, understand that this tool cannot run in parallel, but only in a single instance at the same time
- unless you downloaded the bundled version, have a look at `resources/migrate.sql` to find instructions how to update to new releases
- if you encounter errors at start-up, see if renaming the file `dirtrally-laptimes.db` helps (which will create a new database) 

Configuring the tool: 
- Steam updates of the game sometimes reset *hardware_settings_config.xml*. Then, repeat the [configuration steps](#configuration) to enable UDP telemetry again
- in case you modified the telemetry host or port in *hardware_settings_config.xml*, adapt `config.yml` accordingly

Exporting:
- when you export your stage times, be sure to avoid corrupt characters and import the CSV file in a spreadsheet editor with UTF-8 encoding. In MS Excel, use the [query tool.](https://support.office.com/en-us/article/import-data-from-external-data-sources-power-query-be4330b3-5356-486c-a168-b68e9e616f5a)   

In any case, feel free to [open an issue](https://github.com/soong-construction/dirt-rally-time-recorder/issues/new) and attach the `timerecorder.log` from your installation folder. You can also contact the author through [Steam](https://steamcommunity.com/id/soong-construction).


## Resources
UDP telemetry documentation (cf. DiRT 4 for DiRT Rally 2.0):  
[https://docs.google.com/spreadsheets/d/1UTgeE7vbnGIzDz-URRk2eBIPc_LR1vWcZklp7xD9N0Y/edit#gid=0]

Contributors cf. to `develop.md`.

## Remainder
Tested with DiRT Rally v1.22 and DiRT Rally 2.0 v1.13

UDP data recognition in collaboration with ErlerPhilipp: https://github.com/ErlerPhilipp/dr2_logger 

Thanks to Slocan for the initial version: https://github.com/Slocan/timerecord

Credits to Billiam for the core code: https://github.com/Billiam/pygauge
