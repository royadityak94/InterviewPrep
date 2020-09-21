from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def print_tree(self):
        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            print (current.data, " -> ", end='')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print ()

    def print_tree_dfs(self):
        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.pop()
            print (current.data, " -> ", end='')
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        print()

    def invert_binary_tree(self, root):
        if not root:
            return
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        root.left, root.right = root.right, root.left

    def invert_binary_tree_iterative(self, root):
        if not root:
            return

        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right

def main():
    tree = BinaryTree(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.left.right = Node(8)

    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    tree.root.left.left.left = Node(2)
    tree.root.left.left.right = Node(3)

    tree.print_tree()
    tree.print_tree_dfs()
    tree.invert_binary_tree_iterative(tree.root)
    tree.print_tree()
    tree.print_tree_dfs()

main()
