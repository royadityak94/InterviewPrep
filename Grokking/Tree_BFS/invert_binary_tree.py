# Python program to invert binary tree
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
            node = queue.popleft()
            print (node.data, ' -> ', sep='', end='')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print ()
    def print_tree_dfs(self):
        stack = deque()
        stack.append(self.root)
        while stack:
            node = stack.pop()
            print (node.data, ' -> ', sep='', end='')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print()
    def invert_binary_tree(self, root):
        if not root:
            return
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        # Swap left, right pointers
        root.left, root.right = root.right, root.left

def main():
    tree = BinaryTree(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.right = Node(8)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    tree.root.left.left.left = Node(2)
    tree.root.left.left.right = Node(3)

    tree.print_tree()
    tree.print_tree_dfs()
    tree.invert_binary_tree(tree.root)
    tree.print_tree()
    tree.print_tree_dfs()

main()
