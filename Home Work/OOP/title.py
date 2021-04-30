class Title:
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return f"-= {self.text} =-"

title = Title('News')
print(title)
