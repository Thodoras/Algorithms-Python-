import math

class Heap:
    """A class of the heap data structure. It inserts an removes items in O(nlogn) time."""

    def __init__(self, array = []):
        self.array = array
        self._heapify()

    def __str__(self):
    	return str(self.array)

    def insert(self, node):
        self.array.append(node)
        index = self.get_length() - 1
        while (self.has_parent(index) and self.get_node(self.get_parent(index)) > node):
            self._swap(index, self.get_parent(index))
            index = self.get_parent(index)

    def remove(self, index):
    	if index >= self.get_length():
    	    return "Index out of heap's bounds"
        jndex = self.get_length() - 1
        self._swap(index, jndex)
        node = self.array.pop(jndex)
        self._heapify_node(index)
        return node

    def get_length(self):
        return len(self.array)

    def get_height(self):
        if len(self.array) == 0:
            return "Null tree."
        else:
            return int(math.ceil(math.log(len(self.array), 2)))

    def get_node(self, index):
        return self.array[index]

    def has_children(self, index):
        if index > self.get_length()/2 - 1:
            return False
        else:
        	return True

    def get_children(self, index):
        if self.has_children(index):
            if 2*index + 2 < self.get_length():
                return [2*index + 1, 2*index + 2]
            else:
                return [2*index + 1]

    def has_parent(self, index):
        if index > 0 and index < self.get_length():
            return True
        else:
            return False

    def get_parent(self, index):
        if self.has_parent(index):
            return int(math.floor(float(index - 1) / 2))
    
    def _heapify(self):
        for i in range(self.get_length() / 2 - 1, -1, -1):
            self._heapify_node(i)

    def _heapify_node(self, index):
        if not self.has_children(index):
            return
        nodes = []
        for i in self.get_children(index):
            nodes.append(self.get_node(i))
        minimum = min(nodes)
        jndex = self.array.index(minimum)
        if self.get_node(index) > minimum:
            self._swap(index, jndex)
            self._heapify_node(jndex)
        else:
            return

    def _swap(self, index, jndex):
        temp = self.array[index]
        self.array[index] = self.array[jndex]
        self.array[jndex] = temp
