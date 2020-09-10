# Python program to separately traverse left and right side of the root node
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)
    def isLeaf(self, node):
        if not node:
            return False
        if node.left is None and node.right is None:
            return True
        return False
    def traverse_left_side(self, node):
        sum = 0
        if not node or node == self.root.right:
            return sum

        # Parsing the left branches
        if self.isLeaf(node.left):
            sum += node.left.data
        else:
            sum += self.traverse_left_side(node.left)

        sum += node.data
        # Parsing the right branches
        if self.isLeaf(node.right):
            sum += node.right.data
        else:
            sum += self.traverse_left_side(node.right)
        return sum

    def traverse_right_side(self, node):
        sum = 0
        if not node or node == self.root.left:
            return sum

        # Parsing the left branches
        if self.isLeaf(node.left):
            sum += node.left.data
        else:
            sum += self.traverse_right_side(node.left)

        sum += node.data

        # Parsing the right branches
        if self.isLeaf(node.right):
            sum += node.right.data
        else:
            sum += self.traverse_right_side(node.right)

        return sum

def main():
    # Scenario - 1
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(8)
    tree.root.right.right.left = Node(7)

    left_sum = tree.traverse_left_side(tree.root.left)
    right_sum = tree.traverse_right_side(tree.root.right)

    if left_sum == right_sum:
        print (-1)
    elif left_sum < right_sum:
        print (">>> Tree is skewed towards the right")
    else:
        print (">>> Tree is skewed towards the left")

    # Scenario - 2
    tree = BinaryTree(35)
    tree.root.left = Node(25)
    tree.root.right = Node(45)
    tree.root.left.left = Node(10)
    tree.root.left.right = Node(15)
    tree.root.left.left.left = Node(7)

    left_sum = tree.traverse_left_side(tree.root.left)
    right_sum = tree.traverse_right_side(tree.root.right)

    if left_sum == right_sum:
        print (-1)
    elif left_sum < right_sum:
        print (">>> Tree is skewed towards the right")
    else:
        print (">>> Tree is skewed towards the left")



main()
