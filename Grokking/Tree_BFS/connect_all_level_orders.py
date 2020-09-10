#Given a binary tree, connect each node with its level order successor.
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

    def connect_all_siblings(self):
        # Time Complexity: O(N), Space Complexity: O(N)
        queue = deque()
        queue.append(self.root)
        previousNode = self.root

        while queue:
            levelSize = len(queue)

            for _ in range(levelSize):
                currentNode = queue.popleft()
                if previousNode:
                    previousNode.next = currentNode
                previousNode = currentNode

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

    def print_tree(self):
        current = self.root
        print ("traversal using next pointer: ", end = '')
        while current is not None:
            print (str(current.data)+' ', end='')
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
    tree.connect_all_siblings()
    print("Level order traversal using 'next' pointer: ")
    tree.print_tree()

main()
