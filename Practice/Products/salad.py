class Salad:
    __ingredients = []

    def __init__(self, name, ingredient_1, ingredient_2):
        if is_type('str', name):
            self.name = name
        else:
            print('Wrong salad name!')
        if is_type('str', ingredient_1):
            self.__ing_1 = ingredient_1
        else:
            print('Wrong first ingredient!')
        if is_type('str', ingredient_2):
            self.__ing_2 = ingredient_2
        else:
            print('Wrong second ingredient!')
    
    def add_ing(self, ingredient):
        if is_type('str', ingredient):
            pass


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
            print('Unknown type!')
    else:
        print('The type to check is specified incorrectly!')
