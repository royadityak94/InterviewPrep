# Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
from collections import deque

class Node:
    def __init__(self, data, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
    def tree_right_view(self, root):
        queue = deque()
        queue.append(root)
        right_nodes  = []

        while queue:
            levelSize = len (queue)
            for i in range(levelSize):
                currentNode = queue.popleft()
                if i == levelSize - 1:
                    right_nodes.append(currentNode)

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)
        return right_nodes
    def tree_left_view(self, root):
        queue = deque()
        queue.append(root)
        left_nodes = []

        while queue:
            levelSize = len(queue)

            for i in range(levelSize):
                currentNode = queue.popleft()
                if i == 0:
                    left_nodes.append(currentNode)

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)
        return left_nodes

def main():
    # tree = BinaryTree(12)
    # tree.root.left = Node(7)
    # tree.root.right = Node(1)
    # tree.root.left.left = Node(9)
    # tree.root.right.left = Node(10)
    # tree.root.right.right = Node(5)
    # tree.root.left.left.right = Node(3)

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.left = Node(8)

    right_nodes = tree.tree_right_view(tree.root)
    print("Tree right view: ", end='')
    for node in right_nodes:
        print(str(node.data) + " ", end='')
    print ()

    left_nodes = tree.tree_left_view(tree.root)
    print("Tree right view: ", end='')
    for node in left_nodes:
        print(str(node.data) + " ", end='')
    print ()

main()
