class QuickUnion:
	'''union O(N), find O(N)'''

	def __init__(self, length):
		self.array = []
		self.length = length
		for i in range(self.length):
			self.array.append(i)

	def root(self, value):
		while self.array[value] != value:
			value = self.array[value]
		return value

	def connected(self, item1, item2):
		return self.root(item1) == self.root(item2)

	def union(self, item1, item2):
		temp1 = self.root(item1)
		temp2 = self.root(item2)
		self.array[temp1] = temp2
