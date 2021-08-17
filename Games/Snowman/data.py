from random import randint
from os import system
from time import sleep

# Map
gm = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

class Obj:
    def __init__(self, gm, obj_number, y, x):
        if self.__is_y(y):
            if self.__is_x(x):
                if obj_number > 0:
                    self.__y = y
                    self.__x = x
                    self.__number = obj_number
                    gm[self.__y][self.__x] = self.__number
                else:
                    print('Номер объекта должен быть больше нуля!')
    
    def __is_y(self, y):
        if y in range(0, 10):
            return True
        else:
            print('Неправильная Y координата!')
    
    def __is_x(self, x):
        if x in range(0, 10):
            return True
        else:
            print('Неправильная X координата!')

    def set_coord(self, gm, y=None, x=None, direction=None):
        if is_none(y) and is_none(x):
            if self.__is_y(y):
                if self.__is_x(x):
                    gm[y][x] = self.__number
        elif is_none(direction):
            if is_type('str', direction):
                if direction == 'влево':
                    if self.__x != 0:
                        self.__x -= 1
                        gm[self.__y][self.__x] = self.__number
                    else:
                        self.__x = 0
                        gm[self.__y][self.__x] = self.__number
                elif direction == 'вправо':
                    if self.__x != 9:
                        self.__x += 1
                        gm[self.__y][self.__x] = self.__number
                    else:
                        self.__x = 9
                        gm[self.__y][self.__x] = self.__number
                elif direction == 'вверх':
                    if self.__y != 0:
                        self.__y -= 1
                        gm[self.__y][self.__x] = self.__number
                    else:
                        self.__y = 0
                        gm[self.__y][self.__x] = self.__number
                elif direction == 'вниз':
                    if self.__y != 9:
                        self.__y += 1
                        gm[self.__y][self.__x] = self.__number
                    else:
                        self.__y = 9
                        gm[self.__y][self.__x] = self.__number
                else:
                    print('Напишите правильное направление! (влево/вправо/вверх/вниз)')
            else:
                print('Напишите правильное направление! (влево/вправо/вверх/вниз)')
        else:
            print('Укажите координаты или направление!')
    
    def del_coord(self, gm, mine=None):
        gm[self.__y][self.__x] = 0
        if is_none(mine):
            self.__y = 10
            self.__x = 10

    def get_coord(self):
        return [self.__y, self.__x]

    def set_hp(self, hp=None, op=None):
        if is_none(hp):
            if is_type('int', hp):
                self.__hp = hp
            else:
                print('Колличество жизней должно быть целым числовым значением!')
        elif is_none(op):
            if is_type('str', op):
                if op == 'add':
                    self.__hp += 1
                elif op == 'sub':
                    self.__hp -= 1
            else:
                print('Недопустимая операция!')
    
    def get_hp(self):
        return self.__hp
    
    def __eq__(self, other):
        if self.__y == other.__y and\
        self.__x == other.__x:
            return True
        else:
            return False

class Interactive(Obj):
    def __init__(self):
        pass
    def action(self):
        return input(f"\n{cursor.get()} ")

class Icon:
    def __init__(self, icon):
        if is_type('str', icon):
            self.__icon = icon
        else:
            print('Иконка передана в неверном формате!')
    
    def set(self, icon):
        if is_type('str', icon):
            self.__icon = icon
        else:
            print('Иконка передана в неверном формате!')
    
    def get(self):
        return self.__icon

def clear(wait=None):
    if wait == None: 
        system('clear')
    elif wait != None:
        input(f'\n{watch.get()} Нажмите Enter чтобы продолжить... ')
        system('clear')

def print_hp(variable):
    hp = variable.get_hp()
    if hp != 0:
        for i in range(hp):
            print(heart.get(), end=' ')
        print()

def is_type(t, variable):
    if type(t) == str:
        if t == 'str':
            if type(variable) == str:
                return True
            else:
                return False
        elif t == 'int':
            if type(variable) == int:
                return True
            else:
                return False
        elif t == 'float':
            if type(variable) == float:
                return True
            else:
                return False
        else:
            print(f'{cross.get()} Неизвестный тип данных!')
    else:
        print(f'{cross.get()} Проверяемый тип данных указан в неверном формате!')

def is_none(variable):
    if variable != None:
        return True
    else:
        return False

# Objects
snowman = Obj(gm, 1, randint(0, 9), randint(0, 9))
mine_1 = Obj(gm, 2, randint(0, 9), randint(0, 9))
mine_2 = Obj(gm, 3, randint(0, 9), randint(0, 9))
mine_3 = Obj(gm, 4, randint(0, 9), randint(0, 9))
m_1 = True
m_2 = True
m_3 = True
mines = [mine_1, mine_2, mine_3]

# Set HP
snowman.set_hp(3)

# Interactive
option = Interactive()
ru = ['ф', 'в', 'ц', 'ы']

# Icons
character = Icon('☃')
mine = Icon('☠')
land = Icon('●')
heart = Icon('♥')
cursor = Icon('▶')
skull = Icon('💀')
cross = Icon('❌')
watch = Icon('🕐')
