Del /F dirtrally-lb.db
bin\sqlite3 -batch -init resources\setup-dr1.sql dirtrally-lb.db .exit 
pyinstaller timerecord.spec --noconfirm --name timerecorder-dr1
