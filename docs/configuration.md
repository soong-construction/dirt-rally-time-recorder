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
  user_signals: 0
```

Heuristics will try to resolve car ambiguities and decide for one of the possible cars. This can reduce the number of times you need to run update scripts after a session and keep your installation folder more tidy. Note that heuristics are only applied when you complete a stage, not before.

Since heuristics are only correct to a certain degree (but better than tossing a coin), the update scripts are even more important. Always make sure to run the provided script in case the heuristics is wrong, otherwise the recorded data is false.  

You first need to activate heuristics with `activate: 1`. Afterwards, a very basic heuristics method is applied that will choose one of the possible cars by chance. If you enable any other heuristics, each one described below overrules the previous heuristics.

If you use authentic shifting (also cf. [this setting](#car-control-information)), i.e. use H-pattern shifting for cars that have such gearboxes, you can also configure `authentic_shifting: 1` to enable gear shift heuristics. It will detect skipped gears (which cannot occur for sequential shifting) to tell H-pattern cars from others.  

Even with authentic shifting taken into account, not all car ambiguities can be resolved. To this end, user signals are a way to tell *dirt-rally-time-recorder* which of two possible cars it should assume was chosen. There are two signals which are explained below: "engage THROTTLE turning LEFT" and "engage THROTTLE turning RIGHT". 

If enabled (`user_signals: 1`), user signals are interpreted after you pulled the handbrake and as long as the car has not launched from the start line. User signals are transmitted with the user-defined game inputs. Caution: Depending on your input settings, the game will force center your wheel after you pull the handbrake. It's best to give the signal after force center.  

If you steer to the *left* when you hit the throttle, this is a LEFT signal. Steering to the *right* while engaging throttle is a RIGHT signal. If you use an analogue input such as a wheel, you don't need to go the maximum input level. The program plays a short tune to confirm a signal to you. After that, you can stop the signal input and focus on the launch. Since this will almost always be with the wheel straightened, no further signals should be received.  

The program has an internal order of cars that match the car's position in the in-game menus. Two ambiguous cars can be seen as ordered LEFT and RIGHT, depending on where you will find them in the menu:
- inside one class, signal LEFT for the first car in the list, RIGHT for the other
- if the cars are in different classes, signal LEFT for the car in the class first in the list, RIGHT for the other

After a while, you will know which cars cannot be told apart by the UDP telemetry, what their in-game order is, and which one is LEFT/RIGHT. Note that the received signal holds for the current stage. A stage restart will reset signal detection.

Caveat: User signals only work properly for DiRT Rally 2.0, enabling it for DiRT Rally can lead to wrong heuristics.

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
