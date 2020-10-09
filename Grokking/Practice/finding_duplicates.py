import unittest

def findDuplicates(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            finder = 0
            while finder != slow:
                slow = nums[slow]
                finder = nums[finder]
            return finder

class Test(unittest.TestCase):
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_1(self):
        self.assertEqual(findDuplicates([1, 3, 4, 2, 2]), 2)
    def test_2(self):
        self.assertEqual(findDuplicates([1, 2, 3, 4, 1, 5]), 1)

if __name__ == '__main__':
    unittest.main()
