from random import randint
from time import sleep

class NumberProvider:
    def __init__(self, min=-100, max=100):
        if type(min) == int and type(max) == int:
            self.min = min
            self.max = max
        else:
            print('Error: values [min] and [max] must be integer!')

    def generate(self):
        return randint(self.min, self.max)

    def whenPositive(self, positiveCB):
        self.positiveCB = positiveCB

    def whenNegative(self, negativeCB):
        self.negativeCB = negativeCB

    def start(self):
        while True:
            number = self.generate()
            if number >= 0:
                self.positiveCB(number)
            else:
                self.negativeCB(number)
            sleep(1)
