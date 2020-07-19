if (Test-Path dirtrally-lb.db) {
  Remove-Item -Force dirtrally-lb.db
}
bin\sqlite3 -batch -init resources\setup-dr1.sql dirtrally-lb.db .exit 
pyinstaller timerecord.spec --noconfirm --name timerecorder-dr1
pwsh.exe -wd resources resources\sign.ps1 -Exe ..\dist\timerecorder-dr1\timerecord.exe
exit $LASTEXITCODE
