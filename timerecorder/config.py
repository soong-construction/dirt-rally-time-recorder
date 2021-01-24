'''
Generates and parses config.yml and provides dict-like access to it
'''
import os
import yaml
from .log import getLogger

logger = getLogger(__name__)
# Never import as identifier directly, as this has copy-by-value semantics
GET = None

SPEED_UNIT = 'speed_unit'
SHOW_CAR_CONTROLS = 'show_car_controls'
KEEP_UPDATE_SCRIPTS_DAYS = 'keep_update_scripts_days'
KEEP_UPDATE_SCRIPTS_DAYS_DEFAULT = 7

HEURISTICS_SETTINGS = 'heuristics'
HEURISTICS_ACTIVATE = 'activate'
AUTHENTIC_SHIFTING = 'authentic_shifting'
USER_SIGNALS = 'user_signals'

TELEMETRY_SERVER = 'telemetry_server'
HOST = 'host'
PORT = 'port'

def readVersion(approot):
    with open(approot + '/VERSION', encoding='utf-8', newline='\n') as file:
        return file.readline().strip()

def init(filename):
    global GET  #pylint: disable=global-statement
    config = Config(filename)
    config.load()
    GET = config

# After https://codereview.stackexchange.com/a/186672 by Graipher
class Config(dict):  #pylint: disable=too-many-instance-attributes

    def readFromFile(self, filename):
        try:
            with open(filename, encoding='utf-8', newline='\n') as file:
                super().update(yaml.load(file, yaml.SafeLoader) or {})
        except:
            raise IOError(f'{os.path.basename(filename)} seems to be corrupt, please check or delete file.')  #pylint: disable=raise-missing-from

    def __init__(self, filename):  #pylint: disable=super-init-not-called
        self.filename = filename
        if os.path.isfile(filename):
            self.readFromFile(filename)

        self.server = None
        self.speed_unit = None
        self.show_car_controls = None
        self.keep_update_scripts_days = None

        self.heuristics_activated = None
        self.authentic_shifting = None
        self.user_signals = None

        self._migrate()

    def dump(self):
        with open(file=self.filename, mode='w', encoding='utf-8', newline='\n') as file:
            yaml.dump(self.copy(), file)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.dump()

    def __delitem__(self, key):
        super().__delitem__(key)
        self.dump()

    def update(self, kwargs):
        super().update(kwargs)
        self.dump()

    def _setDefaultHeuristics(self):
        defaultHeuristics = {HEURISTICS_ACTIVATE: 0, AUTHENTIC_SHIFTING: 0, USER_SIGNALS: 0}
        self.setdefault(HEURISTICS_SETTINGS, defaultHeuristics)
        self[HEURISTICS_SETTINGS].setdefault(HEURISTICS_ACTIVATE, defaultHeuristics[HEURISTICS_ACTIVATE])
        self[HEURISTICS_SETTINGS].setdefault(AUTHENTIC_SHIFTING, defaultHeuristics[AUTHENTIC_SHIFTING])
        self[HEURISTICS_SETTINGS].setdefault(USER_SIGNALS, defaultHeuristics[USER_SIGNALS])

    def _migrate(self):
        defaultServer = {HOST:'127.0.0.1', PORT:20777}
        self.setdefault(TELEMETRY_SERVER, defaultServer)
        self[TELEMETRY_SERVER].setdefault(HOST, defaultServer[HOST])
        self[TELEMETRY_SERVER].setdefault(PORT, defaultServer[PORT])

        self.setdefault(SPEED_UNIT, 'kph')
        self.setdefault(SHOW_CAR_CONTROLS, 1)
        self.setdefault(KEEP_UPDATE_SCRIPTS_DAYS, KEEP_UPDATE_SCRIPTS_DAYS_DEFAULT)

        self._setDefaultHeuristics()
        self.dump()

    def _loadBasicSettings(self):
        telemetry = self[TELEMETRY_SERVER]
        self.server = telemetry[HOST], int(telemetry[PORT])
        self.speed_unit = self[SPEED_UNIT]
        self.show_car_controls = int(self[SHOW_CAR_CONTROLS])
        self.keep_update_scripts_days = int(self[KEEP_UPDATE_SCRIPTS_DAYS])

    def _loadHeuristics(self):
        heuristics = self[HEURISTICS_SETTINGS]
        self.heuristics_activated = int(heuristics[HEURISTICS_ACTIVATE])
        self.authentic_shifting = int(heuristics[AUTHENTIC_SHIFTING])
        self.user_signals = int(heuristics[USER_SIGNALS])

        if self.heuristics_activated:
            logger.info('HEURISTICS activated')

    def load(self):
        logger.debug('Loading config')
        file = os.path.basename(self.filename)

        try:
            self._loadBasicSettings()
            self._loadHeuristics()

        except Exception as ex:
            logger.debug('Failed to load config file %s: %s', file, ex)
            raise IOError(f'{file} seems to be corrupt, please check or delete file.') from None
