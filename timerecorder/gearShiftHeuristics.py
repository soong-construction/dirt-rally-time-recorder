from .log import getLogger

is_h_pattern = lambda shift: shift == 'H-PATTERN'
REQUIRED_SHIFT_COUNT = 10

logger = getLogger(__name__)

class GearShiftHeuristics:
    
    def __init__(self, car_shift_list, gearTracker):
        self.car_shift_list = car_shift_list
        self.gearTracker = gearTracker
      
    def withFallback(self, heuristics):  
        self.fallback = heuristics
        
    def guessCar(self):
        select_match = lambda car_shift: is_h_pattern(car_shift[1])
        select_mismatch = lambda car_shift: not is_h_pattern(car_shift[1])

        cars_with_h_pattern_shifting = list(filter(select_match, self.car_shift_list))
        cars_without_h_pattern_shifting = list(filter(select_mismatch, self.car_shift_list))

        # TODO #25 Check for skipCount > M to account for missed Recovers?
        sufficientData = self.gearTracker.getGearChangeCount() >= REQUIRED_SHIFT_COUNT
        canDiscriminate = len(self.car_shift_list) == 2 and len(cars_with_h_pattern_shifting) == 1
        applicable = sufficientData and canDiscriminate

        if not applicable:
            logger.debug('GEAR HEURISTICS not applicable')
            return self.fallback and self.fallback.guessCar()

        gearsWereSkipped = self.gearTracker.getGearSkipCount() > 0

        singleton_list = cars_with_h_pattern_shifting if gearsWereSkipped else cars_without_h_pattern_shifting

        (car, _) = singleton_list[0]
        
        return car
