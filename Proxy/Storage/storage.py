from memorystorage import MemoryStorage
from filestorage import FileStorage
from jsonstorage import JsonStorage


class StorageError(Exception):
    pass


class WrongStorageMethod(Exception):
    pass


class _StorageProxy:
    def __init__(self, storageType="memory"):
        if storageType == "memory": self.realStorage = MemoryStorage()
        elif storageType == "file": self.realStorage = FileStorage()
        elif storageType == "json": self.realStorage = JsonStorage()
        else: raise TypeError('Wrong storage type!')

    def __getattr__(self, name):
        if name in ["load", "save"]:
            if name == 'load': return self.realStorage.load
            elif name == 'save': return self.realStorage.save


class Storage:
    def __init__(self, storage_type=None):
        if storage_type in ['memory', 'file', 'json'] or storage_type == None:
            if storage_type == None or storage_type == 'memory':
                self._storage = _StorageProxy()
            elif storage_type == 'file': self._storage = _StorageProxy('file')
            elif storage_type == 'json': self._storage = _StorageProxy('json')
        else: raise StorageError('unknown storage type')

    def __getattr__(self, name):
        if name in ['load', 'save']:
            if name == 'load': return self._storage.load
            elif name == 'save': return self._storage.save
        else: raise WrongStorageMethod('unknown storage method')
