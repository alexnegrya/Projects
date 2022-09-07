class FruitBox:
    def __init__(self, apples, oranges):
        self.apples = apples
        self.oranges = oranges
        if type(self.apples) != int or type(self.oranges) != int:
            print('Error: arguments must be int!')
        elif (self.apples + self.oranges) > 50:
                print('Error: max box capacity is 50!')

    def __add__(self, other_box):
        apples = self.apples + other_box.apples
        oranges = self.oranges + other_box.oranges
        new_box = FruitBox(apples, oranges)
        return new_box

    def __str__(self): return f"This fruit box contains {self.apples} apples\
 and {self.oranges} oranges."


if __name__ == '__main__':
    box1 = FruitBox(5, 10)
    box2 = FruitBox(10, 20)
    box3 = box1 + box2
    
    print('Box 1 ---', box1)
    print('Box 2 ---', box2)
    print('Box 1 + Box 2 ------', box1 + box2)
