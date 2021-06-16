class Matrix:
    def __init__(self, matrix2d):
        if type(matrix2d) == list:
            for i in range(len(matrix2d)):
                if type(matrix2d[i]) != list:
                    raise TypeError('the list is not two-dimensional')
        else:
            raise TypeError('the argument must be a list')
        self.matrix2d = matrix2d
        self.__index_y = 0
        self.__index_x = 0
        self.__stop_iter = False

    def __str__(self):
        out = "[\n"
        for row in self.matrix2d:
            for val in row:
                out += f"{val:4}, "
            out += "\n"
        out += "]"
        return out
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__stop_iter:
            raise StopIteration
        if self.__index_y == len(self.matrix2d) - 1 and self.__index_x == len(self.matrix2d[self.__index_y]) - 1:
            self.__stop_iter = True
            return self.matrix2d[self.__index_y][self.__index_x]
        if len(self.matrix2d[self.__index_y]) == 1:
            self.__index_x = 0
            self.__index_y += 1
            return self.matrix2d[self.__index_y - 1][0]
        if self.__index_x == 0:
            self.__index_x += 1
            return self.matrix2d[self.__index_y][0]
        elif self.__index_x == len(self.matrix2d[self.__index_y]) - 1:
            self.__index_x = 0
            self.__index_y += 1
            return self.matrix2d[self.__index_y - 1][len(self.matrix2d[self.__index_y - 1]) - 1]
        elif self.__index_x > 0 and self.__index_x < len(self.matrix2d[self.__index_y]):
            self.__backup = self.__index_x
            self.__index_x += 1
            return self.matrix2d[self.__index_y][self.__backup]