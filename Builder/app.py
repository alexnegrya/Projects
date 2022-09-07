from date_start_end import *
from tourist import *
from tour import *


if __name__ == '__main__':
    tour_1 = TourBuilder('Greece', 'Tour 1', [
            Tourist('John', 20), Tourist('Frank', 18)],
        Period('01.03.2021', '10.04.2021')
    ).with_ensurance().with_guide().build()
    print(tour_1)
else: print('This module using only separately')
