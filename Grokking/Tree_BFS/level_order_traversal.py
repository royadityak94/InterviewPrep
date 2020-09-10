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

    def traverse_level_order(self, root):
        # Time Complexity: O(N), Space Complexity: O(N)
        queue = deque()
        queue.append(root)
        level_order_traversal = []

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
            level_order_traversal.append(currentLevel)
        return level_order_traversal

def main():
    tree = TreeNode(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    print("Level order traversal: " + str(tree.traverse_level_order(tree.root)))

main()
