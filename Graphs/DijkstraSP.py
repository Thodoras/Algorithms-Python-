import HeapKV
import Graph

def shortest_path(graph, lengths, source):
    """Fast shortest path algorithm, that completes its procedures in O(mlogn) time
    using heap (priority queue)."""

    heap = HeapKV.HeapKV()
    dist = []
    for vertex in graph.vertices():
        if source == vertex:
            dist.append(0)
        else:
            dist.append(float("inf"))
        heap.insert(vertex, dist[vertex])
    
    while heap.get_length() != 0:

        node = heap.minimum()
        node = node[0]
        for edge in graph.edges(node):
            distance = dist[node] + lengths[node][edge]
            if distance < dist[edge]:
                dist[edge] = distance
                heap.change_value(edge, dist[edge])

    return dist

"""lst = Graph.Graph([[1,2], [2,3], [3], []])
length_list = [{1:1, 2:4}, {2:2, 3:6}, {3:3}, {}]
print shortest_path(lst, length_list, 0)"""