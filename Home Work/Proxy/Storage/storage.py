from memorystorage import MemoryStorage
from filestorage import FileStorage
from jsonstorage import JsonStorage

class StorageProxy:
  def __init__(self, storageType="memory"):
    if storageType == "memory":
      self.realStorage = MemoryStorage()
    elif storageType == "file":
      self.realStorage = FileStorage()
    elif storageType == 'json':
      self.realStorage = JsonStorage()
    else:
      raise TypeError('Wrong storage type!')

  def __getattr__(self, name):
    if name == "load":
      return self.realStorage.load
    if name == "save":
      return self.realStorage.save