import sys

from Astar import Astar
from BKTree import BKTree

from BrokenPhone import BrokenPhone

bk_tree = BKTree()
file = open(sys.argv[1], 'r')
print("Start loading file!")
for word in file:
    bk_tree.insert(word.rstrip())
print("End loading file!")

astar = Astar()
astar.search(bk_tree, "life", "death")

for item in astar.getChain():
    print(item)