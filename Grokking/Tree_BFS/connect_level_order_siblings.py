# Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
from collections import deque
from __future__ import print_function

class Node:
    def __init__(self, data, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
    def connect_level_order_siblings(self):
        # Time Complexity: O(N), Space Complexity: O(N)
        queue = deque()
        queue.append(self.root)

        while queue:
            levelSize = len(queue)
            previousNode = None

            for _ in range(levelSize):
                currentNode = queue.popleft()

                if previousNode:
                    previousNode.next = currentNode
                previousNode = currentNode

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)
        return

    def print_level_order(self):
        nextLevelRoot = self.root

        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None

            while current:
                print (str(current.data)+" ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

def main():
    tree = BinaryTree(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.left.right = Node(2)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    tree.connect_level_order_siblings()
    print("Level order traversal using 'next' pointer: ")
    tree.print_level_order()

main()
