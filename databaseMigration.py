# Steps:
# NOTE cannot migrate dirtrally-lb.db which is either shipped OR user configured for one of the supported games
# if user_version == 0:
# - migrate laptimes.db as per migrate.sql, ignore errors
# - set user_version = 2.1.0
# for each VERSION.sql in migrate/ with user_version < VERSION
# - run file
# - set user_version = VERSION
import sqlite3

class DatabaseMigration:
    
    # TODO #15 Duplicate
    laptimesDbName = 'dirtrally-laptimes.db'
    laptimesDb = '/' + laptimesDbName
    baseDb = '/dirtrally-lb.db'
    
    def __init__(self, approot):
        self.approot = approot
        self.db = None
    
    def setup(self):
        try:
            conn = sqlite3.connect(self.approot + self.baseDb)
            db = conn.cursor()
            self.db = db
        except (Exception) as exc:
            print("Error when reading from %s, please check set-up instructions in the README" % (self.baseDb))
            raise exc

    def getUserVersion(self):
        userVersion = self.db.execute('PRAGMA user_version;').fetchall()[0][0]
        return userVersion
    
    def setUserVersion(self, newVersion):
        self.db.execute('PRAGMA user_version = '+ str(newVersion))
