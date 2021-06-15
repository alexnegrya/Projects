from date_start_end import *
from tourist import *
from tour import *

tour_1 = TourBuilder('Greece', 'Tour 1', [Tourist('John', 20), Tourist('Frank', 18)], Period('01.03.2021', '10.04.2021'))\
    .withEnsurance().withGuide().build()

print(tour_1)