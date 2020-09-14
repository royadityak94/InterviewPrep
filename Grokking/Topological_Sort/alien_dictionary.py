# Write a method to find the correct order of the alphabets in the alien language. It is given that the input is a valid dictionary and there exists an ordering among its alphabets.
from collections import deque

def find_order(words):
    # Time Complexity: O(V+N), Space Complexity: O(V+N);
    # V: Character count, N: Number of words in the input
    sortedOrder = []
    if len(words) == 0:
        return ""
    # Graph Initalization
    graph, inDegree = {}, {}
    for word in words:
        for character in word:
            if character not in graph:
                graph[character] = []
                inDegree[character] = 0

    # Graph Construction
    for i in range(len(words)-1):
        set1, set2 = words[i], words[i+1]
        for j in range(min(len(set1), len(set2))):
            if set1[j] != set2[j]:
                graph[set1[j]].append(set2[j])
                inDegree[set2[j]] += 1
                break

    # Finding non-dependent nodes
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # Iterating to populate downstream dependencies
    while sources:
        source = sources.popleft()
        sortedOrder.append(source)
        for child in graph[source]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # Checking for non-cyclicity or DAG
    if len(sortedOrder) != len(inDegree):
        return ""
    return "".join(sortedOrder)

def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))

main()
