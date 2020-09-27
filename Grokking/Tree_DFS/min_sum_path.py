class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = self.right = None
    def __lt__(self, other):
        return self.data < other.data

def min_path_sum(node):
    if not node:
        return
    min_sum = [float('inf')]
    min_path_sum_recursive(node, 0, min_sum)
    return min_sum[0]

def min_path_sum_recursive(node, current_sum, min_sum):
    if not node:
        return 0
    current_sum += node.data
    if not node.left and not node.right:
        min_sum[0] = min(min_sum[0], current_sum)
    min_path_sum_recursive(node.left, current_sum, min_sum)
    min_path_sum_recursive(node.right, current_sum, min_sum)

def min_path_sum2(node):
    if not node:
        return 0
    return min(node.data + min_path_sum2(node.left), node.data + min_path_sum2(node.right))

def main():
    root = TreeNode(0)
    root.left = TreeNode(5)
    root.left.left = TreeNode(14)

    root.right = TreeNode(6)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(16)
    print ("Path with min sum : ", min_path_sum(root))
    print ("Path with min sum : ", min_path_sum2(root))

main()
