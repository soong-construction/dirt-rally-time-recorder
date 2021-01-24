# Building

Using an IDE is recommended, the author has been content with using [PyDev](https://www.pydev.org/). 

## Requirements
- to set up a Python enviroment with the necessary dependencies, cf. to the job `build` in `.github/workflows/main.yml`
- optionally, install coverage

## Tasks
- `python -m timerecorder.timerecord` to run *dirt-rally-time-recorder* from a command line
- `python -m pytest tests` to run all tests
- `coverage run -m pytest tests` and `coverage report -m` to keep statement coverage at around 90 %
- `pylint timerecorder --rcfile=timerecorder/.pylintrc` to lint code
- `pylint tests --rcfile=tests/.pylintrc` to lint tests

# Bundling

Note that bundling with pyinstaller is OS dependent.

## Requirements
Cf. job `assemble`, step `Install job dependencies` in `.github/workflows/main.yml`

## Tasks

To bundle for DiRT Rally
* Cf. job `assemble`, step `Bundle DR1 executable` in `.github/workflows/main.yml`

To bundle for DiRT Rally 2.0
* Cf. job `assemble`, step `Bundle DR2 executable` in `.github/workflows/main.yml`

*Hint*: You can disregard the `shell` and `env` parameters. To invoke the .ps1 scripts, you need the Powershell and to [allow script execution](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7). You should also remove the signing step in the scripts if you bundle locally.

*Hint regarding Linux*: Use `sh resources/build-local.sh dr1` to build the installation folder for DiRT Rally
- ensure that this folder is on the search path
- ensure that SQLite 3.33.0 or newer is on the search path
- you might need to install an additional library under Debian: `libasound2-dev`

# Releasing

## Requirements
Not all steps are necessary for each release
- check if a new SQLite version should be included: https://www.sqlite.org/index.html
- check if a new stable Python version is available: https://www.python.org/downloads/
- check if PyInstaller can be updated https://pyinstaller.readthedocs.io/en/stable/CHANGES.html
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

# License matters
The `LICENSE` must be kept up-to-date, although it should rarely change.  

The `THIRD_PARTY_LICENSES` include all works from outside this project, which must be compatible to the chosen `LICENSE`.
- All used libraries like PyYAML: Include necessary texts
- All used build tools like pytest: same
- PyInstaller because we built bundles with it that are not bound to its license
- CPython license including special module licenses for the bundles: https://docs.python.org/3.8/license.html#psf-license-agreement-for-python-release
- All used binaries like sounds

`xref-timerecord.html` from the bundling process can help identify dependencies.
