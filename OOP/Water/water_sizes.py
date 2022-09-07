class Water:
    def __init__(self, volume=0):
        if type(volume) == int or type(volume) == float: self.volume = volume
        elif type(volume) == str \
          and self.is_str_volume(volume):
            if volume == 'large': self.volume = 1000
            elif volume == 'medium': self.volume = 100
            elif volume == 'small': self.volume = 10
        else: print('Error: Wrong volume value!')
    
    def __str__(self): return f"{self.size[0].upper() + self.size[1:]}" + \
        f" water --- {self.volume}L"

    def __setattr__(self, name: str, value) -> None:
        if name == 'volume':
            if value == 0: size = 'empty'
            elif value <= 10: size = 'small'
            elif value <= 100: size = 'medium'
            elif value <= 1000: size = 'large'
            object.__setattr__(self, 'size', size)
        object.__setattr__(self, name, value)
    
    def is_number(self, value): return type(value) == int or \
        type(value) == float
    
    def is_str_volume(self, var):
        return var in ['large', 'medium', 'small']

    def __len__(self): return self.volume

    def __gt__(self, other):
        if self.is_number(other): return self.volume > other
        else: return self.volume > other.volume
    
    def __ge__(self, other):
        if self.is_number(other): return self.volume >= other
        else: return self.volume >= other.volume
    
    def __lt__(self, other):
        if self.is_number(other): return self.volume < other
        else: return self.volume < other.volume
    
    def __le__(self, other):
        if self.is_number(other): return self.volume <= other
        else: return self.volume <= other.volume
    
    def __eq__(self, other):
        if self.is_number(other): return self.volume == other
        else: return self.volume == other.volume
    
    def __ne__(self, other):
        if self.is_number(other): return self.volume != other
        else: return self.volume != other.volume
    
    def __add__(self, other): return Water(self.volume + other.volume)


if __name__ == '__main__':
    empty_water = Water()
    large_water = Water('large')
    medium_water = Water('medium')
    small_water = Water('small')

    print(empty_water)
    print(large_water)
    print(medium_water)
    print(small_water)
    print('Large > medium:', large_water > medium_water)   # True
    print('Small < medium:', small_water < medium_water)   # True
    print('Large >= medium:', large_water >= medium_water)  # True
    print('Small <= medium:', small_water <= medium_water)  # True
    print('Large == small:', large_water == small_water)   # False
    print('Medium != medium:', medium_water != medium_water) # False
