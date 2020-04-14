# Building

Using an IDE is recommended, the author has been content with using [PyDev](https://www.pydev.org/). 

## Requirements
Cf. job `build` in `.github/workflows/main.yml`

## Tasks
- `python -m timerecorder.timerecord` to run *dirt-rally-timerecorder* from a command line
- `python -m pytest tests` to run all tests

# Releasing

Note that bundling with pyinstaller is OS dependent. Bundle releases for *dirt-rally-time-recorder* target x64 Windows platforms. 

## Prepare a release
Not all steps are necessary for each release
- check if a new SQLite version should be included
- check if a new stable Python version is available
- check if PyInstaller can be updated
- update `migrate.sql`

Finally
- bump VERSION
- create tag

## Requirements
Cf. job `assemble` in `.github/workflows/main.yml`

## Bundling locally 

*Note:* Since v2.5.0, release are bundled automatically as part of the CI (GitHub Actions).

To create a bundle (e.g. for DR1)
- follow the steps of the `assemble` job in `.github/workflows/main.yml`
- zip `/dist/timerecorder` as `timerecorder-dirt-rally.zip`

## Publish release
- draft a new GitHub release
- upload all zip files
- publish the release

