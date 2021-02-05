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



def main():
    print("Topological sort: " +
        str(topological_sort(4, [[3, 0], [3, 2], [0, 2], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

main()
