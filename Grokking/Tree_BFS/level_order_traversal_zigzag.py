# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
from collections import deque

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class TreeNode(object):
    def __init__(self, data):
        self.root = Node(data)

    def traverse_level_order_zigzag(self, root):
        # Time Complexity: O(N), Space Complexity: O(N)
        traversed_levels = []
        queue = deque()
        queue.append(root)
        order = 1

        while queue:
            levelSize = len(queue)
            currentLevel = []

            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.data)

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

            if order == -1:
                currentLevel.reverse()
            order *= -1
            traversed_levels.append(currentLevel)

        return traversed_levels

def main():
    tree = TreeNode(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    tree.root.right.left.left = Node(20)
    tree.root.right.left.right = Node(17)
    print("Level order traversal: " + str(tree.traverse_level_order_zigzag(tree.root)))

main()
