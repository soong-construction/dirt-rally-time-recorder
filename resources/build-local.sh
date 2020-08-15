game=$1
echo Building for $game
rm -f dirtrally-lb.db
./bin/sqlite3 -batch -init resources/setup-${game}.sql dirtrally-lb.db .exit 
pyinstaller timerecord.spec --noconfirm --name timerecorder-${game}

# Linux only
rm dist/**/*.pyd
rm dist/**/*.zip
rm dist/**/timerecord.exe*
rm dist/**/python*.dll
cp --parents timerecorder/*.py dist/timerecorder-${game}

pushd dist/timerecorder-${game}
mv list-laptimes.bat list-laptimes.sh
cp export-laptimes.bat export-laptimes.sh
# Reduce scripts to core parts
sed -i '1d;$d' *-laptimes.sh
popd