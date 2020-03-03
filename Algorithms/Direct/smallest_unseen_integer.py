# Python program to implement the smallest unseen integer
import unittest

def return_smallest_integer(arr):
    smallest_unseen = 1
    for ele in sorted(arr):
        if ele == smallest_unseen:
            smallest_unseen += 1
        elif ele > smallest_unseen:
            return smallest_unseen
    return smallest_unseen

class Test(unittest.TestCase):
    def test_case1(self):
        arr = [-1, -3]
        self.assertEqual(return_smallest_integer(arr), 1)
    def test_case2(self):
        arr = [1, 3, 6, 4, 1, 2]
        self.assertEqual(return_smallest_integer(arr), 5)
    def test_case3(self):
        arr = [1, 2, 3]
        self.assertEqual(return_smallest_integer(arr), 4)

if __name__ == '__main__':
    unittest.main()
