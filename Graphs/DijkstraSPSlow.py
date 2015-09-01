import Graph

def shortest_path(graph, length_list, start_vertex):
    """Dirkstra's algorithm for computing shortest paths between two vertices in O(nm) time.
    Doesn't use heaps."""

    vertices_explored = [start_vertex]
    vertex_distances = {}
    vertex_distances[start_vertex] = 0
    while len(vertices_explored) != len(graph.vertices()):
    	minimum = float('inf')
    	node = -1
        for vertex in vertices_explored:
            for edge in graph.edges(vertex):
                if edge not in vertices_explored:
                    if vertex_distances[vertex] + length_list[vertex][edge] < minimum:
                        minimum = vertex_distances[vertex] + length_list[vertex][edge]
                        node = edge
        vertices_explored.append(node)
        vertex_distances[node] = minimum
    return vertex_distances


lst = Graph.Graph([[1,2], [2,3], [3], []])
length_list = [{1:1, 2:4}, {2:2, 3:6}, {3:3}, {}]
print shortest_path(lst, length_list, 0)