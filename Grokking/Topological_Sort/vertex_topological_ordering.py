# Given a directed graph, find the topological ordering of its vertices.
# Ref: https://www.educative.io/courses/grokking-the-coding-interview/m25rBmwLV00
# I/p: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
# O/p: [[3, 2, 0, 1], [3, 2, 1, 0]]

# Important Related Question ------>
# Find if a given Directed Graph has a cycle in it or not : Exactly same problem!!!

# Topological ordering is possible only when the graph has no directed cycles (cyclic dependencies), i.e. if the graph is a DAG.

from collections import deque
# Graph initalization (inDegree, graph), Graph Construction, Finding all source sink, Iterating over the source sink
# Checking for DAF/Cyclic Dependency, Returning Values

def topological_sort(vertices, edges):
    # Time Complexity: O(V+E), Space Complexity: O(V+E)
    sortedOrder = []
    if vertices == 0:
        return sortedOrder
    # Graph initalization (inDegree, graph)
    inDegree = {i:0 for i in range(vertices)}
    graph = {i:[] for i in range(vertices)}

    # Graph Construction
    for parent, child in edges:
        graph[parent].append(child)
        inDegree[child] += 1

    # Finding all the source
    sources = deque()
    for child in inDegree:
        if inDegree[child] == 0:
            sources.append(child)

    # Iterating over the source sink
    while sources:
        source = sources.popleft()
        sortedOrder.append(source)
        for child in graph[source]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # Checking for DAF/Cyclic Dependency
    if len(sortedOrder) != vertices:
        return []
    return sortedOrder

def main():
    print("Topological sort: " +
        str(topological_sort(4, [[3, 0], [3, 2], [0, 2], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

main()
