# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.
from heapq import heappush, heappop
import unittest

def find_sum_of_elements(nums, k1, k2):
    # Time Complexity: O(NLogN), Space Complexity: O(N)
    minHeap = []

    for ele in nums:
        heappush(minHeap, ele)
    cnt = 0
    while cnt < k1:
        heappop(minHeap)
        cnt += 1

    desired_sum = 0
    for _ in range(k1, k2-1):
        desired_sum += heappop(minHeap)
    return desired_sum



class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6), 23)
    def test_2(self):
        self.assertEqual(find_sum_of_elements([3, 5, 8, 7], 1, 4), 12)

if __name__ == '__main__':
    unittest.main()
