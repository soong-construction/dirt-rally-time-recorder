import asyncore
import os.path
import sys
import yaml

# Cf. https://stackoverflow.com/a/45488820
try:
    from .receiver import Receiver  # @UnusedImport
    from . import log  # @UnusedImport
except (ImportError, ModuleNotFoundError):
    from timerecorder.receiver import Receiver  # @Reimport
    from timerecorder import log # @Reimport

if __name__ == '__main__':

    isBundled = getattr(sys, 'frozen', None)
    
    if isBundled:
        approot = os.path.dirname(sys.executable)
    else:
        approot = os.path.dirname(os.path.realpath(__file__))
        approot = os.path.dirname(approot) # Move to root
    
    log.init(approot + '/timerecord.log')
    logger = log.getLogger('timerecorder.timerecord')

    logger.debug('Loading config')
    try:
        config = yaml.load(open(approot + '/config.yml', 'r'), yaml.SafeLoader)
    except (yaml.YAMLError) as exc:
        logger.exception("Error when loading configuration")

    server = (config['telemetry_server']['host'], config['telemetry_server']['port'])
    speed_unit = config['speed_unit']

    receiver = Receiver(server, speed_unit, approot)
    receiver.reconnect()

    asyncore.loop()
