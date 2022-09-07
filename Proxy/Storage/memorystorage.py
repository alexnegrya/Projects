class MemoryStorage:
	def __init__(self): self.data = None

	def save(self, data): self.data = data

	def load(self): return self.data
