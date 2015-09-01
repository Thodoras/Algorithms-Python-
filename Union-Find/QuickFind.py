class QuickFind:
	'''In General: A straightforward algorithm which unions indices of a given array in O(N) time and 
	finds connectivity in O(1) time.'''

	def __init__(self, length):
		self.array = []
		self.length = length
		for i in range(self.length):
			self.array.append(i)

	def connected(self, item1, item2):
		return self.array[item1] == self.array[item2]

	def union(self, item1, item2):
		temp1 = self.array[item1]
		temp2 = self.array[item2]
		for i in range(self.length):
			if self.array[i] == temp1:
				self.array[i] = temp2

	
