# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaximumPathSum:
    def find_maximum_path_sum(self, root):
        # Time Complexity: O(N), Space Complexity: O(N)
        self.global_maximum_sum = float('-inf')
        self.find_maximum_path_sum_recursive(root)
        return self.global_maximum_sum
    def find_maximum_path_sum_recursive(self, node):
        if not node:
            return 0

        leftPathSum = self.find_maximum_path_sum_recursive(node.left)
        rightPathSum = self.find_maximum_path_sum_recursive(node.right)
        leftPathSum = max(leftPathSum, 0)
        rightPathSum = max(rightPathSum, 0)

        localMaxSum = leftPathSum + rightPathSum + node.val
        self.global_maximum_sum = max(self.global_maximum_sum, localMaxSum)

        return max(leftPathSum, rightPathSum) + node.val


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    maximumPathSum = MaximumPathSum()
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
    #
    # root = TreeNode(-1)
    # root.left = TreeNode(-3)
    # print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

main()
