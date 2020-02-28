# Python program to complete the implementation of Kadane's Algorithm
# wherein maximum contigous sum of an array is based on the sum seen till now,
# and the current element. Runtime - O(n)

# importing the required packages
import unittest

def kadane_implementation(arr):
    local_sum = arr[0]
    global_sum = local_sum
    for i in range(1, len(arr)):
        local_sum = max(arr[i], local_sum+arr[i])
        global_sum = max(global_sum, local_sum)
    return global_sum

class Test(unittest.TestCase):
    def test_case1(self):
        arr = [-2, -3, 4, -1, -2, 1, 5, -3]
        self.assertEqual(kadane_implementation(arr), 7)
    def test_case2(self):
        arr = [6, 3, -1, -10, -9, 18]
        self.assertEqual(kadane_implementation(arr), 18)

if __name__ == '__main__':
    unittest.main()
