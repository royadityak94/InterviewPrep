# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.
from collections import deque

# O(V+E) time | O(V+E) space
def find_order(vertices, edges):
    sortedOrder = []
    if not vertices:
        return True

    # Initializing graph and indegree
    graph = {i:[] for i in range(vertices)}
    inDegree = {i:0 for i in range(vertices)}

    # Building the graph
    for parent, child in edges:
        graph[parent] += child,
        inDegree[child] += 1

    # Initializing sources (zero dependency vertex)
    sources = deque()
    for vertex in range(vertices):
        if not inDegree[vertex]:
            sources += vertex,

    # Building the sources
    while sources:
        vertex = sources.popleft()
        sortedOrder += vertex,
        for child in graph[vertex]:
            inDegree[child] -= 1
            if not inDegree[child]:
                sources += child,

    return len(sortedOrder) == vertices, sortedOrder


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
