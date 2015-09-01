class Stack:
	'''Simple API for stack data structure'''

	def __init__(self):
		self.array = []

	def push(self, item):
		self.array.append(item)

	def pop(self):
		return self.array.pop()

	def size(self):
		return len(self.array)

	def isEmpty(self):
		return 0 == self.size()