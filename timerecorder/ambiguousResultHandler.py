import re
from datetime import datetime, timedelta
from _datetime import timezone
import time
from .log import getLogger
import os

scriptRegex = r"(\d{9,10})_\S+_\S+\.bat"
scriptTemplate = 'sqlite3 %s "%s"'

logger = getLogger(__name__)

class AmbiguousResultHandler(object):

    def __init__(self, dbName):
        self.dbName = dbName
        pass

    def buildFileName(self, track, car, timestamp):
        return str(int(timestamp)) + '_' + track.replace(' ', '') + '_' + car.replace(' ', '') + '.bat'

    def buildScript(self, statement):
        return scriptTemplate % (self.dbName, statement)

    def handleUpdateStatement(self, track, car, timestamp, updateStatement):

        fileName = self.buildFileName(track, car, timestamp)

        insertFile = open(file=fileName, mode='w', encoding='utf-8', newline='\n')
        insertFile.write(self.buildScript(updateStatement))

        return fileName

    def listUpdateScripts(self, directory):
        file_list = os.listdir(directory)
        return [directory + '/' + file for file in file_list if re.match(scriptRegex, file)]

    def isBeforeDeadline(self, time, script):
        matches = re.finditer(scriptRegex, script)
        match = next(matches)
        
        creation_timestamp = int(match.group(1))
        creation_time = datetime.fromtimestamp(creation_timestamp, timezone.utc)
        deadline = time - timedelta(days = 7)

        return creation_time < deadline

    def listOldUpdateScripts(self, time, directory):
        scripts = self.listUpdateScripts(directory)

        old_scripts = filter(lambda script: self.isBeforeDeadline(time, script), scripts)

        return list(old_scripts)

    def delete(self, file):
        os.remove(file)

    def cleanUp(self, directory):
        logger.debug('Cleaning up update scripts...')
        now = datetime.fromtimestamp(time.time(), timezone.utc)
        for file in self.listOldUpdateScripts(now, directory):
            logger.debug('Deleting %s', os.path.basename(file))
            self.delete(file)
