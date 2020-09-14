# Solving variant of all sum paths with binary trees
# Problem 1: Given a binary tree, return all root-to-leaf paths.
# Problem 2: Given a binary tree, find the root-to-leaf path with the maximum sum.
# Problem 3: Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def all_paths(self, root):
        # Time Complexity: O(N^2), Space Complexity: O(N)
        all_paths = []
        self.all_paths_recursive(root, [], all_paths)
        return all_paths
    def all_paths_recursive(self, node, current_path, all_paths):
        if not node:
            return all_paths
        current_path.append(node.data)
        if not node.left and not node.right:
            all_paths.append(list(current_path))
        else:
            self.all_paths_recursive(node.left, current_path, all_paths)
            self.all_paths_recursive(node.right, current_path, all_paths)
        del current_path[-1]
    def all_paths_max_sum(self, root):
        max_sum = [float('-inf')]
        self.all_paths_max_sum_recursive(root, 0, max_sum)
        return max_sum[0]

    def all_paths_max_sum_recursive(self, node, current_sum, max_sum):
        if not node:
            return
        current_sum += node.data
        if not node.left and not node.right and current_sum > max_sum[0]:
            max_sum[0] = current_sum
        else:
            self.all_paths_max_sum_recursive(node.left, current_sum, max_sum)
            self.all_paths_max_sum_recursive(node.right, current_sum, max_sum)
    def find_path_presence(self, root, path):
        # Time Complexity: O(N), Space Complexity: O(N)
        status = [False]
        self.find_path_presence_recursive(root, [], path, status)
        return status[0]
    def find_path_presence_recursive(self, node, current_path, path, status):
        if not node:
            return False
        current_path.append(node.data)
        if not node.left and not node.right and current_path == path:
            status[0] = True
        else:
            self.find_path_presence_recursive(node.left, current_path, path, status)
            self.find_path_presence_recursive(node.right, current_path, path, status)
        del current_path[-1]

def main():
    root = TreeNode(4)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(15)
    # Solving Problem - 1
    print ("All paths : ", root.all_paths(root))
    # Solving Problem - 2 (max_sum)
    print ("Max Sum across All paths : ", root.all_paths_max_sum(root))
    # Solving Problem - 3
    search_path_sequences = [[4, 7, 6], [4, 1, 13], [12, 7, 4], [4, 1, 11]]
    for path in search_path_sequences:
        status = root.find_path_presence(root, path)
        print ("Path %s found '%s' in the binary tree" % (str(path), str(status)))

main()
