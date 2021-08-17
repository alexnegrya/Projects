from icons import *

# ############################# Data #############################
speed = 0.5 # Game speed
test = Check()
# ################################################################
class GameMap:
    
    def __init__(self, lenght):
        # Map generation
        __game_map = [
            [],
            [],
            []
        ]
        test.lenght(lenght)
        for __ap in range(lenght):
            __game_map[0].append(0)
            __game_map[1].append(0)
            __game_map[2].append(-1)
        self.__lenght = lenght
        self.__map = __game_map
    
    def __str__(self):
        return str(self.__map) 

    def get_len(self):
        return self.__lenght
    
    def draw(self):
        for y in range(len(self.__map)):
            for x in range(len(self.__map[y])):
                # Objects
                if self.__map[y][x] == character.get_number():
                    print(cube, end='')
                elif self.__map[y][x] == spike_1.get_number():
                    print(spike_down, end='')
                elif self.__map[y][x] == spike_2.get_number():
                    print(spike_up, end='')
                # Ground and emptiness
                elif self.__map[y][x] == -1:
                    print(ground, end='')
                else:
                    print(empty, end='')
            print()
    
    def set_obj(self, y, x, obj):
        test.pos(y, x)
        if is_type(int, obj):
            self.__map[y][x] = obj
        else:
            test.obj(obj)
            self.__map[y][x] = obj.get_number()
    
    def del_obj(self, y, x):
        test.pos(y, x)
        self.__map[y][x] = 0
    
    def update(self, gm):
        # Deleting the first map line
        character.move(gm, 'вправо')
        for __y in range(len(self.__map)):
            self.__map[__y].pop(0)
        # Genarating and adding second map line
        for __y in range(len(self.__map)):
            __r_up = randint(0, 1)
            __r_down = randint(0, 1)
            if __y == 0:
                if __r_up == 0:
                    self.__map[__y].append(__r_up)
                else:
                    self.__map[__y].append(spike_1.get_number())
            elif __y == 1:
                if __r_down == 0:
                    self.__map[__y].append(__r_down)
                else:
                    self.__map[__y].append(spike_2.get_number())
            else:
                self.__map[2].append(-1)

gm = GameMap(10)
lenght = gm.get_len()

class OptionError(Exception):
    pass

class Obj:
    def __init__(self, y, x, number, gm, damage=None, health=None):
        test.pos(y, x)
        self.__y = y
        self.__x = x
        if number <= 0:
            raise ValueError('Номер должен быть больше нуля!')
        else:
            self.__number = number
            if type(gm) == GameMap:
                gm.set_obj(y, x, number)
        if damage == None:
            self.__damage = None
        else:
            test.damage(damage)
            self.__damage = damage
        if health != None:
            self.__health = None
        else:
            test.health(health)
            self.__health = health

    def __str__(self):
        print('Координаты:')
        print(f'{point.get()} Y: {self.__y}')
        print(f'{point.get()} X: {self.__x}')
    
    def get_pos(self, pos):
        if is_type(str, pos):
            if pos == 'y':
                return self.__y
            elif pos == 'x':
                return self.__x
            elif pos == 'all':
                return [self.__y, self.__x]
            else:
                raise OptionError('Неизвестная опция!')
    
    def set_pos(self, y, x, gm):
        test.pos(y, x)
        test.gm(gm)
        self.__y = y
        self.__x = x
        gm.set_obj(y, x, self.__number)
    
    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        test.number(number)
        self.__number = number
    
    def move(self, gm, direction):
        test.gm(gm)
        if is_type(str, direction):
            no = False
            limit = False
            coord = self.get_pos('all')
            if direction == 'вверх':
                if self.__y != 0:
                    self.__y -= 1
                elif self.__y == 0:
                    limit = True
                else:
                    no = True
            elif direction == 'вниз':
                if self.__y != 1:
                    self.__y += 1
                elif self.__y == 1:
                    limit = True
                else:
                    no = True
            elif direction == 'влево':
                if self.__x != (lenght - lenght):
                    self.__x -= 1
                elif self.__x == lenght - lenght:
                    limit = True
                else:
                    no = True
            elif direction == 'вправо':
                if self.__x != (lenght - 1):
                    self.__x += 1
                elif self.__x == lenght - 1:
                    limit = True
                else:
                    no = True
            if no:
                raise OptionError('Неизвестная опция!')
            if limit == False:
                gm.del_obj(coord[0], coord[1])
                gm.set_obj(self.__y, self.__x, self.__number)
            else:
                self.__y = coord[0]
                self.__x = coord[1]

# ###################### Objects ######################
character = Obj(1, 0, 1, gm, health=3)
spike_1 = Obj(0, 3, 2, gm, damage=1)
spike_2 = Obj(1, 5, 3, gm, damage=1)
# #####################################################
