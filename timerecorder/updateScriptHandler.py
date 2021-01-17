import os
import time
import re
from datetime import datetime, timedelta
from _datetime import timezone
from .log import getLogger
from . import config

scriptRegex = r"(\d{9,10})_\S+_\S+\.bat"
scriptTemplate = 'sqlite3 {} "{}"'

logger = getLogger(__name__)

def isUpdateScript(file):
    return re.match(scriptRegex, file)

class UpdateScriptHandler():

    def __init__(self, dbName):
        self.dbName = dbName

    def _buildFileName(self, track, car, timestamp):
        return '{}_{}_{}.bat'.format(int(timestamp), track.replace(' ', ''), car.replace(' ', ''))

    def _buildScript(self, statement):
        return scriptTemplate.format(self.dbName, statement)

    def writeScript(self, track, car, timestamp, updateStatement):

        fileName = self._buildFileName(track, car, timestamp)

        insertFile = open(file=fileName, mode='w', encoding='utf-8', newline='\n')
        insertFile.write(self._buildScript(updateStatement))

        return fileName

    def _listUpdateScripts(self, directory):
        file_list = os.listdir(directory)
        return [directory + '/' + file for file in file_list if isUpdateScript(file)]

    def _isBeforeDeadline(self, datetime, keep_for_days, script):
        matches = re.finditer(scriptRegex, script)
        match = next(matches)

        deadline = datetime - timedelta(days = keep_for_days)

        creation_timestamp = int(match.group(1))
        creation_time = datetime.fromtimestamp(creation_timestamp, timezone.utc)


        return creation_time < deadline

    def _warnShortRetentionTime(self):
        return logger.warning(
            ('CAUTION: Keeping update scripts for less than %s days. '
                'Follow possible hints to update scripts directly after your session.'), config.KEEP_UPDATE_SCRIPTS_DAYS_DEFAULT)

    def _listOldUpdateScripts(self, time, directory):
        keep_for_days = config.GET.keep_update_scripts_days
        if keep_for_days < config.KEEP_UPDATE_SCRIPTS_DAYS_DEFAULT:
            self._warnShortRetentionTime()

        scripts = self._listUpdateScripts(directory)

        old_scripts = filter(lambda script: self._isBeforeDeadline(time, keep_for_days, script), scripts)

        return list(old_scripts)

    def _delete(self, file):
        os.remove(file)

    def cleanUp(self, directory):
        logger.debug('Cleaning up update scripts...')
        now = datetime.fromtimestamp(time.time(), timezone.utc)
        for file in self._listOldUpdateScripts(now, directory):
            logger.debug('Deleting %s', os.path.basename(file))
            self._delete(file)
