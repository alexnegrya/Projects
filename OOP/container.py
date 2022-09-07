class Container:
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second
        if first > second:
            self.first = second
            self.second = first

    def __str__(self):
        if self.first != 0 and self.second != 0:
            return f"[{self.first}, {self.second}]"
        elif self.first == 0 and self.second != 0: return f"[{self.second}]"
        elif self.first != 0 and self.second == 0: return f"[{self.first}]"
        else: return '[]'

    def __eq__(self, other):
        return self.first == other.first and self.second == other.second


if __name__ == '__main__':
    c1 = Container()
    c2 = Container(10)
    c3 = Container(10, 100)
    c4 = Container(100, 10)

    print(c1)
    print(c2)
    print(c3)
    print(c4)
    print('3 == 4:', c3 == c4)
