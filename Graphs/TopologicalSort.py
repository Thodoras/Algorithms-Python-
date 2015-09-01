import Graph
import Stack

def topological_sort(graph):
    """A function that returns a list of an acyclic directed graph's vertices 
    in topologigal order."""
    
    vertices = graph.vertices()
    visited = [False] * len(vertices)
    current_label = range(len(vertices))
    sorted_graph = [-1] * len(vertices)
    for vertex in vertices:
        if not visited[vertex]:
             DFS(graph, vertex, visited, current_label, sorted_graph)
    return sorted_graph

def DFS(graph, vertex, visited, current_label, sorted_graph):
    visited[vertex] = True
    for edge in graph.edges(vertex):
        if not visited[edge]:
            DFS(graph, edge, visited, current_label, sorted_graph)
    sorted_graph[current_label[-1]] = vertex
    current_label.pop(-1)