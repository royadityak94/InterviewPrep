#Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
import unittest
from heapq import heappush, heappop
from collections import Counter

def find_k_frequent_numbers(arr, k):
    # Time Complexity: O(N + NLogK + K), Space Complexity: O(N)
    countMap = Counter(arr)
    occurrences = []

    for key in countMap.keys():
        heappush(occurrences, (countMap[key], key))
        if len(occurrences) > k:
            heappop(occurrences)

    # Preparing the returnable list
    frequent_numbers = []
    while occurrences:
        frequent_numbers += heappop(occurrences)[1],

    return frequent_numbers

class Test(unittest.TestCase):
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_1(self):
        self.assertEqual(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2), [11, 12])
    def test_2(self):
        self.assertEqual(find_k_frequent_numbers([5, 12, 11, 3, 11], 2), [12, 11])

if __name__ == '__main__':
    unittest.main()
