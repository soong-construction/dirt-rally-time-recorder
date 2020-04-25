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

logfile = 'timerecord.log'
homepage = 'https://github.com/soong-construction/dirt-rally-time-recorder'

def informUser():
    input('Press ENTER to end program.')

def main(logfile):
    try:
        isBundled = getattr(sys, 'frozen', None)
        if isBundled:
            approot = os.path.dirname(sys.executable)
        else:
            approot = os.path.dirname(os.path.realpath(__file__))
            approot = os.path.dirname(approot) # Move to root
        
        log.init(approot + '/' + logfile)
        config.init(approot + '/config.yml')
        
        receiver = Receiver(approot)
        receiver.reconnect()
        
        asyncore.loop()
        
    except:
        logger = log.getLogger('timerecorder.timerecord')
        logger.exception('Unfortunately, timerecord crashed. Look at %s for help', homepage)
        informUser()

if __name__ == '__main__':
    main(logfile)
