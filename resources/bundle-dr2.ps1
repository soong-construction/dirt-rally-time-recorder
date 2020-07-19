if (Test-Path dirtrally-lb.db) {
  Remove-Item -Force dirtrally-lb.db
}
bin\sqlite3 -batch -init resources\setup-dr2.sql dirtrally-lb.db .exit 
pyinstaller timerecord.spec --noconfirm --name timerecorder-dr2
pwsh.exe -wd resources resources\sign.ps1 -Exe ..\dist\timerecorder-dr2\timerecord.exe
exit $LASTEXITCODE
