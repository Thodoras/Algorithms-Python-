from Node import Node
from Levenstein import Levenstein as lst
from MinPriorityQueue import MinPriorityQueue


class Astar:

    def __init__(self):
        self._prev = None
        self._pq = None
        self._visited = None
        self._found = None
        self._start_word = None
        self._end_word = None

    def search(self, bk_tree, start_word, end_word):
        self._prev = {}
        self._pq = MinPriorityQueue()
        self._visited = set()
        self._found = False
        self._start_word = start_word
        self._end_word = end_word

        dist = lst.distance(start_word, end_word)
        self._pq.insert(Node(start_word, dist))
        depth = 0

        while not self._pq.isEmpty():
            node = self._pq.popMin()
            word = node.word
            depth += 1

            if word == end_word:
                self._found = True
                return
            self._visited.add(word)
            neighbor_words = bk_tree.search(word, 1)
            for neighbor_word in neighbor_words:
                if neighbor_word not in self._visited:
                    weight = depth + lst.distance(neighbor_word, end_word)
                    if not self._pq.hasWord(neighbor_word):
                        self._pq.insert(Node(neighbor_word, weight))
                        self._prev[neighbor_word] = word
                    elif weight < self._pq.getWeightOfWord(neighbor_word):
                        self._pq.update(neighbor_word, weight)
                        self._prev[neighbor_word] = word

    def isConnected(self):
        return self._found

    def getChain(self):
        if not self.isConnected():
            return self._start_word
        result = [self._end_word]
        while result[-1] != self._start_word:
            word = result[-1]
            prev_word = self._prev[word]
            result.append(prev_word)
        result.reverse()
        return result