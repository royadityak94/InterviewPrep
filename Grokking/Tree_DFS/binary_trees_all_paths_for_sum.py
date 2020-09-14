# python program to find all paths with the requisite sum
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def all_paths(self, root, sum):
        all_paths = []
        self.all_paths_recursive(root, sum, [], all_paths)
        return all_paths
    def all_paths_recursive(self, current_node, required_sum, current_path, all_paths):
        # Time Complexity: O(N^2)~O(NLogN), Space Complexity: O(N)
        if not current_node:
            return
        current_path.append(current_node.data)

        if current_node.data == required_sum and not current_node.left and not current_node.right:
            all_paths.append(list(current_path))
        else:
            self.all_paths_recursive(current_node.left, required_sum-current_node.data, current_path, all_paths)
            self.all_paths_recursive(current_node.right, required_sum-current_node.data, current_path, all_paths)
        del current_path[-1]

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(root.all_paths(root, required_sum)))

main()
