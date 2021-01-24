'''
Manages update scripts necessary for resolution of ambiguous recordings
'''
import os
import time
import re
from datetime import datetime, timedelta
from _datetime import timezone
from .log import getLogger
from . import config

SCRIPT_REGEX = r"(\d{9,10})_\S+_\S+\.bat"
SCRIPT_TEMPLATE = 'sqlite3 {} "{}"'

logger = getLogger(__name__)

def isUpdateScript(file):
    return re.match(SCRIPT_REGEX, file)

class UpdateScriptHandler():

    def __init__(self, dbName):
        self.db_name = dbName

    def _buildFileName(self, track, car, timestamp):
        return '{}_{}_{}.bat'.format(int(timestamp), track.replace(' ', ''), car.replace(' ', ''))

    def _buildScript(self, statement):
        return SCRIPT_TEMPLATE.format(self.db_name, statement)

    def writeScript(self, track, car, timestamp, updateStatement):

        fileName = self._buildFileName(track, car, timestamp)

        insertFile = open(file=fileName, mode='w', encoding='utf-8', newline='\n')
        insertFile.write(self._buildScript(updateStatement))

        return fileName

    def _listUpdateScripts(self, directory):
        fileList = os.listdir(directory)
        return [directory + '/' + file for file in fileList if isUpdateScript(file)]

    def _isBeforeDeadline(self, _datetime, keepForDays, script):
        matches = re.finditer(SCRIPT_REGEX, script)
        match = next(matches)

        deadline = _datetime - timedelta(days=keepForDays)

        creationTimestamp = int(match.group(1))
        creationTime = _datetime.fromtimestamp(creationTimestamp, timezone.utc)

        return creationTime < deadline

    def _warnShortRetentionTime(self):
        return logger.warning(
            ('CAUTION: Keeping update scripts for less than %s days. '
                'Follow possible hints to update scripts directly after your session.'), config.KEEP_UPDATE_SCRIPTS_DAYS_DEFAULT)

    def _listOldUpdateScripts(self, _time, directory):
        keepForDays = config.GET.keep_update_scripts_days
        if keepForDays < config.KEEP_UPDATE_SCRIPTS_DAYS_DEFAULT:
            self._warnShortRetentionTime()

        scripts = self._listUpdateScripts(directory)

        oldScripts = filter(lambda script: self._isBeforeDeadline(_time, keepForDays, script), scripts)

        return list(oldScripts)

    def _delete(self, file):
        os.remove(file)

    def cleanUp(self, directory):
        logger.debug('Cleaning up update scripts...')
        now = datetime.fromtimestamp(time.time(), timezone.utc)
        for file in self._listOldUpdateScripts(now, directory):
            logger.debug('Deleting %s', os.path.basename(file))
            self._delete(file)
