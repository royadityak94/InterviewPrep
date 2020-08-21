# Python program to check if the input graph is bipartite or not
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for _ in range(self.V)] for _ in range(self.V)]

    def isBipartite(self, src):
        colorArr = [-1] * self.V
        queue = []
        colorArr[src] = 1
        queue.append(src)

        while queue:
            u = queue.pop()
            # Check for cycles in the Graph
            if self.graph[u][u] == 1:
                return False
            for v in range(self.V):
                if self.graph[u][v] == 1 and colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
        return True

if __name__ == '__main__':
    # Quadrilateral
    g1 = Graph(4)
    g1.graph = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0] ]
    if g1.isBipartite(0):
        print ("Input g1 is Bipartite graph" )
    else:
        print ("Input g1 is NOT a Bipartite graph")

    # Pentagon
    g2 = Graph(5)
    g2.graph = [[0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]
    if g2.isBipartite(0):
        print ("Input g2 is Bipartite graph" )
    else:
        print ("Input g2 is NOT a Bipartite graph")

    # Hexagon
    g3 = Graph(6)
    g3.graph = [[0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0]]
    if g3.isBipartite(0):
        print ("Input g3 is Bipartite graph" )
    else:
        print ("Input g3 is NOT a Bipartite graph")
