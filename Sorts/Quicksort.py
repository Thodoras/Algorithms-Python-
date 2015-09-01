import random

class Quicksort:
	"""Elegant non-deterministic sorting algorithm."""

    @staticmethod
    def sort(array):
    	random.shuffle(array)
        Quicksort._sort(array, 0, len(array) - 1)

    @staticmethod
    def _sort(array, low, high):
        if high <= low:
            return
        med = Quicksort._partition(array, low, high)
        Quicksort._sort(array, low, med - 1)
        Quicksort._sort(array, med + 1, high)

    @staticmethod
    def _partition(array, low, high):
        i = low + 1
        j = high
        pivot = array[low]
        while True:
        	while array[i] <= pivot:
        		if i == high:
        			break
        		i+=1
        	while array[j] > pivot:
        		if j == low:
        			break
        		j -= 1
        	if i >= j:
        		break
        	Quicksort._exchange(array, i, j)
        Quicksort._exchange(array, low, j)
        return j

    @staticmethod
    def _exchange(array, index1, index2):
    	temp = array[index1]
    	array[index1] = array[index2]
    	array[index2] = temp