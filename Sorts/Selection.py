class Selection:
	'''Basic selection algorithm for sorting. Always O(N^2).'''

	@staticmethod
	def sort(array):
		for i in range(len(array)):
			j = Selection.findMinIndex(array, i)
			Selection.exchange(array, i,j)
		return array

	#private method
	@staticmethod
	def findMinIndex(array, starting_position):
		min = array[starting_position]
		index = starting_position
		for i in range(starting_position, len(array)):
			if array[i] < min:
				min = array[i]
				index = i
		return index

	#private method
	@staticmethod
	def exchange(array, index1, index2):
		temp1 = array[index1]
		array[index1] = array[index2]
		array[index2] = temp1