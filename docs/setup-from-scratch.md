### Set up from scratch  
*These steps refer to Windows. Linux users should take a look at this [issue.](https://github.com/soong-construction/dirt-rally-time-recorder/issues/33#issue-606797917)*

- From the [latest release](https://github.com/soong-construction/dirt-rally-time-recorder/releases/latest), download and unpack the sources zip file to your disk. Instead, you can also clone the repository.
  - this creates your *work folder*, e.g. `C:\dirtrally-time-recorder-dr2`
- Install Python 3.7: https://wiki.python.org/moin/BeginnersGuide/Download
  - If Python was installed already, ensure [pip is set up properly](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) 
- Follow the bundling instructions in [develop.md](develop.md#bundling) 
  - this creates your bundle in `dist`. You can move the *installation folder* `timerecorder` anywhere you like
  - you can delete the work folder afterwards
- Start time tracking  
  - in your installation folder, start `timerecord.exe` 
  - It should tell you to be *Waiting for data...*, otherwise check the set up or take a look at [Troubleshooting](../README.md#troubleshooting)

