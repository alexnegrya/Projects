class FileStorage:
 def __init__(self):
   self.name = "data.txt"

 def save(self, data):
   file = open(self.name, "w")
   file.write(data)
   file.close()

 def load(self):
   file = open(self.name, "r")
   data = file.read()
   file.close()
   return data