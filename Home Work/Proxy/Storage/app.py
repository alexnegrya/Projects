from storage import Storage

storage = Storage()   # in memory
storage.save("Memory Data")
print(storage.load())

storage = Storage("file")   # in file
storage.save("File Data")
print(storage.load())

storage = Storage('json')   # in json
storage.save('Json Data')
print(storage.load())