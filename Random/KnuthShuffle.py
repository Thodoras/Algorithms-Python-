import random

class KnuthShuffle:

    @staticmethod
    def shuffle(array):
    	for i in range(len(array)):
    		index = random.randrange(i + 1)
    		KnuthShuffle._exchange(array, i, index)

    @staticmethod
    def _exchange(array, index_1, index_2):
        temp = array[index_1]
        array[index_1] = array[index_2]
        array[index_2] = temp