# Given the number of tasks and a list of prerequisite pairs, write a method to print >>all possible ordering<< of tasks meeting all prerequisites.
from collections import deque

def print_orders(tasks, prerequisites):
    # Time = Space (Complexity) : O(V! * E)
    sortedOrder = []
    if tasks <= 0:
        return sortedOrder
    # ------- Formulating the problem as a graph problem
    # Graph Initalization
    inDegree = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}

    # Graph Construction
    for parent, child in prerequisites:
        graph[parent].append(child)
        inDegree[child] += 1

    # Loading all the pure sources (independent tasks)
    sources = deque()
    for node in inDegree:
        if inDegree[node] == 0:
            sources.append(node)

    print_all_topological_orders(graph, inDegree, sources, sortedOrder)

def print_all_topological_orders(graph, inDegree, sources, sortedOrder):
    if sources:
        for vertex in sources:
            sortedOrder.append(vertex)
            sourcesNextCycle = deque(sources)
            sourcesNextCycle.remove(vertex)

            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sourcesNextCycle.append(child)

            print_all_topological_orders(graph, inDegree, sourcesNextCycle, sortedOrder)

            # Backtracking by removing the current vertex and considering all its children
            sortedOrder.remove(vertex)
            for child in graph[vertex]:
                inDegree[child] += 1


    if len(sortedOrder) == len(graph):
        print (sortedOrder)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
