import random
import math

class Quick3Way:
	"""Very fast non-deterministic algorithm for sorting lists with may duplicates."""

    @staticmethod
    def sort(array):
        random.shuffle(array)
        Quick3Way._sort(array, 0, len(array) - 1)

    @staticmethod
    def _sort(array, low, high):
    	if (high <= low):
    		return
    	pivot_index = low
    	i = low
    	j = high
    	pivot = array[pivot_index]
        while i <= j:
            compare = Quick3Way._compare(pivot, array[i])
            if compare > 0:
                Quick3Way._exchange(array, pivot_index, i)
                pivot_index += 1
                i += 1
            elif compare < 0:
    	    	Quick3Way._exchange(array, i, j)
    	    	j -= 1
    	    else:
    	    	i += 1
    	Quick3Way._sort(array, low, pivot_index - 1)
    	Quick3Way._sort(array, j + 1, high)

        
    @staticmethod
    def _exchange(array, index1, index2):
    	temp = array[index1]
    	array[index1] = array[index2]
    	array[index2] = temp

    @staticmethod
    def _compare(value1, value2):
    	if value1 > value2:
    		return 1
    	elif value1 < value2:
    		return -1
    	else:
    		return 0