class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def __str__(self):
        content = ""
        # Цикл проходится по свойству files текущего класса
        # и склеивает названия в единный str на который ссылается переменная content
        for file in self.files:
            content += str(file) + ' '
        return f"Dir {self.name:15}\n{content}"
    
    def pasteFile(self, file):
        if file != self.files:
            self.files.append(file)
    
    def deleteFile(self, file):
        for f in self.files:
            if f == file:
                self.files.remove(file)

class File:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"\tFile {self.name:15}\n"
    
    def __eq__(self, other):
        if type(other) == File:
            if self.name == other.name:
                return True
            else:
                return False
        else:
            if self.name == other:
                return True
            else:
                return False

photos = Directory('Photos')

photos.pasteFile(File('summer_1.jpg'))
photos.pasteFile(File('summer_2.png'))
photos.pasteFile(File('summer_3.jpeg'))
print(photos)

photos.deleteFile(File('summer_1.jpg'))
print(photos)