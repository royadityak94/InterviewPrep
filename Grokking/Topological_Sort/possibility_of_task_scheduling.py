from collections import deque

# Important ------ Similar Problems ->
# There are ‘N’ courses, labeled from ‘0’ to ‘N-1’. Each course can have some prerequisite courses which need to be completed before it can be taken. Given the number of courses and a list of prerequisite pairs, find if it is possible for a student to take all the courses.

def is_scheduling_possible(tasks, prerequisites):
    # Time Complexity: O(V+E), Space Complexity: O(V+E)
    sortedOrder = []
    if tasks <= 0:
        return False

    # Graph Initalization
    inDegree = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}

    # Graph Construction
    for parent, child in prerequisites:
        graph[parent].append(child)
        inDegree[child] += 1

    # Finding out pure-sources
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # Iterating to created the sorted task list
    while sources:
        source = sources.popleft()
        sortedOrder.append(source)

        for downstream_task in graph[source]:
            inDegree[downstream_task] -= 1
            if inDegree[downstream_task] == 0:
                sources.append(downstream_task)

    # Check if the scheduling is possible, i.e. construction of DAG
    if len(sortedOrder) != tasks:
        return False

    return True

def main():
    print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
