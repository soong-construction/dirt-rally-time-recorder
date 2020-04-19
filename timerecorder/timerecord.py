import asyncore
import os.path
import sys

# Cf. https://stackoverflow.com/a/45488820
try:
    from . import log, config  # @UnusedImport
    from .receiver import Receiver  # @UnusedImport
except (ImportError, ModuleNotFoundError):
    from timerecorder import log, config # @Reimport
    from timerecorder.receiver import Receiver  # @Reimport

if __name__ == '__main__':

    isBundled = getattr(sys, 'frozen', None)
    
    if isBundled:
        approot = os.path.dirname(sys.executable)
    else:
        approot = os.path.dirname(os.path.realpath(__file__))
        approot = os.path.dirname(approot) # Move to root
    
    log.init(approot + '/timerecord.log')
    config.init(approot + '/config.yml')

    receiver = Receiver(approot)
    receiver.reconnect()

    asyncore.loop()
