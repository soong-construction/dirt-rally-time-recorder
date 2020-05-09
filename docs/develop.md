# Building

Using an IDE is recommended, the author has been content with using [PyDev](https://www.pydev.org/). 

## Requirements
Cf. job `build` in `.github/workflows/main.yml`

## Tasks
- `python -m timerecorder.timerecord` to run *dirt-rally-timerecorder* from a command line
- `python -m pytest tests` to run all tests

# Bundling

Note that bundling with pyinstaller is OS dependent. Bundles for *dirt-rally-time-recorder* target x64 Windows platforms. 

## Requirements
Cf. job `assemble`, step `Install` in `.github/workflows/main.yml`

## Tasks

To bundle for DiRT Rally
* Cf. job `assemble`, step `Bundle DR1` in `.github/workflows/main.yml`

To bundle for DiRT Rally 2.0
* Cf. job `assemble`, step `Bundle DR2` in `.github/workflows/main.yml`

# Releasing

## Requirements
Not all steps are necessary for each release
- check if a new SQLite version should be included
- check if a new stable Python version is available
- check if PyInstaller can be updated
- update `migrate.sql`

Finally
- bump VERSION
- create tag

## Tasks

Bundles are automatically created by GitHub Actions for all tagged versions and provided in `artifacts.zip`. To create a release bundle locally (e.g. for DR1)
- follow the steps [above](#bundling)
- zip `/dist/timerecorder-dr1` as `timerecorder-dirt-rally.zip`

## Publish release
- draft a new GitHub release
- upload all bundles
- publish the release

