import random
import math

class Mincut:
'''An algorithm that computes the minimun cut (i.e. the least amount of edges between any two connected components that divide the graph) 
of a connected graph in O(n^2*m)'''

    @staticmethod
    def compute_min_cut(graph, align = False):
        if align:
            Mincut._align(graph)
        tries = []
    	for i in range(len(graph) * int(math.ceil(math.log(len(graph))))):
            temp_graph = list(graph)
            count = range(len(graph))
            while(len(count) > 2):
                vertex1 = random.choice(count)
                vertex2 = random.choice(temp_graph[vertex1])
                count.remove(vertex2)
                temp_graph = Mincut._merge(temp_graph, vertex1, vertex2)
            for item in temp_graph:
        	    if len(item) > 0:
        		    tries.append(len(item))
        		    break
        return min(tries)

    @staticmethod
    def _merge(graph, vertex1, vertex2):
    	new_graph = []
        for i in range(len(graph)):
            if i == vertex1:
                new_graph.append([item for item in graph[vertex1] if item != vertex1 and item != vertex2] + [item for item in graph[vertex2] if item != vertex1 and item != vertex2])
            elif i == vertex2:
                new_graph.append([])
            else:
                temp_line = []
                for item in graph[i]:
                    if item == vertex2:
                        temp_line.append(vertex1)
                    else:
                        temp_line.append(item)
                new_graph.append(list(temp_line))
        return new_graph

    @staticmethod
    def _align(graph):
    	'''This function subtracts 1 from the abjacency list so that it agrees with pyhton's list notation.'''
    	
        for item in graph:
            for i in range(len(item)):
                item[i] -= 1
