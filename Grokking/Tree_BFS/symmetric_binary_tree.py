# Checking if the input tree is symmetric or not
from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
    def is_leaf(self, root):
        if not root:
            return True
        if (not root.left and not root.right):
            return True
        return False

    def is_symmetric(self, root):
        if not root:
            return
        elif self.is_leaf(root):
            return True
        elif not root.left or not root.right:
            return False

        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()

            # Condition - 1 : un-equal nodes
            if (leftNode.data != rightNode.data) :
                return False

            # Condition - 2:
            if (leftNode.left and rightNode.right):
                queue.append(leftNode.left)
                queue.append(rightNode.right)
            elif (leftNode.left or rightNode.right):
                return False

            # Condition - 3
            if  (leftNode.right and rightNode.left):
                queue.append(leftNode.right)
                queue.append(rightNode.left)

            elif (leftNode.right and rightNode.left):
                return False

        return True

def main():
    tree = BinaryTree(1)
    tree.root.left = Node(3)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(6)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(4)
    print(tree.is_symmetric(tree.root))
    tree.root.right.right.right = Node(7)
    print(tree.is_symmetric(tree.root))

main()
