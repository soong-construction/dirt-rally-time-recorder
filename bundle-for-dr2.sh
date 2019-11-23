# NOTE This is meant to be executed in Git Bash, hence the terminal switch with winpty - omit in a pure bash
rm -f dirtrally-lb.db
sqlite3 -batch -init setup-dr2.sql dirtrally-lb.db .exit 
winpty pyinstaller timerecord.spec --noconfirm