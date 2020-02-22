# Shortest path implementation using 'Floyd-Warshall' Algorithm
#Importing the required packages
import unittest
import numpy as np

def floyd_warshall(w):
    n = len(w)
    arr = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            arr[i, j] = fwr(w, n, i, j)
    return arr

def fwr(w, k, i, j):
    if k==0:
        return w[i-1][j-1]
    else:
        return (min(
        fwr(w, k-1, i, j),
        fwr(w, k-1, i, k) + fwr(w, k-1, k, j)
        ))


class Test(unittest.TestCase):
    def test_floyd_warshall(self):
        INF = 99999999999999999
        graph = [[0,5,INF,10], [INF,0,3,INF], [INF,INF,0,1], [INF,INF,INF,0]]
        print(floyd_warshall(graph))
        
if __name__ == '__main__':
    unittest.main()
