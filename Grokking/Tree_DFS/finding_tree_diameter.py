# Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes.
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    def find_max_height(self, root, depth=0):
        if not root:
            return depth
        return max(self.find_max_height(root.left, depth+1),
            self.find_max_height(root.right, depth+1))
        return depth

    def find_diameter(self, root):
        # Time Complexity: O(N), Space Complexity: O(N)
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, root):
        if not root:
            return 0
        leftDiameter = self.calculate_height(root.left)
        rightDiameter = self.calculate_height(root.right)
        diameter = leftDiameter + rightDiameter + 1
        self.treeDiameter = max(self.treeDiameter, diameter)

        return max(leftDiameter, rightDiameter) + 1

def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))

main()
