import asyncore
import os.path
import sys

import yaml
from receiver import Receiver
from log import getLogger

if __name__ == '__main__':

    logger = getLogger(__name__)
    
    if getattr(sys, 'frozen', None):
        approot = os.path.dirname(sys.executable)
    else:
        approot = os.path.dirname(os.path.realpath(__file__))

    try:
        config = yaml.load(open(approot + '/config.yml', 'r'), yaml.SafeLoader)
    except (yaml.YAMLError) as exc:
        logger.exception("Error when loading configuration")

    server = (config['telemetry_server']['host'], config['telemetry_server']['port'])
    speed_unit = config['speed_unit']

    receiver = Receiver(server, speed_unit, approot)
    receiver.reconnect()

    asyncore.loop()
