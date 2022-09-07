class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def __str__(self):
        content = ""
        for file in self.files:
            content += str(file) + ' '
        return f"Dir {self.name:15}\n{content}"
    
    def paste_file(self, file):
        if file not in self.files:
            self.files.append(file)
    
    def delete_file(self, file):
        for f in self.files:
            if f == file:
                self.files.remove(file)

class File:
    def __init__(self, name): self.name = name

    def __str__(self): return f"\tFile {self.name:15}\n"
    
    def __eq__(self, other): return self.name == other.name if type(other) == \
        File else self.name == other

photos = Directory('Photos')

photos.paste_file(File('photo_1.jpg'))
photos.paste_file(File('photo_2.png'))
photos.paste_file(File('photo_3.jpeg'))
photos.paste_file(File('photo_2.png'))
print(photos)

photos.delete_file(File('photo_1.jpg'))
print(photos)
