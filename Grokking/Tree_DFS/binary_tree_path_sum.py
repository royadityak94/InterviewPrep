# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’
from collections import deque

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def has_path(self, root, sum):
        # Time Complexity: O(N), Space Complexity: O(N)
        if not root:
            return False
        if root.data == sum and not root.left and not root.right:
            return True
        return self.has_path(root.left, sum-root.data) or self.has_path(root.right, sum-root.data)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(root.has_path(root, 23)))
  #print("Tree has path: " + str(root.has_path(root, 16)))
 # print("Tree has path: " + str(root.has_path(root, 18)))

main()
