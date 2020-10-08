# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.
import unittest
from heapq import heappush, heappop
from collections import Counter

def find_maximum_distinct_elements(arr, k):
    # Time Complexity: O(NLogN + KLogN), Space Complexity: O(N)
    countMap = Counter(arr)
    minHeap = []
    disctinctCount = 0

    for key, freq in countMap.items():
        if freq > 1:
            heappush(minHeap, (freq, key))
        else:
            disctinctCount += 1

    # Using greedy approach we attempt to remove the least frequent items first
    while k > 0  and minHeap:
        freq, key = heappop(minHeap)
        k -= freq - 1
        if k >= 0:
            disctinctCount += 1

    if k > 0:
        disctinctCount -= k
    return disctinctCount

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2), 3)
    def test_2(self):
        self.assertEqual(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3), 2)
    def test_3(self):
        self.assertEqual(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2), 3)

if __name__ == '__main__':
    unittest.main()
