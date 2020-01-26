Note that bundling with pyinstaller is OS dependent. Releases for dirt-rally-time-recorder target x64 Windows platforms. 

Once, run `pip install pyinstaller==3.5`.  

To create bundle (repeat for DR2)
- update `migrate.sql`
- check if a new SQLite version should be included
- check if a new stable Python version is available
- check if PyInstaller can be updated
- bump version and create tag
- execute `bundle-for-dr1.sh`
- zip it as `timerecorder-dirt-rally.zip`

Draft a new GitHub release, upload all zip files, and publish the release.
