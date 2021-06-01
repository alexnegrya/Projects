from json import dumps, loads

class JsonStorage:
    def __init__(self):
        self.name = 'data.json'
    
    def save(self, data):
        file = open(self.name, 'w')
        file.write(dumps(data))
        file.close()

    def load(self):
        file = open(self.name, 'r')
        data = loads(file.read())
        file.close()
        return data