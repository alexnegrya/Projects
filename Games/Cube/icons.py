from functions import *

class Icon:
    def __init__(self, icon):
        if is_type(str, icon):
            self.__icon = icon

    def __str__(self):
        return self.get()

    def set(self, icon):
        if is_type(str, icon):
            self.__icon = icon

    def get(self, quantity=None):
        if quantity != None:
            if is_type(int, quantity):
                if quantity > 1:
                    return (self.__icon * quantity)
                elif quantity == 1:
                    raise ValueError('Для передачи одной иконки не надо указывать аргумент!')
                else:
                    raise ValueError('Недопустимое количество!')
        else:
            return self.__icon

# Character
cube = Icon('▣')

# Spikes
spike_up = Icon('▲')
spike_down = Icon('▼')

# Emptiness
empty = Icon(' ')

# Ground
ground = Icon('=')

# Cross
cross = Icon('❌')

# Watch
watch = Icon('🕐')

# Black circle
point = Icon('●')
