class Node:

    def __init__(self, word, weight):
        self.word = word
        self.weight = weight

    def lessThan(self, node):
        return self.weight < node.weight
