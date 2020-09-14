# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

from collections import deque

def find_order(tasks, prerequisites):
    # Time Complexity: O(V+E), Space Complexity: O(V+E)
    sortedOrder = []
    if tasks <= 0:
        return sortedOrder

    # ----- Formulating it as a graph problem -----

    # Graph Initalization
    inDegree = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}

    # Graph Construction
    for parent, child in prerequisites:
        graph[parent].append(child)
        inDegree[child] += 1

    # Skimming out pure-sources
    sources = deque()
    for source in inDegree:
        if inDegree[source] == 0:
            sources.append(source)

    # Iterating over the sources to create downstream tasks
    while sources:
        source = sources.popleft()
        sortedOrder.append(source)
        for child in graph[source]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # Checking for DAG (non-cyclicity)
    if len(sortedOrder) != tasks:
        return []

    return sortedOrder

def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
