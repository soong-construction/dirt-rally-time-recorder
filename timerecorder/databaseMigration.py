class DatabaseMigration:
    
    def __init__(self, lapDb):
        self.lapDb = lapDb
    
    def getUserVersion(self):
        userVersion = self.lapDb.execute('PRAGMA user_version;').fetchall()[0][0]
        return userVersion
    
    def setUserVersion(self, newVersion):
        self.lapDb.execute('PRAGMA user_version = '+ str(newVersion))
        
    def expandVersion(self, versionString):
        segments = versionString.split('.')
        if len(segments) != 3:
            raise RuntimeError('VERSION must match pattern X.Y.Z')
        segments = list(map(int, segments))
        return segments[0] * 10**6 + segments[1] * 10**3 + segments[2]
    
    def migrateDb(self):
        # Initial migration
        self.migrate_2_2_0()
        
        self.migrate('2.4.0', self.migrate_2_4_0)
    
    def migrate_2_2_0(self):
        self.migrate('2.2.0', lambda _: None)

    def migrate_2_4_0(self, lapDb):
        lapDb.execute('ALTER TABLE laptimes ADD COLUMN topspeed REAL DEFAULT NULL;')
    
    def migrate(self, targetVersionString, applicator):
        targetVersion = self.expandVersion(targetVersionString)
        user_version = self.getUserVersion()
        
        if user_version < targetVersion:
            applicator(self.lapDb)
            self.setUserVersion(targetVersion)
