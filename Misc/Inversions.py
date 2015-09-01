class Inversions:
	'''A class that counts inversions of an array efficiently (O(NlogN)). '''

    def __init__(self):
        self.count = 0

    def count_inversions(self, array):
        if len(array) <= 1:
        	return 0
        aux_array = list(array)
        low = 0
        high = len(array) - 1
        self._sort(array, aux_array, low, high)
        return self.count

    def _sort(self, array, aux_array, low, high):
        if low >= high:
            return array
        mid = (low + high) / 2
        self._sort(array, aux_array, low, mid)
        self._sort(array, aux_array, mid+1, high)
        self._merge(array, aux_array, low, mid, high)

    def _merge(self, array, aux_array, low, mid, high):
    	for i in range(low, high + 1):
            aux_array[i] = array[i]

        pointer_1 = low
        pointer_2 = mid + 1
        for i in range(low, high + 1):
            if pointer_1 > mid:
                array[i] = aux_array[pointer_2]
                pointer_2 += 1
            elif pointer_2 > high:
                array[i] = aux_array[pointer_1]
                pointer_1 += 1
            elif aux_array[pointer_1] > aux_array[pointer_2]:
                array[i] = aux_array[pointer_2]
                self.count += (mid + 1 - pointer_1)
                pointer_2 += 1
            else:
                array[i] = aux_array[pointer_1]
                pointer_1 += 1

#Testing
"""
txt_file = open('IntegerArray.txt', 'r')
array = []
count = 0
for line in txt_file:
	array.append(int(line))
a = [76, 85, 59, 142, 67, 51, 133, 64, 42, 128, 9, 153, 169, 114, 193, 162, 90, 77, 14, 154, 151, 182, 18, 160, 197, 26, 143, 178, 137, 166, 1, 74, 152, 122, 185, 10, 78, 107, 84, 113, 116, 28, 175, 124, 129, 89, 30, 29, 163, 49, 40, 101, 66, 19, 80, 119, 135, 57, 38, 104, 73, 32, 146, 2, 91, 99, 190, 58, 132, 23, 194, 75, 167, 79, 123, 112, 199, 131, 60, 55, 47, 174, 17, 168, 52, 155, 109, 200, 161, 136, 195, 111, 25, 71, 145, 88, 24, 81, 186, 16, 130, 179, 68, 65, 83, 156, 53, 148, 4, 196, 33, 50, 3, 94, 34, 45, 36, 147, 35, 70, 62, 69, 191, 141, 22, 46, 183, 126, 87, 13, 159, 103, 127, 144, 8, 11, 41, 189, 198, 54, 56, 108, 176, 106, 173, 97, 21, 164, 98, 172, 171, 170, 149, 110, 138, 31, 125, 63, 82, 192, 39, 92, 95, 15, 7, 105, 187, 180, 5, 6, 44, 102, 134, 188, 181, 139, 184, 177, 12, 115, 61, 165, 37, 140, 100, 157, 20, 150, 43, 117, 120, 48, 27, 121, 86, 96, 158, 72, 118, 93]
c = Inversions()
print c.count_inversions(array)
"""
