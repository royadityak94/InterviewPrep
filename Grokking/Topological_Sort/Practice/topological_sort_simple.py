'''
Given a directed graph, find the topological ordering of its vertices.
'''
from collections import deque

# O(V+E) time | O(V+E) space
def topological_sort(vertices, edges):
    sortedOrder = []
    if not vertices:
        return sortedOrder

    # Initializing graph and inDegree
    graph = {i:[] for i in range(vertices)}
    inDegree = {i:0 for i in range(vertices)}

    # Building graph
    for parent, child in edges:
        graph[parent] += child,
        inDegree[child] += 1

    # Initializing sources
    sources = deque()
    for vertex in range(vertices):
        if not inDegree[vertex]:
            sources += vertex,

    # Iterating over all the edges using sources
    while sources:
        vertex = sources.popleft()
        sortedOrder += vertex,
        for child in graph[vertex]:
            inDegree[child] -= 1
            if not inDegree[child]:
                sources += child,
    if len(sortedOrder) != vertices:
        return []
    return sortedOrder



if __name__ == '__main__':
    print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))
