# Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.
from collections import deque

def return_relevant_matching_node(graph, ele):
    for key in graph.keys():
        if ele in graph[key]:
            return key
    return -1

def can_construct(originalSeq, sequences):
    # Time Complexity : O(V+N), Space Complexity: O(V+E)
    # V: Distinct No. count, E: Number of sequences, N: Count of numbers in sequences
    if len(originalSeq) == 0 or len(sequences) == 0:
        return False

    sortedOrder = []
    graph, inDegree = {}, {}
    # Graph Construction
    for node in originalSeq:
        graph[node] = []
        inDegree[node] = 0

    # Graph Initalization
    for sequence in sequences:
        for i in range(len(sequence)-1):
            duplicate_index = return_relevant_matching_node(graph, sequence[i+1])
            if duplicate_index != -1:
                graph[duplicate_index].remove(sequence[i+1])
                inDegree[sequence[i+1]] -= 1

            graph[sequence[i]].append(sequence[i+1])
            inDegree[sequence[i+1]] += 1

    # Finding pure-sources or non-dependent nodes
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # Iterating to populate downstream dependencies
    while sources and len(sources) == 1:
        source = sources.popleft()
        sortedOrder.append(source)
        for child in graph[source]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    if sortedOrder != originalSeq:
        return False
    return True

def main():
    print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))

main()
