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

class File:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"\tFile {self.name:15}\n"

photos = Directory('Photos')
photos.files.append('summer_1.jpg')
photos.files.append('summer_2.png')
photos.files.append('summer_3.jpeg')
print(photos)