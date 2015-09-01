class MergerSort:

    '''sStable, deterministic algorithm for sorting with O(NlogN) execution time, but not in place (i.e. uses (linear) extra memory)'''

    @staticmethod
    def sort(array):
        if len(array) <= 1:
            return
        aux_array = list(array)
        low = 0
        high = len(array) - 1
        MergerSort._sort(array, aux_array, low, high)

    @staticmethod
    def _sort(array, aux_array, low, high):
        if low >= high:
            return array
        mid = (low + high) / 2
        MergerSort._sort(array, aux_array, low, mid)
        MergerSort._sort(array, aux_array, mid+1, high)
        MergerSort._merge(array, aux_array, low, mid, high)
		
    @staticmethod
    def _merge(array, aux_array, low, mid, high):
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
                pointer_2 += 1
            else:
                array[i] = aux_array[pointer_1]
                pointer_1 += 1

lst = [0,4,6,3]
MergerSort.sort(lst)
print lst