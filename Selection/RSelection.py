import random

class RSelection:
    '''An algorithm that computes the i-th order statistic in linear time.'''

    @staticmethod
    def rSelect(array, order_stat):
    	if len(array) < order_stat:
    		return 'Insufficient number of elements for this statistic order.'
        if len(array) == 1:
            return array[0]
        rand_index = random.choice(range(len(array)))
        RSelection._swap(array, 0, rand_index)
        index = RSelection._partition(array)
        if index + 1 == order_stat:
            return array[index]
        elif index + 1 > order_stat:
            return RSelection.rSelect(array[:index], order_stat)
        else:
            return RSelection.rSelect(array[index + 1:], order_stat - index - 1)

    @staticmethod
    def _partition(array):
        pivot = array[0]
        i = 1
        for j in range(1,len(array)):
            if pivot > array[j]:
                RSelection._swap(array, i, j)
                i += 1
        RSelection._swap(array, 0, i-1)
        return i - 1


    @staticmethod
    def _swap(array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp