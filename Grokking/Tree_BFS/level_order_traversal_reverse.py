# Python program to compute the level order traversal in reverse
from collections import deque

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

class TreeNode(object):
    def __init__(self, data):
        self.root = Node(data)

    def traverse_level_order_reverse(self, root):
        # Time Complexity: O(N) {N: No. of nodes in tree}
        # Space Complexity: O(N)
        traversed_levels = []

        queue = deque()
        queue.append(root)

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

            traversed_levels.insert(0, currentLevel)
        return traversed_levels


def main():
    tree = TreeNode(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    print("Level order traversal: " + str(tree.traverse_level_order_reverse(tree.root)))

main()
