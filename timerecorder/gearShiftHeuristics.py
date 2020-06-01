from .log import getLogger
from .heuristics import Heuristics

is_h_pattern = lambda shift: shift == 'H-PATTERN'
REQUIRED_SHIFT_COUNT = 10

logger = getLogger(__name__)

class GearShiftHeuristics(Heuristics):

    def __init__(self, car_shift_list, gearTracker):
        Heuristics.__init__(self)
        self.car_shift_list = car_shift_list
        self.gearTracker = gearTracker

        select_match = lambda car_shift: is_h_pattern(car_shift[1])
        select_mismatch = lambda car_shift: not is_h_pattern(car_shift[1])

        self.cars_with_h_pattern_shifting = list(filter(select_match, self.car_shift_list))
        self.cars_without_h_pattern_shifting = list(filter(select_mismatch, self.car_shift_list))

    def isApplicable(self):
        sufficientData = self.gearTracker.getGearChangeCount() >= REQUIRED_SHIFT_COUNT
        canDiscriminate = len(self.car_shift_list) == 2 and len(self.cars_with_h_pattern_shifting) == 1

        applicable = sufficientData and canDiscriminate
        return applicable

    def apply(self):
        gearsWereSkipped = self.gearTracker.getGearSkipCount() > 0

        singleton_list = self.cars_with_h_pattern_shifting if gearsWereSkipped else self.cars_without_h_pattern_shifting

        (car, _) = singleton_list[0]

        return car
