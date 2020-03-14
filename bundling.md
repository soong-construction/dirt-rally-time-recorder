Note that bundling with pyinstaller is OS dependent. Releases for dirt-rally-time-recorder target x64 Windows platforms. 

## Prepare a release
Not all steps are necessary for each release
- check if a new SQLite version should be included
- check if a new stable Python version is available
- check if PyInstaller can be updated
- update `migrate.sql`

Finally
- bump VERSION
- create tag

## Bundling locally 

*Note:* Since v2.5.0, release are bundled automatically as part of the CI (GitHub Actions).

Once, run `pip install pyinstaller==3.5`.  

To create bundle (e.g. for DR1)
- perform the bundle steps as per `.github/workflows`
- zip `/dist/timerecorder` as `timerecorder-dirt-rally.zip`

## Publish release
- draft a new GitHub release
- upload all zip files
- publish the release

