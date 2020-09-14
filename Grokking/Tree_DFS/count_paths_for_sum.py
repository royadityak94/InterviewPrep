# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

def count_possible_sums(arr, desired_sum):
    path_sum = matches = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == desired_sum:
            matches += 1
            path_sum = 0
        else:
            path_sum += arr[i]
            if path_sum == desired_sum:
                matches += 1
                path_sum = arr[i]
            elif path_sum > desired_sum:
                path_sum = arr[i]
    return matches

def count_in_path_sum(arr, desired_sum):
    # Avoids repeated counting
    path_sum = matches = 0
    for i in range(len(arr)-1, -1, -1):
        path_sum += arr[i]
        if path_sum == desired_sum:
            matches += 1
    return matches

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def count_paths(self, root, requisite_sum):
        # Time Complexity: O(N), Space Complexity: O(N^2) ~ O(NLogN) [for balanced tree]
        total_paths = [0]
        self.count_paths_recursive(root, [], total_paths, requisite_sum)
        return total_paths[0]
    def count_paths_recursive(self, node, current_path, total_paths, requisite_sum):
        if not node:
            return
        current_path.append(node.data)
        if count_in_path_sum(current_path, requisite_sum) > 0:
            total_paths[0] += 1
        self.count_paths_recursive(node.left, current_path, total_paths, requisite_sum)
        self.count_paths_recursive(node.right, current_path, total_paths, requisite_sum)
        del current_path[-1]

def main():
    root = TreeNode(4)
    root.left = TreeNode(7)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(15)

    requisite_sum = 11
    print ("Total paths matching requisite sum: ", root.count_paths(root, requisite_sum))s

main()
