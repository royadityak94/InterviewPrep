# Python file to create graph for computing bellman-ford algorithm
import math
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v, w):
        self.graph[u].append((w, v))
    def display(self):
        print (self.graph)
    def get_all_vertexes(self):
        vertices = set()
        for key in self.graph.keys():
            if key not in vertices:
                vertices.add(key)
                for (cost, neighbor) in self.graph.get(key):
                    if neighbor not in vertices:
                        vertices.add(neighbor)
        vertices = list(vertices)
        vertices.sort()
        return vertices
    def bellman_ford(self, start):
        all_vertex = self.get_all_vertexes()
        dist = {}
        for i in all_vertex:
            if i==start:
                dist[i] = 0
            else:
                dist[i] = math.inf

        for iteration in range(len(all_vertex)-1):
            not_update = True
            for vertex in all_vertex:
                if self.graph.get(vertex) is not None:
                    for (cost, neighbor) in self.graph.get(vertex):
                        if (dist.get(vertex) != math.inf) and (dist.get(neighbor) > dist.get(vertex) + cost):
                            dist[neighbor] = dist.get(vertex)+ cost
                            not_update = False
            if not_update:
                break
        print (dist)
        return

if __name__ == '__main__':
    naive_graph = {
    'a': {'b':-1, 'c':4},
    'b': {'c':3, 'd':2, 'e':2},
    'd': {'b':1, 'c':5},
    'e': {'d': -3}
    }

    g = Graph()
    for key in naive_graph.keys():
        for inner_key in naive_graph.get(key).keys():
            element = naive_graph.get(key).get(inner_key)
            g.addEdge(key, inner_key, element)

    g.display()
    g.bellman_ford('a')
