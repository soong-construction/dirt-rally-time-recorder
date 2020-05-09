## Configuration

This document describes all the configuration options for *dirt-rally-time-recorder*. Please read it carefully 
before you change any settings. The following holds for any of the settings:
- never change the option name, only its value
- 0 means disabled or inactive, 1 means enabled or active
- mistakes when editing the file may lead to crashes at start up of `timerecord.exe` or strange behaviour
- check `timerecord.log` for hints what might be wrong with your `config.yml`
- in case of problems, you can always delete `config.yml` altogether and restart the tool in order to 
create a fresh configuration file
- changed settings only apply the next time you start `timerecord.exe`

### Heuristics
```
heuristics:
  activate: 0
  authentic_shifting: 0
```

Heuristics will try to resolve car ambiguities and decide for one of the possible cars. This can reduce the number of times you need to run update scripts after a session and keep your installation folder more tidy.

Since heuristics are only correct to a certain degree (but better than tossing a coin), the update scripts are even more important. Always make sure to run the provided script in case the heuristics is wrong, otherwise the recorded data is false.  

You first need to activate heuristics with `activate: 1`. Afterwards, a very basic heuristics method is applied that will choose one of the possible cars by chance. 

If you use authentic shifting (also cf. [this setting](#car-control-information)), i.e. use H-pattern shifting for cars that have such gearboxes, you can also configure `authentic_shifting: 1` to enable gear shift heuristics. It will detect skipped gears (which cannot occur for sequential shifting) to tell H-pattern cars from others.  


### Update script removal
`keep_update_scripts_days: 7`

Update scripts allow you to resolve unclear recordings for ambiguous cars and tracks. Whether you use them or not, they will ultimately gather and pollute the installation folder. After a certain time (one week per default), update scripts will be removed at start up. You can select a different number of days for that time. If you go below the default value, a warning will be shown.

### Car control information
`show_car_controls: 1`

If you do not care for car control information like forward gears and the actual shifting and handbrake options, you can change this setting to `0` to disable them.

### Speed unit
`speed_unit: kph`

If you prefer imperial units (mph), you can change the `speed_unit` in `config.yml` (default: kph). 
If you change this later on, you will falsify top speeds of recorded stages (unless you migrate your database).
So this should be a setting you configure once.  

### Telemetry 
```
telemetry_server:
  host: 127.0.0.1
  port: 20777
```

This must match the host and port of the machine DiRT Rally [2.0] runs on.  
The default `host` should not be changed unless the game runs on a different machine. The port can be changed if you configure the game UDP output to another port than the default (cf. [README.md](../README.md#configuration))

 