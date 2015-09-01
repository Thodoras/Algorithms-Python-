import Graph
import Queue

def Distance(graph, s_node, d_node):
    """Algorithm that computes the shortest path from a starting node to another node
    in a graph in O(n + m)."""
    if s_node == d_node:
        return 0
    visited = [False] * len(graph.vertices())
    visited[s_node] = True
    dist = {}
    dist[s_node] = 0
    queue = Queue.Queue()
    queue.enqueue(s_node)
    while not queue.isEmpty():
        vertex = queue.dequeue()
        for edge in graph.edges(vertex):
            if not visited[edge]:
                queue.enqueue(edge)
                visited[edge] = True
                dist[edge] = dist[vertex] + 1
                if edge == d_node:
                    return dist[edge]
    return "+oo"