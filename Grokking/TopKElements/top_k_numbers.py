import unittest
from heapq import heappush, heappop

def find_topK_numbers(arr, k):
    # Time Complexity: O(NLogK), Space Complexity: O(K)
    topK = []

    for ele in enumerate(arr):
        if len(topK) < k:
            heappush(topK, ele)
        else:
            if ele > topK[0]:
                heappop(topK)
                heappush(topK, ele)
    return list(topK)

class Test (unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(find_topK_numbers([3, 1, 5, 12, 2, 11], 3), [5, 12, 11])
    def test_2(self):
        self.assertEqual(find_topK_numbers([5, 12, 11, -1, 12], 3), [11, 12, 12])


if __name__ == '__main__':
    unittest.main()
