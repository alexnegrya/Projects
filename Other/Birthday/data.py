from os import system

class PersonBirthday:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year
    
    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    def day(self):
        return self.__day
    
    def month(self):
        return self.__month
    
    def year(self):
        return self.__year


def clear(wait=None):
    if wait != None:
        input('\nНажмите ENTER чтобы продолжить... ')
    system('clear')

def error(text):
    if type(text) != str:
        raise TypeError('Only string type supported!')
    else:
        clear()
        print(text)
        clear('')

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
