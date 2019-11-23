class AmbiguousResultHandler(object):
    
    def __init__(self, dbName):
        self.dbName = dbName
        self.scriptTemplate = 'sqlite3 %s "%s"'
        pass

    # TODO #8 It would be nice to append the localtime, e.g. 11-32.bat
    def buildFileName(self, track, car, timestamp):
        return str(int(timestamp)) + '_' + track.replace(' ', '') + '_' + car.replace(' ', '') + '.bat'

    def buildScript(self, statement):
        return self.scriptTemplate % (self.dbName, statement)

    def handleUpdateStatement(self, track, car, timestamp, updateStatement):
        
        fileName = self.buildFileName(track, car, timestamp)
        
        # TODO #8 Clean up: Remove <epoch-prefix>* files older than 7 days on start up 
        insertFile = open(file=fileName, mode='w', encoding='utf-8', newline='\n')
        insertFile.write(self.buildScript(updateStatement))
        
        return fileName
