class Water:
    def __init__(self, volume=1, temp=18):
        self.set_volume(volume)
        self.set_temp(temp)
        
    def __str__(self):
        return f"Water  {self.__volume}L | {self.__state} | {self.__temp}C"
    
    def __temp_incorrect(self, temp):
        return temp > 2000 or temp < -273

    def __temp_error(self):
        print('Error: No such temperatures for water!')
    
    def __set_state(self, temp):
        if temp > 100:
            self.__state = 'vapor'
        elif temp <= 0:
            self.__state = 'solid'
        else:
            self.__state = 'liquid'

    def set_temp(self, temp):
        if self.__temp_incorrect(temp):
            self.__temp_error
        else:
            self.__temp = temp
            self.__set_state(temp)
    
    def get_temp(self):
        return self.__temp
    
    def add_temp(self, temp):
        if self.__temp_incorrect(temp):
            self.__temp_error
        else:
            self.__temp += temp
            self.__set_state(temp)

    def sub_temp(self, temp):
        if self.__temp_incorrect(temp):
            self.__temp_error
        else:
            self.__temp -= temp
            self.__set_state(temp)
    
    def set_volume(self, volume):
        if volume < 1:
            print('Error: minumum volume is 1L!')
        else:
            self.__volume = volume
    
    def get_volume(self):
        return self.__volume


def heat(water, deltaTemp=0):
    water.add_temp(deltaTemp)

def cool(water, deltaTemp=0):
    water.sub_temp(deltaTemp)


bucket_1 = Water()
heat(bucket_1, 100)

bucket_2 = Water()
cool(bucket_2, 100)

print(bucket_1)
print(bucket_2)
