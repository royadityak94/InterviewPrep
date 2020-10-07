# Python program to compute the kth smallest number
import unittest
from heapq import heappush, heappop

def find_kth_smallest(arr, k):
    # Time Complexity: O(NLogK), Space Complexity: O(K)
    bottomK = []
    for ele in arr:
        if len(bottomK) < k:
            heappush(bottomK, -ele)
        else:
            if bottomK[0] < -ele:
                heappop(bottomK)
                heappush(bottomK, -ele)

    return -heappop(bottomK)

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(find_kth_smallest([1, 5, 12, 2, 11, 5], 3), 5)
    def test_2(self):
        self.assertEqual(find_kth_smallest([1, 5, 12, 2, 11, 4], 5), 11)

if __name__ == '__main__':
    unittest.main()
