# Dijkstra's implementation yields cheapest and shortest path (collision) ...
from collections import defaultdict
import heapq
import math

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)
    def addEdge(self, u, v, w):
        self.graph[u].update({v: w})
    def display(self):
        print (self.graph)
    def count(self, arr):
        return
    def shortest_path(self, start, end):
        queue, seen = [(0, start, [])], set()
        while True:
            (cost, v, path) = heapq.heappop(queue)
            if v not in seen:
                seen.add(v)
                path = path + [v]
                if v == end:
                    print (math.floor(cost), path)
                    return
                for (next, c) in self.graph[v].iteritems():
                    heapq.heappush(queue, (cost+c+math.log(len(path)), next, path))

if __name__ == '__main__':
    inp_graph = {
    'a': {'w': 14, 'x': 7, 'y': 9},
    'b': {'w': 9, 'z': 6},
    'w': {'a': 14, 'b': 9, 'y': 2},
    'x': {'a': 7, 'y': 10, 'z': 15},
    'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
    'z': {'b': 6, 'x': 15, 'y': 11}}

    g = Graph()
    for node in inp_graph.keys():
        for key in inp_graph.get(node).keys():
            g.addEdge(node, key, inp_graph.get(node).get(key))

    g.display()
    g.shortest_path('b', 'x')
