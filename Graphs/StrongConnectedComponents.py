import Graph

def strong_components(graph):
    """ Kosaraju's two-pass algorithm. 
    A function than computes the number of the stongly connected components of a directed graph in O(m + m) time.
    A strongly connected component is a subset of the set of nodes in a graph that for every two nodes p,q
    in it there is a path from p to q and a path from q to p."""

    revgraph = graph.reverse()
    finishing_times = {}
    for vertex in graph.vertices():
        finishing_times[vertex] = vertex
    DFS_loop(revgraph, finishing_times, False)
    return len(DFS_loop(graph, finishing_times, True))

def DFS_loop(graph, finishing_times, debug):
    visited = [False] * len(graph.vertices())
    nodes_visited = [0]
    leading_nodes = []
    temp_finishing_times = dict(finishing_times)
    for node in temp_finishing_times:
        current_node = temp_finishing_times[len(temp_finishing_times) - node - 1]
        if not visited[current_node]:
            leading_nodes.append(current_node)
            DFS(graph, current_node, visited, nodes_visited, finishing_times)
    return leading_nodes

def DFS(graph, vertex, visited, nodes_visited, finishing_times):
    visited[vertex] = True
    for edge in graph.edges(vertex):
        if not visited[edge]:
            DFS(graph, edge, visited, nodes_visited, finishing_times)
    finishing_times[nodes_visited[0]] = vertex
    nodes_visited[0] += 1

    






#lst = Graph.Graph([[2], [0], [1], [2]])
#lst = Graph.Graph([[6], [4], [8], [0], [7], [2,7], [3,8], [1], [5]])
lst = Graph.Graph([[1], [0]])
print strong_components(lst)
