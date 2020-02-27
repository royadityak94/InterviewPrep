# Python program to implement the basic BFS-DFS algorithm
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited_dfs = []
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def bfs(self, s):
        visited = []
        queue = []
        queue.append(s)
        visited.append(s)

        while queue:
            s = queue.pop(0)
            print (s, end=" ")
            for neighbor in self.graph[s]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)
        return
    def dfs(self, s):
        if s not in self.visited_dfs:
            self.visited_dfs.append(s)
            print (s, end=" ")
            for neighbor in self.graph[s]:
                self.dfs(neighbor)
        return

if __name__ == '__main__':
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 5)
    g.addEdge(1, 3)
    g.addEdge(2, 5)
    g.addEdge(2, 4)
    g.addEdge(5, 4)
    g.addEdge(3, 6)
    g.addEdge(3, 7)
    g.addEdge(5, 8)
    g.addEdge(8, 9)

    print ("Following is the BFS starting from vertex = 2")
    #g.bfs(1)
    g.dfs(1)
