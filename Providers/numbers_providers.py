from random import randint
from time import sleep


class NumbersProvider:
    def __init__(self, positive_action, negative_action, min=-100, max=100):
        self.positive_action = positive_action
        self.negative_action = negative_action
        if type(min) == int and type(max) == int:
            self.min = min
            self.max = max
        else: print('Error: values [min] and [max] must be integer!')

    def generate(self): return randint(self.min, self.max)

    def start(self):
        while True:
            number = self.generate()
            if number >= 0: self.positive_action(number)
            else: self.negative_action(number)
            sleep(1)
