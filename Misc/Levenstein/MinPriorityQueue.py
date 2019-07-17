class MinPriorityQueue:

    def __init__(self):
        self._pq = []
        self._ind_dict = {}

    def insert(self, node):
        self._ind_dict[node.word] = len(self._pq)
        self._pq.append(node)
        self._swim(len(self._pq) - 1)

    def popMin(self):
        if len(self._pq) == 0:
            return None
        min_val = self._pq[0]
        self._ind_dict.pop(min_val.word)
        self._swap(0, len(self._pq)-1)
        self._pq = self._pq[:-1]
        self._sink(0)
        return min_val

    def update(self, word, new_weight):
        index = self._ind_dict[word]
        self._pq[index].weight = new_weight
        self._swim(index)
        self._sink(index)

    def isEmpty(self):
        return len(self._pq) == 0

    def hasWord(self, word):
        return word in self._ind_dict

    def getWeightOfWord(self, word):
        index = self._ind_dict[word]
        return self._pq[index].weight

    def _swim(self, i):
        parent_i = self._get_parent(i)
        if parent_i is not None and self._pq[i].lessThan(self._pq[parent_i]):
            self._swap(parent_i, i)
            self._swim(parent_i)

    def _sink(self, i):
        children = self._get_children(i)
        child = self._get_min_child(children)
        if child is not None and self._pq[child].lessThan(self._pq[i]):
            self._swap(child, i)
            self._sink(child)

    def _get_children(self, i):
        if 2*i + 2 < len(self._pq):
            return [2*i + 1, 2*i + 2]
        if 2*i + 1 < len(self._pq):
            return [2*i + 1]
        return []

    def _get_parent(self, i):
        if i <= 0 or i >= len(self._pq):
            return None
        return (i - 1) // 2

    def _swap(self, i, j):
        self._ind_dict[self._pq[i].word] = j
        self._ind_dict[self._pq[j].word] = i
        temp = self._pq[i]
        self._pq[i] = self._pq[j]
        self._pq[j] = temp

    def _get_min_child(self, children):
        if len(children) == 2:
            if self._pq[children[0]].lessThan(self._pq[children[1]]):
                return children[0]
            return children[1]
        if len(children) == 1:
            return children[0]
        return None
