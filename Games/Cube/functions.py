from os import system
from random import randint
from time import sleep

def clear(wait=None):
    if wait == None:
        system('clear')
    elif wait != None:
        from icons import watch
        input(f'\n{watch} Нажмите Enter чтобы продолжить... ')
        system('clear')

def is_type(t, variable):
    if type(variable) == t:
        return True
    else:
        raise TypeError('Неверный тип аргумента(ов)!')

class Check:
    def pos(self, y, x):
        if is_type(int, y) and is_type(int, x):
            from data import gm
            if y in range(0, 3) and x in range(0, gm.get_len()):
                pass
            else:
                raise ValueError('Недопустимые значения для координат!') 

    def lenght(self, lenght):
        if is_type(int, lenght):
            if lenght < 5:
                raise ValueError('Значение ниже минимально допустимого!')
    
    def number(self, number):
        if is_type(int, number):
            if number <= 0:
                raise ValueError('Номер должен быть больше нуля!')

    def gm(self, gm):
        from data import GameMap
        if is_type(GameMap, gm):
            pass
    
    def health(self, health):
        if health != None:
            if is_type(int, health):
                if health in range(0, 11):
                    pass
                else:
                    raise ValueError('Количество жизней не в рамках допустимых значений!')
    
    def damage(self, damage):
        if damage != None:
            if damage in range(0, 4):
                if is_type(int, damage):
                    pass
            else:
                raise ValueError('Урон не в рамках допустимых значений!')
    
    def obj(self, obj):
        from data import Obj
        if is_type(Obj, obj):
            pass
