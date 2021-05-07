class Water:
    def __init__(self, volume=0):
        if type(volume) == int or type(volume) == float:
            self.volume = volume
        elif type(volume) == str\
            and self.isVolumeStr(volume):
                if volume == 'large':
                    self.volume = 1000
                elif volume == 'medium':
                    self.volume = 100
                elif volume == 'small':
                    self.volume = 10
        else:
            print('Error: Wrong volume value!')
    
    def __str__(self):
        return f"Water <{self.volume}>"
    
    def isNumber(self, value):
        return type(value) == int or type(value) == float
    
    def isVolumeStr(self, variable):
        return variable in ['large', 'medium', 'small']

    def __len__(self):
        return self.volume

    def __gt__(self, other):
        if self.isNumber(other):
            return self.volume > other
        else:
            return self.volume > other.volume
    
    def __ge__(self, other):
        if self.isNumber(other):
            return self.volume >= other
        else:
            return self.volume >= other.volume
    
    def __lt__(self, other):
        if self.isNumber(other):
            return self.volume < other
        else:
            return self.volume < other.volume
    
    def __le__(self, other):
        if self.isNumber(other):
            return self.volume <= other
        else:
            return self.volume <= other.volume
    
    def __eq__(self, other):
        if self.isNumber(other):
            return self.volume == other
        else:
            return self.volume == other.volume
    
    def __ne__(self, other):
        if self.isNumber(other):
            return self.volume != other
        else:
            return self.volume != other.volume
    
    def __add__(self, other):
        return Water(self.volume + other.volume)


emptyWater = Water()
largeWater = Water('large')
mediumWater = Water('medium')
smallWater = Water('small')

print(largeWater)
print(mediumWater)
print(smallWater)
print(largeWater > mediumWater)   # True
print(smallWater < mediumWater)   # True
print(largeWater >= mediumWater)  # True
print(smallWater <= mediumWater)  # True
print(largeWater == smallWater)   # False
print(mediumWater != mediumWater) # False
