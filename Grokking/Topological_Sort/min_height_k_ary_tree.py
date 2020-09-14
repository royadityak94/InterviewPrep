# We are given an >>undirected<< graph that has characteristics of a k-ary tree. In such a graph, we can choose any node as the root to make a k-ary tree. The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs.
# Reference: https://www.educative.io/courses/grokking-the-coding-interview/3Ym408v7NQA#minimum-height-trees-hard
# Strategy: Since leaves can't give us MHT, keep removing them until we are left with 1-2 nodes which is our answer
from collections import deque

def find_trees(nodes, edges):
    # Time Complexity = Space Complexity = O(V+E)
    if nodes == 0:
        return []
    if nodes == 1:
        return [0]

    # Graph Initalization
    graph = {i:[] for i in range(nodes)}
    inDegrees = {i:0 for i in range(nodes)}

    # Graph Construction
    for parent, child in edges:
        graph[parent].append(child)
        graph[child].append(parent)
        inDegrees[child] += 1
        inDegrees[parent] += 1

    # Adding the non-dependent or pure-source nodes
    sources = deque()
    for key in inDegrees:
        if inDegrees[key] == 1:
            sources.appendleft(key)

    totalNodes = nodes
    while totalNodes > 2:
        leafSize = len(sources)
        totalNodes -= leafSize
        for j in range(leafSize):
            node = sources.popleft()
            for child in graph[node]:
                inDegrees[child] -= 1
                if inDegrees[child] == 1:
                    sources.append(child)

    return list(sources)

def main():
    print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))

main()
