# Given a binary tree and a node, find the level order successor of the given node in the tree.
from collections import deque

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)

    def find_successor(self, root, searchable):
        # Time Complexity: O(N), Space Complexity: O(N) {Max N/2 node at any level}
        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)

            for _ in range(levelSize):
                currentNode = queue.popleft()

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

                if currentNode.data == searchable:
                    return queue.popleft()
        return -1


def main():
    tree = BinaryTree(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    result = tree.find_successor(tree.root, 12)
    if result:
        print(result.data)
    result = tree.find_successor(tree.root, 9)
    if result:
        print(result.data)

main()
