# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of connecting two ropes is equal to the sum of their lengths.
import unittest
from heapq import heappush, heappop

def rope_connect_min_cost(ropes):
    # Time Complexity: O(NLogN), Space Complexity: O(N)
    costMap = []
    for rope in ropes:
        heappush(costMap, rope)

    connection_cost = 0
    while len(costMap) > 1:
        popped_left = heappop(costMap)
        popped_right = heappop(costMap)
        connection_cost += (popped_left + popped_right)
        heappush(costMap, (popped_left + popped_right))

    return connection_cost

class Test(unittest.TestCase):
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_1(self):
        self.assertEqual(rope_connect_min_cost([1, 3, 11, 5]), 33)
    def test_2(self):
        self.assertEqual(rope_connect_min_cost([3, 4, 5, 6]), 36)
    def test_3(self):
        self.assertEqual(rope_connect_min_cost([1, 3, 11, 5, 2]), 42)

if __name__ == '__main__':
    unittest.main()
