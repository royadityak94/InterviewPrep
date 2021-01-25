# Python program to output list of lists for tree order traversal'
from collections import deque

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class TreeNode(object):
    def __init__(self, data):
        self.root = Node(data)

    # def traverse_level_order(self, root):
    #     # Time Complexity: O(N), Space Complexity: O(N)
    #     stack = deque()
    #     current = root
    #     while stack:
    #         while current:
    #             stack += current,
    #             cucrent = current.left
    #         node = stack.pop()
    #         print (node.data)
    #         node = node.right

    def traverse_level_order(self, root):
        # Time Complexity: O(N), Space Complexity: O(N)
        stack = deque()
        returned = []
        current = root
        while stack or current:
            if current:
                stack += current,
                cucrent = current.left
            else:
                node = stack.pop()
                print (node.data)
                returned += node.data,
                cucrent = node.right
        return returned

def main():
    tree = TreeNode(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    print("Level order traversal: " + str(tree.traverse_level_order(tree.root)))

main()
