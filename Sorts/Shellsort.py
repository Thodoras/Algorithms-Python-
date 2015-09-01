class Shellsort:
	'''Non trivial sorting method with O(N^3/2) growth'''

	@staticmethod
	def sort(array):
		length = len(array)
		aux = 1
		while aux < length // 3:
			aux = aux*3 + 1

		while aux >= 1:
			for i in range(aux, length):
				for j in range(i, 0, -aux):
					if array[j] < array[j-1]:
						Shellsort.exchange(array, j, j-1)
					else:
						break
			aux /= 3
		return array

	@staticmethod
	def exchange(array, index1, index2):
		temp1 = array[index1]
		array[index1] = array[index2]
		array[index2] = temp1