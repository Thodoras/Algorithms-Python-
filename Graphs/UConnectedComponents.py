import Graph
import Queue

def connected_comp(graph, explicit = False):
    """Function that computes the connected components of an undirected graph."""
    
    components = []
    vertices = graph.vertices()
    visited = [False] * len(vertices)
    for vertex in vertices:
        if not visited[vertex]:
            components.append(explore_BFS(graph, vertex, visited))
    if explicit:
        return components
    else:
        return len(components)

def explore_BFS(graph, start_node, visited):
    queue = Queue.Queue()
    queue.enqueue(start_node)
    component = [start_node]
    while not queue.isEmpty():
    	vertex = queue.dequeue()
        for edge in graph.edges(vertex):
            if not visited[edge]:
                visited[edge] = True
                queue.enqueue(edge)
                if edge != start_node:
                    component.append(edge)
    return component

lst = Graph.Graph([[2,4],[3],[0,4],[1], [0,2,6,8], [7,9], [4], [5,9], [4], [5,7]])
print connected_comp(lst, True) 
