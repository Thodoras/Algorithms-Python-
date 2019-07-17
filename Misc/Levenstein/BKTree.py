import queue

from Levenstein import Levenstein


class BKTree:

    def __init__(self):
        self._tree = {}
        self._root = ""

    def insert(self, word):

        if len(self._tree) == 0:
            self._tree[word] = {}
            self._root = word
            return

        node = self._root
        while True:
            distance = Levenstein.distance(word, node)
            if self._has_child_with_that_distance(node, distance):
                node = self._get_child_with_given_distance(node, distance)
            else:
                self._add_child_for_given_distance(node, distance, word)
                break

    def search(self, word, threshold):

        results = set()
        to_visit = queue.Queue()
        to_visit.put(self._root)

        while not to_visit.empty():
            node = to_visit.get()
            distance = Levenstein.distance(node, word)

            if  distance <= threshold:
                results.add(node)

            min_dist = distance - threshold
            max_dist = distance + threshold
            for dist, child in self._get_children(node).items():
                if min_dist <= dist <= max_dist:
                    to_visit.put(child)
        return results

    def _has_child_with_that_distance(self, node, distance):
        return distance in self._tree[node]

    def _get_children(self, node):
        return self._tree[node]

    def _get_child_with_given_distance(self, node, distance):
        return self._tree[node][distance]

    def _add_child_for_given_distance(self, node, distance, word):
        self._tree[node][distance] = word
        self._tree[word] = {}
