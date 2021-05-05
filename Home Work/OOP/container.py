class Container:

    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second

    def __str__(self):
        if self.first != None and self.second != None:
            if self.first >= self.second:
                return f"[{self.first},{self.second}]"
            elif self.second >= self.first:
                return f"[{self.second},{self.first}]"
        elif self.first == None and self.second != None:
            return f"[{self.second}]"
        elif self.first != None and self.second == None:
            return f"[{self.first}]"
        else:
            return f"[]"

    def __eq__(self, other_container):
        if self.first == other_container.first and self.second == other_container.second:
            return True
        else:
            return False

c1 = Container()
c2 = Container(10)
c3 = Container(10, 100)

print(c1)
print(c2)
print(c3)
print(c2 == c3)
