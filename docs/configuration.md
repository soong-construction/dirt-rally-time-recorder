## Configuration

This document describes all the configuration options for *dirt-rally-time-recorder*. Please read it carefully 
before you change any settings. The following holds for any of the settings:
- never change the option name, only its value
- 0 means disabled or inactive, 1 means enabled or active
- mistakes when editing the file may lead to crashes at start up of timerecord.exe or strange behaviour
- check `timerecord.log` for hints what might be wrong with your `config.yml'
- in case of problems, you can always delete `config.yml` altogether and restart the tool in order to 
create a fresh configuration file
- any setting only applies the next time you start timerecord.exe

### Speed unit
`speed_unit: kph`

If you prefer imperial units (mph), you can change the `speed_unit` in `config.yml` (default: kph). 
If you change this later on, you will falsify top speeds of recorded stages (unless you migrate your database).
So this should be a setting you configure once.  

### Car control information
`show_car_controls: 1`

If you do not care for car control information like forward gears and the actual shifting and handbrake options, you can change this setting to `0` to disable them.

### Telemetry 
```
telemetry_server:
  host: 127.0.0.1
  port: 20777
```

This must match the host and port of the machine DiRT Rally [2.0] runs on.  
The default `host` should not be changed unless the game runs on a different machine. The port can be changed if you configure the game UDP output to another port than the default (cf. [README.md](../README.md#configuration))

 