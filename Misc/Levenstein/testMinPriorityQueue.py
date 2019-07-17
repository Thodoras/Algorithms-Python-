from Node import Node
from MinPriorityQueue import MinPriorityQueue

pq = MinPriorityQueue()
print(pq.popMin())
pq.insert(Node("foo", 5))
print(pq._pq)
pq.insert(Node("bar", 3))
print(pq._pq)
pq.insert(Node("asd", 4))
print(pq._pq)
pq.update("foo", 2)
print(pq._pq)
pq.insert(Node("ass", 7))
print(pq._pq)
pq.insert(Node("kjh", 0))
print(pq._pq)
pq.insert(Node("zxc", 1))
print(pq._pq)
print(pq.popMin())
print(pq._pq)
print(pq.popMin())
print(pq._pq)
# pq.update(7, 1)
# print(pq._pq)



