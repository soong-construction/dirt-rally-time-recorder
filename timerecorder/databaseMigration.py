'''
Provides version-specific migration logic for existing databases
'''

class DatabaseMigration:

    def __init__(self, lapDb):
        self.lap_db = lapDb

    def getUserVersion(self):
        userVersion = self.lap_db.execute('PRAGMA user_version;').fetchall()[0][0]
        return userVersion

    def setUserVersion(self, newVersion):
        self.lap_db.execute(f'PRAGMA user_version = {newVersion}')

    def expandVersion(self, versionString):
        segments = versionString.split('.')
        if len(segments) != 3:
            raise RuntimeError('VERSION must match pattern X.Y.Z')
        segments = list(map(int, segments))
        return segments[0] * 10 ** 6 + segments[1] * 10 ** 3 + segments[2]

    def migrateDb(self):
        # Initial migration
        self._migrate_2_2_0()

        self._migrate('2.4.0', self._migrate_2_4_0)

    def _migrate_2_2_0(self):  #pylint: disable=invalid-name
        self._migrate('2.2.0', lambda _: None)

    def _migrate_2_4_0(self, lapDb):  #pylint: disable=invalid-name
        lapDb.execute('ALTER TABLE laptimes ADD COLUMN topspeed REAL DEFAULT NULL;')

    def _migrate(self, targetVersionString, applicator):
        targetVersion = self.expandVersion(targetVersionString)
        userVersion = self.getUserVersion()

        if userVersion < targetVersion:
            applicator(self.lap_db)
            self.setUserVersion(targetVersion)
