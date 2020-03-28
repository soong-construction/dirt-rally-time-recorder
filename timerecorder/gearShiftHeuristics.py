from .log import getLogger

is_h_pattern = lambda shift: shift == 'H-PATTERN'

logger = getLogger(__name__)

# TODO #25 Test
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

        # TODO Check for shiftCount > N to ensure enough data
        # TODO Check for skipCount > M to account for missed Recovers
        applicable = len(self.car_shift_list) == 2 and len(cars_with_h_pattern_shifting) == 1

        if not applicable:
            logger.debug('GEAR HEURISTICS not applicable')
            return self.fallback and self.fallback.guessCar()

        gearsWereSkipped = self.gearTracker.getGearSkipCount() > 0

        singleton_list = cars_with_h_pattern_shifting if gearsWereSkipped else cars_without_h_pattern_shifting

        car, _ = singleton_list[0]
        
        return car
