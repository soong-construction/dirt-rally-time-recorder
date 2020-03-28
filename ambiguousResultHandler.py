class AmbiguousResultHandler(object):
    
    def __init__(self, dbName):
        self.dbName = dbName
        self.scriptTemplate = 'sqlite3 %s "%s"'
        pass

    def buildFileName(self, track, car, timestamp):
        return str(int(timestamp)) + '_' + track.replace(' ', '') + '_' + car.replace(' ', '') + '.bat'

    def buildScript(self, statement):
        return self.scriptTemplate % (self.dbName, statement)

    def handleUpdateStatement(self, track, car, timestamp, updateStatement):
        
        fileName = self.buildFileName(track, car, timestamp)
        
        # TODO #22 Clean up: Remove <epoch-prefix>* files older than 7 days on start up 
        insertFile = open(file=fileName, mode='w', encoding='utf-8', newline='\n')
        insertFile.write(self.buildScript(updateStatement))
        
        return fileName
