from .log import getLogger
import yaml
import os

logger = getLogger(__name__)
# Never import as identifier directly, as this has copy-by-value semantics
get = None

telemetry_server = 'telemetry_server'
host = 'host'
port = 'port'
speed_unit = 'speed_unit'
heuristicsMode = 'heuristics_mode'

def readVersion(approot):
    with open(approot + '/VERSION', encoding='utf-8', newline='\n') as file:
        return file.readline().strip()
    
# TODO #25 Update docs
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
    
    def migrate(self):
        default_server = {host:'127.0.0.1', port:20777}
        self.setdefault(telemetry_server, default_server)
        self[telemetry_server].setdefault(host, default_server[host])
        self[telemetry_server].setdefault(port, default_server[port])
        
        self.setdefault(speed_unit, 'kph')
        self.setdefault(heuristicsMode, 0)
        self.dump()
        
    def load(self):
        logger.debug('Loading config')
        file = os.path.basename(self.filename)

        try:
            telemetry = self[telemetry_server]
            self.server = (telemetry[host], int(telemetry[port]))
            self.speed_unit = self[speed_unit]
            self.heuristicsMode = int(self[heuristicsMode])
        except Exception as e:
            logger.debug('Failed to load config file %s: %s', file, e)
            raise IOError(file + ' seems to be corrupt, please check or delete file.') from None
