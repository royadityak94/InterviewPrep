'''
Given a directed graph, find the topological ordering of its vertices.
'''
from collections import deque

def topological_sort(vertices, edges):
    sortedOrder = []
    if not vertices:
        return sortedOrder

    inDegree = {i:0 for i in range(vertices)}
    graph = {i:[] for i in range(vertices)}

    # Build the graph
    for parent, child in edges:
        graph[parent] += child,
        inDegree[child] += 1

    # Find all the sources, i.e. having 0 in-degrees
    sources = deque()
    for key in inDegree:
        if not inDegree[key]:
            sources += key,

    # For each source, add it to the sorted order, and substract from its children inDegrees
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
