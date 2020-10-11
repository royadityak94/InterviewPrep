# Lowest common ancestor (LCA) - https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
import unittest

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def lowest_common_ancestor(root, a, b):
    if not root or not a or not b:
        return None

    while root:
        if a <= root.data <= b:
            return root.data
        elif root.data > a and root.data > b:
            root = root.left
        else:
            root = root.right
    return -1

class Test(unittest.TestCase):

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_1(self):
        root = Node(7)
        root.left = Node(2)
        root.left.left = Node(1)
        root.left.right = Node(5)
        root.right = Node(9)

        self.assertEqual(lowest_common_ancestor(root, 1, 9), 7)

    def test_2(self):
        root = Node(8)
        root.left = Node(3)
        root.left.left = Node(2)
        root.left.right = Node(6)
        root.right = Node(9)

        self.assertEqual(lowest_common_ancestor(root, 2, 6), 3)

    def test_3(self):
        root = Node(8)
        root.left = Node(6)
        root.right = Node(9)

        self.assertEqual(lowest_common_ancestor(root, 6, 8), 8)

if __name__ == '__main__':
    unittest.main()
