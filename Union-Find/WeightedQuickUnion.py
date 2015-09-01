class WeightedQuickUnion:
	'''union O(logN), find O(logN), optimal'''

	def __init__(self, length):
		self.array = []
		self.size = []
		self.length = length
		for i in range(self.length):
			self.array.append(i)
			self.size.append(1)

	def root(self, value):
		while self.array[value] != value:
			self.array[value] = self.array[self.array[value]]
			value = self.array[value]
		return value

	def connected(self, item1, item2):
		return self.root(item1) == self.root(item2)

	def union(self, item1, item2):
		temp1 = self.root(item1)
		temp2 = self.root(item2)
		if temp1 == temp2:
			return
		if self.size[temp1] < self.size[temp2]:
			self.array[temp1] = temp2
			self.size[temp2] += self.size[temp1]
		else:
			self.array[temp2] = temp1
			self.size[temp1] += self.size[temp2]