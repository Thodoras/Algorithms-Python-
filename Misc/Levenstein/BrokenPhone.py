from BKTree import BKTree

class BrokenPhone:

    def __init__(self):
        self._tree = BKTree()

    def load(self, path):
        file = open(path, 'r')
        for word in file:
            self._tree.insert(word.rstrip())


