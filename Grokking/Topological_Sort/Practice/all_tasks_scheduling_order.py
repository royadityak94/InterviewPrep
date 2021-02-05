# Given the number of tasks and a list of prerequisite pairs, write a method to print >>all possible ordering<< of tasks meeting all prerequisites.
from collections import deque

# O(V!E) time | O(V!E) space
def print_orders(vertices, edges):
    sortedOrder = []
    if not vertices:
        return sortedOrder

    # Initialize graph and indegree
    graph = {i:[] for i in range(vertices)}
    inDegree = {i:0 for i in range(vertices)}

    # Build the graph
    for parent, child in edges:
        graph[parent] += child,
        inDegree[child] += 1

    # Initialize sources
    sources = deque()
    for vertex in range(vertices):
        if not inDegree[vertex]:
            sources += vertex,

    all_orders = []
    # Recursively populate the sorted ordering
    populate_sorted_orders(graph, inDegree, sources, sortedOrder, all_orders)
    print (len(all_orders), all_orders)

def populate_sorted_orders(graph, inDegree, sources, sortedOrder, all_orders):
    if sources:
        for vertex in sources:
            sortedOrder += vertex,
            futureSources = deque(sources)
            futureSources.remove(vertex)

            for child in graph[vertex]:
                inDegree[child] -= 1
                if not inDegree[child]:
                    futureSources += child,
            populate_sorted_orders(graph, inDegree, futureSources, sortedOrder, all_orders)
            sortedOrder.remove(vertex)
            for child in graph[vertex]:
                inDegree[child] += 1
    if len(sortedOrder) == len(graph):
        #print (sortedOrder)
        all_orders += sortedOrder[:],

def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
