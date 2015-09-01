class Graph:
    """A class that enriches an adjacency list with many useful methods."""

    def __init__(self, adj_list, prog_convention = True):
        """The boolean 'prog_convention' argument defines if the adjacency list begin 
        with zero (True) or with one (False)."""

        self.lst = adj_list
        if prog_convention:
            self.prog_convention = 0
        else:
            self.prog_convention = 1

    def __str__(self):
        representation = ""
        for vertex in self.vertices():
            representation += str(vertex) + " " + str(self.edges(vertex)) + "\n"
        return representation

    def vertices(self):
        return range(self.prog_convention, len(self.lst) + self.prog_convention)

    def edges(self, vertex):
        return self.lst[vertex - self.prog_convention]

    def union(self, node1, node2, directed = False):
        if not directed:
            self.lst[node1].append(node2)
            #self.lst[node1].sort()
            self.lst[node2].append(node1)
            #self.lst[node2].sort()
        else:
            self.lst[node1].append(node2).sort()
            #self.lst[node1].sort()
    
    def reverse(self):
        """Useful for directed graphs only."""

        temp_list = [[]]*len(self.vertices())
        for node in self.vertices():
            for edge in self.edges(node):
            	temp = list(temp_list[edge])
            	temp.append(node)
            	temp_list[edge] = temp
        return Graph(temp_list)