import asyncore
import os.path
import sys
import yaml

try:
    from .receiver import Receiver  # @UnusedImport
    from .log import getLogger  # @UnusedImport
except ModuleNotFoundError:
    from timerecorder.receiver import Receiver  # @Reimport
    from timerecorder.log import getLogger  # @Reimport

logger = getLogger(__name__)

if __name__ == '__main__':

    # TODO Is this condition the difference between the distributable and the dev version?
    if getattr(sys, 'frozen', None):
        approot = os.path.dirname(sys.executable)
    else:
        approot = os.path.dirname(os.path.realpath(__file__))
        approot = os.path.dirname(approot) # Move to root
    try:
        config = yaml.load(open(approot + '/config.yml', 'r'), yaml.SafeLoader)
    except (yaml.YAMLError) as exc:
        logger.exception("Error when loading configuration")

    server = (config['telemetry_server']['host'], config['telemetry_server']['port'])
    speed_unit = config['speed_unit']

    receiver = Receiver(server, speed_unit, approot)
    receiver.reconnect()

    asyncore.loop()
