class Insertion:
	'''Basic sorting algorithm with ~1/4*N^2 compares and ~1/4*N^2 exchanges. Good for partial sorted arrays. Stable.'''

	@staticmethod
	def sort(array):
		for i in range(1, len(array)):
			for j in range(i, 0, -1):
				if array[j] < array[j-1]:
					Insertion.exchange(array, j, j-1)
				else:
					break
		return array

	@staticmethod
	def exchange(array, index1, index2):
		temp1 = array[index1]
		array[index1] = array[index2]
		array[index2] = temp1