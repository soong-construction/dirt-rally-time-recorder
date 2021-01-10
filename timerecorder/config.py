import os
import yaml
from .log import getLogger

logger = getLogger(__name__)
# Never import as identifier directly, as this has copy-by-value semantics
get = None

telemetry_server = 'telemetry_server'
host = 'host'
port = 'port'
speed_unit = 'speed_unit'
show_car_controls = 'show_car_controls'
keep_update_scripts_days = 'keep_update_scripts_days'
keep_update_scripts_days_default = 7

heuristics_settings = 'heuristics'
heuristics_activate = 'activate'
authentic_shifting = 'authentic_shifting'
user_signals = 'user_signals'

def readVersion(approot):
    with open(approot + '/VERSION', encoding='utf-8', newline='\n') as file:
        return file.readline().strip()
    
def init(filename):
    global get
    config = Config(filename)
    config.load()
    get = config

# After https://codereview.stackexchange.com/a/186672 by Graipher
class Config(dict):

    def readFromFile(self, filename):
        try:
            with open(filename, encoding='utf-8', newline='\n') as f:
                super(Config, self).update(yaml.load(f, yaml.SafeLoader) or {})
        except:
            raise IOError(os.path.basename(filename) + ' seems to be corrupt, please check or delete file.')

    def __init__(self, filename):
        self.filename = filename
        if os.path.isfile(filename):
            self.readFromFile(filename)
        
        self.migrate()

    def dump(self):
        with open(file=self.filename, mode='w', encoding='utf-8', newline='\n') as f:
            yaml.dump(self.copy(), f)

    def __setitem__(self, key, value):
        super(Config, self).__setitem__(key, value)
        self.dump()

    def __delitem__(self, key):
        super(Config, self).__delitem__(key)
        self.dump()

    def update(self, kwargs):
        super(Config, self).update(kwargs)
        self.dump()
    
    def setDefaultHeuristics(self):
        default_heuristics = {heuristics_activate: 0, authentic_shifting: 0, user_signals: 0}
        self.setdefault(heuristics_settings, default_heuristics)
        self[heuristics_settings].setdefault(heuristics_activate, default_heuristics[heuristics_activate])
        self[heuristics_settings].setdefault(authentic_shifting, default_heuristics[authentic_shifting])
        self[heuristics_settings].setdefault(user_signals, default_heuristics[user_signals])

    def migrate(self):
        default_server = {host:'127.0.0.1', port:20777}
        self.setdefault(telemetry_server, default_server)
        self[telemetry_server].setdefault(host, default_server[host])
        self[telemetry_server].setdefault(port, default_server[port])
        
        self.setdefault(speed_unit, 'kph')
        self.setdefault(show_car_controls, 1)
        self.setdefault(keep_update_scripts_days, keep_update_scripts_days_default)
        
        self.setDefaultHeuristics()
        self.dump()

    def loadBasicSettings(self):
        telemetry = self[telemetry_server]
        self.server = telemetry[host], int(telemetry[port])
        self.speed_unit = self[speed_unit]
        self.show_car_controls = int(self[show_car_controls])
        self.keep_update_scripts_days = int(self[keep_update_scripts_days])

    def loadHeuristics(self):
        heuristics = self[heuristics_settings]
        self.heuristics_activated = int(heuristics[heuristics_activate])
        self.authentic_shifting = int(heuristics[authentic_shifting])
        self.user_signals = int(heuristics[user_signals])
        
        if self.heuristics_activated:
            logger.info('HEURISTICS activated')

    def load(self):
        logger.debug('Loading config')
        file = os.path.basename(self.filename)

        try:
            self.loadBasicSettings()
            self.loadHeuristics()
            
        except Exception as e:
            logger.debug('Failed to load config file %s: %s', file, e)
            raise IOError(file + ' seems to be corrupt, please check or delete file.') from None
