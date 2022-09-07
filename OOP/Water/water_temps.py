from random import randint


class Water:
    def __init__(self, volume=1, temp=18):
        self.set_volume(volume)
        self.set_temp(temp)
        
    def __str__(self):
        return f"Water --- {self.__volume}L | {self.state} | {self.__temp}C"

    def __getattr__(self, name: str):
        if name == 'state':
            if self.__temp >= 100: return 'vapor'
            elif self.__temp <= 0: return 'solid'
            else: return 'liquid'
        else: return object.__getattribute__(self, name)
    
    def __temp_incorrect(self, temp): return temp > 2000 or temp < -273

    def __temp_error(self): print('Error: No such temperatures for water!')
    
    def set_temp(self, temp):
        if self.__temp_incorrect(temp): self.__temp_error
        else: self.__temp = temp
    
    def get_temp(self): return self.__temp
    
    def heat(self, temp: int):
        if self.__temp_incorrect(temp): self.__temp_error
        else: self.__temp += temp

    def cool(self, temp: int):
        if self.__temp_incorrect(temp): self.__temp_error
        else: self.__temp -= temp
    
    def set_volume(self, volume):
        if volume < 1: print('Error: minumum volume is 1L!')
        else: self.__volume = volume
    
    def get_volume(self): return self.__volume


if __name__ == '__main__':
    bucket_1 = Water(randint(1, 101))
    bucket_1.heat(randint(1, 101))

    bucket_2 = Water(randint(1, 101))
    bucket_2.cool(randint(1, 101))

    print(bucket_1)
    print(bucket_2)
