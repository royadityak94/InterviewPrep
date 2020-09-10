# Python program to find the sum of left and right sides, and to print them individually
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)
    def preorder_traversal(self, node):
        if not node:
            return
        self.preorder_traversal(node.left)
        print (node.data, end='-')
        self.preorder_traversal(node.right)
    def branches_traversal(self, node):
        if not node or node == self.root:
            return
        self.branches_traversal(node.left)
        print (node.data, end='-')
        self.branches_traversal(node.right)

def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(15)

    tree.preorder_traversal(tree.root)

    print ("\nPrinting on all left side of root ...")
    tree.branches_traversal(tree.root.left)
    print ("\nPrinting all on right side of root ...")
    tree.branches_traversal(tree.root.right)
    print ()
    print ()

    # Another version
    tree = BinaryTree(12)
    tree.root.left = Node(10)
    tree.root.right = Node(20)
    tree.root.right.left = Node(25)
    tree.root.right.right = Node(40)
    tree.root.right.right.left = Node(35)

    tree.preorder_traversal(tree.root)
    print ("\nPrinting all left sides ...")
    tree.branches_traversal(tree.root.left)
    print ()
    print ("Printing all right sides ...")
    tree.branches_traversal(tree.root.right)
    print ()

main()
