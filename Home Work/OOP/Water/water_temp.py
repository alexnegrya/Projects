class Water:
    def __init__(self, volume=1, temp=18):
        self.volume = volume
        self.temp = temp

        if temp > 100:
            self.state = 'vapor'
        elif temp <= 0:
            self.state = 'solid'
        else:
            self.state = 'liquid'
        
    def __str__(self):
        return f"Water  {self.volume}L | {self.state} | {self.temp}C"


def heat(water, deltaTemp=0):
    return Water(water.volume, water.temp + deltaTemp)

def cool(water, deltaTemp=0):
    return Water(water.volume, water.temp - deltaTemp)


bucket_1 = Water()
bucket_1 = heat(bucket_1, 100)

bucket_2 = Water()
bucket_2 = cool(bucket_2, 100)

print(bucket_1)
print(bucket_2)
