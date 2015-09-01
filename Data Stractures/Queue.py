class Queue:
	'''Simple queue API.'''

	def __init__(self):
		self.array = []

	def enqueue(self, item):
		self.array.insert(0, item)

	def dequeue(self):
		return self.array.pop()

	def size(self):
		return len(self.array)

	def isEmpty(self):
		return 0 == self.size()