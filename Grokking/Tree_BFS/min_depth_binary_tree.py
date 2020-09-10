# Python program to find the minimum depth of a binary tree
from collections import deque

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)

    def isLeafNode(self, node):
        if node.left is None and node.right is None:
            return True
        return False

    def finding_minimum_depth(self, root):
        # Time Complexity: O(N), Space Complexity: O(N)
        queue = deque()
        queue.append(root)
        depth = 1

        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if self.isLeafNode(currentNode):
                    return depth
                else:
                    if currentNode.left:
                        queue.append(currentNode.left)
                    if currentNode.right:
                        queue.append(currentNode.right)
            depth += 1
        return -1

def main():
    tree = BinaryTree(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    print("Tree Minimum Depth: " + str(tree.finding_minimum_depth(tree.root)))
    tree.root.left.left = Node(9)
    tree.root.right.left.left = Node(11)
    print("Tree Minimum Depth: " + str(tree.finding_minimum_depth(tree.root)))
main()
