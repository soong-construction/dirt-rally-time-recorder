class AmbiguousResultHandler(object):
    
    def __init__(self):
        # TODO #9 This requires bundling sqlite3
        self.scriptTemplate = 'sqlite3 dirtrally-laptimes.db "%s"'
        pass

    # TODO #4 It would be nice to append the localtime, e.g. 11-32.bat
    def buildFileName(self, track, car, timestamp):
        return str(int(timestamp)) + '_' + track.replace(' ', '') + '_' + car.replace(' ', '') + '.bat'

    def buildScript(self, statement):
        return self.scriptTemplate % (statement, )

    def handleUpdateStatement(self, track, car, timestamp, updateStatement):
        
        fileName =self.buildFileName(track, car, timestamp)
        
        # TODO #4 Clean up: Remove <epoch-prefix>* files older than 7 days on start up 
        insertFile = open(file=fileName, mode='w', encoding='utf-8', newline='\n')
        insertFile.write(self.buildScript(updateStatement))
        
        return fileName
