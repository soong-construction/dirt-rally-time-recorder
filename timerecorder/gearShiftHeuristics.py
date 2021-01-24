'''
Heuristics based on shifting, cf. docs
'''
from .log import getLogger
from .heuristics import Heuristics

is_h_pattern = lambda shift: shift == 'H-PATTERN'
REQUIRED_SHIFT_COUNT = 10

logger = getLogger(__name__)

class GearShiftHeuristics(Heuristics):

    def __init__(self, carShiftList, gearTracker):
        Heuristics.__init__(self)
        self.car_shift_list = carShiftList
        self.gear_tracker = gearTracker

        selectMatch = lambda car_shift: is_h_pattern(car_shift[1])
        selectMismatch = lambda car_shift: not is_h_pattern(car_shift[1])

        self.cars_with_h_pattern_shifting = list(filter(selectMatch, self.car_shift_list))
        self.cars_without_h_pattern_shifting = list(filter(selectMismatch, self.car_shift_list))

    def isApplicable(self):
        sufficientData = self.gear_tracker.getGearChangeCount() >= REQUIRED_SHIFT_COUNT
        canDiscriminate = len(self.car_shift_list) == 2 and len(self.cars_with_h_pattern_shifting) == 1

        applicable = sufficientData and canDiscriminate
        return applicable

    def apply(self):
        gearsWereSkipped = self.gear_tracker.getGearSkipCount() > 0

        singletonList = self.cars_with_h_pattern_shifting if gearsWereSkipped else self.cars_without_h_pattern_shifting

        (car, _) = singletonList[0]

        return car
