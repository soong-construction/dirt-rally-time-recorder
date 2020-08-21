if (Test-Path dirtrally-lb.db) {
  Remove-Item -Force dirtrally-lb.db
}
bin\sqlite3 -batch -init resources\setup-dr1.sql dirtrally-lb.db .exit 
pyinstaller --clean --noconfirm --version-file=resources\version_info.txt timerecord.spec --name test
pwsh.exe -wd resources resources\sign.ps1 -Exe ..\dist\timerecorder-dr1\timerecord.exe
exit $LASTEXITCODE
