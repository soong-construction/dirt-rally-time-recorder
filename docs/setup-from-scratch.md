### Set up from scratch

- From the [latest release](https://github.com/soong-construction/dirt-rally-time-recorder/releases/latest), download and unpack the sources zip file to your disk. Instead, you can also clone the repository.
  - this creates your *work folder*, e.g. `C:\dirt-rally-time-recorder`
- Install Python 3.7: https://wiki.python.org/moin/BeginnersGuide/Download
  - If Python was installed already, ensure [pip is set up properly](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) 
- Follow the bundling instructions in [develop.md](develop.md#bundling) 
  - this creates your *installation folder* under `dist`. You can move `timerecorder-dr1` or `timerecorder-dr2` anywhere you like
  - you can delete the work folder afterwards
- Start time tracking  
  - in your installation folder, start `timerecord.exe`
    > on Linux, call `python -m timerecorder.timerecord` 
  - It should tell you to be *Waiting for data...*, otherwise check the set up or take a look at [Troubleshooting](../README.md#troubleshooting)

