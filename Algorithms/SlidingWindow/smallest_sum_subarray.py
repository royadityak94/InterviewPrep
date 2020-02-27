# Python program to compute the smallest subarray with a given sum
import unittest
import math

def smallest_sum_subarray(arr, max_sum):
    start = 0
    smallest_window = math.inf
    present_window = 0

    for end in range(len(arr)):
        present_window += arr[end]

        while present_window >= max_sum:
            smallest_window = min(smallest_window, (end-start+1))
            present_window -= arr[start]
            start += 1
    return smallest_window

class Test(unittest.TestCase):
    def test_case1(self):
        arr = [2, 1, 5, 2, 3, 1]
        self.assertEqual(smallest_sum_subarray(arr, 7), 2)

    def test_case2(self):
        arr = [1, 4, 2, -1, 3, 5]
        self.assertEqual(smallest_sum_subarray(arr, 9), 4)

if __name__ == '__main__':
    unittest.main()
