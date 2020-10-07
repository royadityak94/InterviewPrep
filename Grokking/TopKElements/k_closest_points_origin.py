# Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.
import unittest
from heapq import heappush, heappop
import math

def compute_K_closest_points(points, K):
    # Time Complexity: O(NLogK), Space Complexity: O(K)
    closest = []

    for x, y in points:
        z = math.sqrt(x**2 + y**2)
        if len(closest) < K:
            heappush(closest, (-z, x, y))
        else:
            if closest[0][0] < -z:
                heappop(closest)
                heappush(closest, (-z, x, y))
    return list(map(lambda x: [x[1], x[2]], closest))

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test1(self):
        self.assertEqual(compute_K_closest_points([[1,2],[1,3]], 1), [[1,2]])
    def test2(self):
        self.assertEqual(compute_K_closest_points([[1, 3], [3, 4], [2, -1]], 2), [[1, 3], [2, -1]])

if __name__ == '__main__':
    unittest.main()
    print (compute_K_closest_points([[1,2],[1,3]], 1))
    print (compute_K_closest_points([[1, 3], [3, 4], [2, -1]], 2))
