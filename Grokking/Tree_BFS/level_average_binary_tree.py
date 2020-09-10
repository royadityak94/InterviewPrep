# Given a binary tree, populate an array to represent the averages of all of its levels.
from collections import deque

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)

    def find_level_averages(self, root):
        # Time Complexity: O(N), Space Complexity : O(N),
        level_averages = []

        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)
            currentLevel = 0
            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentLevel += currentNode.data

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)
            level_averages.append(currentLevel/levelSize)
        return level_averages

    def find_largest_value_each_level(self, root):
        # Time Complexity: O(N), Space Complexity: O(N) {Max N/2 nodes at any level}
        maximum_level = []
        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)
            maximum = float('-inf')
            for _ in range(levelSize):
                currentNode = queue.popleft()
                maximum = max(maximum, currentNode.data)
                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)
            maximum_level.append(maximum)
        return maximum_level

def main():
    tree = BinaryTree(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.left.right = Node(2)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    print ("Level Averages: ", tree.find_level_averages(tree.root))
    print ("Level Maximum: ", tree.find_largest_value_each_level(tree.root))

main()
