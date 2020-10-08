# Python program to search in binary tree
from collections import deque

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def search(self, root, element: int) -> bool:
        if not root or not element:
            return False
        stack = [root]

        while stack:
            node = stack.pop(-1)
            if element == node.data:
                return True
            elif element < node.data:
                if node.left:
                    stack += node.left,
            else:
                if node.right:
                    stack += node.right,
        return False


def main():
    root = TreeNode(12)
    root.left = TreeNode(2)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(18)

    for ele in [-1, 0, 1, 2, 3, 4, 5, 16, 18, 21]:
        if root.search(root, ele):
            print ("\t>> Element %d present in the binary tree" % ele)
        else:
            print ("Element %d is not present in the binary tree" % ele)

main()
