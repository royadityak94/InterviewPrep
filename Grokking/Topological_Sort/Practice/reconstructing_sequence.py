# Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.
from collections import deque

def can_construct(originalSeq, edges):
    if not edges:
        return False
    elif not originalSeq:
        return True

    # Initialize graph, inDegre
    graph = {i:[] for i in range(1, len(originalSeq)+1)}
    inDegree = {i:0 for i in range(1, len(originalSeq)+1)}
    for edge in edges:
        for j in range(1, len(edge)):
            parent, child = edge[j-1], edge[j]
            graph[parent] += child,
            inDegree[child] += 1

    # Initialize sources
    sources = deque()
    for vertex in inDegree:
        if not inDegree[vertex]:
            sources += vertex,

    # Iterating over all the edges
    sequences = []
    while sources:
        if len(sources) > 1 or originalSeq[len(sequences)] != sources[0]:
            return False
        vertex = sources.popleft()
        sequences += vertex,
        for child in graph[vertex]:
            inDegree[child] -= 1
            if not inDegree[child]:
                sources += child,
    return len(sequences) == len(originalSeq)


def main():
    print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))

main()
