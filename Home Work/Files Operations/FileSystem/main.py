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
        self.files.remove(file)

class File:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"\tFile {self.name:15}\n"

photos = Directory('Photos')

photos.pasteFile('summer_1.jpg')
photos.pasteFile('summer_2.png')
photos.pasteFile('summer_3.jpeg')
print(photos)

photos.deleteFile('summer_1.jpg')
print(photos)