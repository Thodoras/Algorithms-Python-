import math

class HeapKV:
    """A class similar to Heap but takes as imput hash tables, and returns keys. Notice! Do not insert values with existing keys.
    Instead use change_value method which is O(logN). KV stands for keys values."""

    def __init__(self, hasht = {}):
        self.keys = [key for key in hasht]
        self.values = [hasht[key] for key in hasht]
        self._heapify()

    def minimum(self):
        key = self.keys[0]
        return [key, self.remove(key)]

    def insert(self, key, value):
        self.keys.append(key)
        self.values.append(value)
        while(self.has_parent(key) and self.get_value_from_key(self.get_parent(key)) > value):
            self._swap(key, self.get_parent(key))

    def remove(self, key):
        last_key = self.keys[-1]
        if key == last_key:
        	self.keys.pop(-1)
        	return self.values.pop(-1)
        self._swap(key, last_key)
        value = self.values.pop(-1)
        self.keys.pop(-1)
        self._heapify_node(self.keys.index(last_key))
        return value

    def change_value(self, key, value):
        self.remove(key)
        self.insert(key, value)

    def get_length(self):
        return len(self.keys)

    def get_height(self):
        if len(self.keys) == 0:
            return 'Null tree'
        else:
            return int(math.ceil(math.log(len(self.keys), 2)))

    def has_key(self, key):
    	return key in self.keys

    def get_value_from_key(self, key):
        index = self.keys.index(key)
        return self.values[index]

    def get_node(self, key):
    	index = self.keys.index(key)
    	return self.values[index]
    
    def has_children(self, key):
        if self.keys.index(key) > self.get_length()/2 - 1:
            return False
        else:
            return True

    def get_children(self, key):
    	index = self.keys.index(key)
        if self.has_children(key):
            if 2*index + 2 < self.get_length():
                return [self.keys[2*index + 1], self.keys[2*index + 2]]
            else:
                return [self.keys[2*index + 1]]

    def has_parent(self, key):
        if self.keys.index(key) > 0 and self.keys.index(key) < self.get_length():
            return True
        else:
            return False

    def get_parent(self, key):
        if self.has_parent(key):
            index = self.keys.index(key)
            return self.keys[int(math.floor(float(index - 1) / 2))]

    def _heapify(self):
        for i in range(self.get_length() / 2 - 1, -1, -1):                  #Iterate through the nodes which have children. That is [l/2], l=length.
            self._heapify_node(i)


    def _heapify_node(self, index):
        if not self.has_children(self.keys[index]):
            return
        node_values = []
        for key in self.get_children(self.keys[index]):
            node_values.append(self.get_value_from_key(key))
        minimum = min(node_values)
        jndex = self.values.index(minimum)
        if self.values[index] > minimum:
            self._swap(self.keys[index], self.keys[jndex])
            self._heapify_node(jndex)
        else:
        	return


    def _swap(self, key1, key2):
        index = self.keys.index(key1)
        jndex = self.keys.index(key2)
        temp1 = self.keys[index]
        temp2 = self.values[index]
        self.keys[index] = self.keys[jndex]
        self.values[index] = self.values[jndex]
        self.keys[jndex] = temp1
        self.values[jndex] = temp2

"""
lst = HeapKV({'a':80, 'b':17, 'cds':30, 27:27, 15:15, 'p':0})
print lst.keys
print lst.values
lst._heapify()
print lst.keys
print lst.values
lst.insert('x', 5)
print lst.keys
print lst.values
lst.insert('y', 1)
print lst.keys
print lst.values
lst.change_value('x', 4)
print lst.keys
print lst.values
print lst.has_key('x')
print lst.keys
print lst.values
print lst.remove('x')
print lst.has_key('x')
print "=========", lst.minimum()
print lst.keys
print lst.values"""

"""
lst = HeapKV({0:0, 1:float("inf"), 2:float("inf"), 3:float("inf")})
node = lst.minimum()
lst.change_value(1, 1)
node = lst.minimum()
print lst.keys
print lst.values
print "==========="
lst.change_value(2,4)
print lst.keys
print lst.values
"""