# Python program to implement the smallest unseen integer
import unittest

def segregate(arr, n):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr

def return_smallest_integer_naive(arr):
    smallest_unseen = 1
    for ele in sorted(arr):
        if ele == smallest_unseen:
            smallest_unseen += 1
        elif ele > smallest_unseen:
            return smallest_unseen
    return smallest_unseen

def return_smallest_integer_hashmap(arr):
    keys = {}
    largest = 0
    for ele in arr:
        if ele > 0:
            largest = max(largest, ele)
            keys[ele] = 1
    for i in range(1, len(arr)):
        if keys.get(i) is None:
            return i
    return largest + 1

def return_smallest_integer_efficient(arr):
    n = len(arr)
    arr = segregate(arr, n)
    if not arr[-1] > 0:
        return 1

    # Change the index to negative in increasing order
    for i in range(n):
        if (abs(arr[i]) - 1) < n and arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
    for i in range(n):
        if arr[i] > 0:
            return (i+1)
    return n+1

class Test(unittest.TestCase):
    def test_case1(self):
        arr = [-1, -3]
        self.assertEqual(return_smallest_integer_efficient(arr), 1)
    def test_case2(self):
        arr = [1, 3, 6, 4, 1, 2]
        self.assertEqual(return_smallest_integer_efficient(arr), 5)
    def test_case3(self):
        arr = [1, 2, 3]
        self.assertEqual(return_smallest_integer_efficient(arr), 4)

if __name__ == '__main__':
    unittest.main()
