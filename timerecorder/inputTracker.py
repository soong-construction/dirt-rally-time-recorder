from .log import getLogger
from enum import Enum

logger = getLogger(__name__)


class Signal(Enum):
    THROTTLE_LEFT = 1
    THROTTLE_RIGHT = 2
    
# Steer (left-neutral-right): -1.0..1.0
# Throttle (no-full): 0.0..1.0
class InputTracker():
    
    def __init__(self, speedTracker):
        self.speedTracker = speedTracker
        self.signal = None
        self.enabled = True

    def hasLaunched(self):
        return self.speedTracker.getTopSpeed() > 1.0

    def track(self, stats):
        throttle, steer = (stats[29:31])

        if not self.enabled:
            return
        
        if self.hasLaunched():
            self.enabled = False
            logger.debug('LAUNCHED')
            print('launched')
            return

        steering_offset = 0.2
        throttle_offset = 0.5
        if self.signal is not None and (throttle < steering_offset or steer > -steering_offset and steer < steering_offset):
            self.signal = None
            print('signal gone')

        if self.signal is not None:
            return
        
        if steer < -steering_offset and throttle > throttle_offset:
            self.signal = Signal.THROTTLE_LEFT
            print('engage throttle turning left')
            
        if steer > steering_offset and throttle > throttle_offset:
            self.signal = Signal.THROTTLE_RIGHT
            print('engage throttle turning right')
