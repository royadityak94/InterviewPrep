# Computing sum of paths (root-> leaf) for a given binary tree
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def all_paths(self, root):
        # Time Complexity: O(N), Space Complexity: O(N)
        all_path_sum = [0]
        self.all_paths_recursive(root, 0, all_path_sum)
        return all_path_sum
    def all_paths_recursive(self, node, current_path_sum, all_path_sum):
        if not node:
            return
        current_path_sum = (current_path_sum*10) + node.data
        if not node.left and not node.right:
            all_path_sum[0] += current_path_sum
        else:
            self.all_paths_recursive(node.left, current_path_sum, all_path_sum)
            self.all_paths_recursive(node.right, current_path_sum, all_path_sum)

def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(6)
    print ("All Path Sum : ", root.all_paths(root))

main()
