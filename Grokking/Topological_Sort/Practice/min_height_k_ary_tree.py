# We are given an >>undirected<< graph that has characteristics of a k-ary tree. In such a graph, we can choose any node as the root to make a k-ary tree. The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs.
# Reference: https://www.educative.io/courses/grokking-the-coding-interview/3Ym408v7NQA#minimum-height-trees-hard
# Strategy: Since leaves can't give us MHT, keep removing them until we are left with 1-2 nodes which is our answer
from collections import deque

# O(V+E) time | O(V+E) space
def find_trees(vertices, edges):
    if not vertices:
        return []

    # Initializing graph & inDegree
    graph = {i:[] for i in range(vertices)}
    inDegree = {i:0 for i in range(vertices)}

    # Building graph & indegree
    for edge in edges:
        for j in range(1, len(edge)):
            parent, child = edge[j-1], edge[j]
            graph[parent] += child,
            graph[child] += parent,
            inDegree[child] += 1
            inDegree[parent] += 1

    # Initializing leaves (sources)
    leaves = deque()
    for vertex in inDegree:
        if inDegree[vertex] == 1:
            leaves += vertex,

    # Iterating over all the edges
    totalNodes = vertices
    while totalNodes > 2:
        currentLeafSize = len(leaves)
        totalNodes -= currentLeafSize

        for j in range(currentLeafSize):
            vertex = leaves.popleft()
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 1:
                    leaves += child,

    return list(leaves)





def main():
    print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))

main()
