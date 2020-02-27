# Python program to implement the maximum sum sub-array problem
import unittest

def max_sum_subarray(arr, k):
    max_sum, window_sum = 0, 0
    start = 0

    for end in range(len(arr)):
        window_sum += arr[end]
        if (end-start+1) >= k:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    return max_sum

class Test(unittest.TestCase):
    def test_case1(self):
        arr = [2, 1, 5, 1, 3, 2]
        self.assertEqual(max_sum_subarray(arr, 3), 9)
    def test_case2(self):
        arr = [2, 3, 4, 1, 5]
        self.assertEqual(max_sum_subarray(arr, 2), 7)

if __name__ == '__main__':
    unittest.main()
