# Write a method to find the correct order of the alphabets in the alien language. It is given that the input is a valid dictionary and there exists an ordering among its alphabets.
from collections import deque

# O(V+E) time | O(V+N) space
def find_order(words):
    if not words:
        return ''

    # Initializing graph and inDegree
    graph = {}
    inDegree = {}
    for word in words:
        for ch in word:
            graph[ch] = []
            inDegree[ch] = 0

    # Building the graphs
    for i in range(len(words)-1):
        word1, word2 = words[i], words[i+1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                graph[word1[j]] += word2[j],
                inDegree[word2[j]] += 1
                break

    # Populating the sources
    sources = deque()
    for vertex in inDegree:
        if not inDegree[vertex]:
            sources += vertex,

    # Iterating over the sources
    final_word = []
    while sources:
        vertex = sources.popleft()
        final_word += vertex,
        for child in graph[vertex]:
            inDegree[child] -= 1
            if not inDegree[child]:
                sources += child,

    print (">> ", final_word)
    if len(final_word) != len(inDegree):
        return ''
    return ''.join(final_word)

def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))

main()
