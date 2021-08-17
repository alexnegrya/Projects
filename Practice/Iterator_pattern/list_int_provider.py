from random import randint

class RandomIntProvider:
    def __init__(self, amount):
        if type(amount) == int:
            if amount > 0:
                self.__amount = amount
            else:
                raise ValueError('amount must be greater then 0')
        else:
            raise TypeError('amount must be integer')
        self.__numbers = []
        while len(self.__numbers) <= self.__amount - 1:
            self.__numbers.append(randint(1, 10))
        self.__index = 0
    
    def __str__(self):
        return str(self.__numbers)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == len(self):
            raise StopIteration
        else:
            out = self.__numbers[self.__index]
            self.__index += 1
            return out
    
    def __len__(self):
        return len(self.__numbers)
    
    def __setitem__(self, key, value):
        self.__numbers[key] = value

    def __getitem__(self, key):
        return self.__numbers[key]