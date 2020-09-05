# BST Warm: Insertion, Deletion, Search
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self, data):
        self.root = Node(data)
    def insert(self, data):
        return self.insert_utility(self.root, data)
    def insert_utility(self, current, data):
        if current.data < data:
            if not current.right:
                current.right = Node(data)
            else:
                return self.insert_utility(current.right, data)
        else:
            if not current.left:
                current.left = Node(data)
            else:
                return self.insert_utility(current.left, data)
    def inorder_traversal(self, current):
        if not current:
            return
        self.inorder_traversal(current.left)
        print (current.data, end='-')
        self.inorder_traversal(current.right)
    def search(self, searchable):
        return self.search_utility(self.root, searchable)
    def search_utility(self, current, searchable):
        if not current:
            return False
        if current.data == searchable:
            return True
        if current.data < searchable:
            return self.search_utility(current.right, searchable)
        else:
            return self.search_utility(current.left, searchable)
    def is_bst_satisfied(self):
        def helper(head, lower=float('-inf'), upper=float('inf')):
            if not head:
                return True
            data = head.data
            if not (data >= lower and data <= upper):
                return False
            if not helper(head.right, data, upper):
                return False
            if not helper(head.left, lower, data):
                return False

            return True
        return helper(self.root)

def main():
    bst = BinarySearchTree(10)
    bst.insert(3)
    bst.insert(1)
    bst.insert(25)
    bst.insert(9)
    bst.insert(13)
    bst.inorder_traversal(bst.root)
    print ()

    print("BST Satisfied ? ", bst.is_bst_satisfied())

    print("12 in BST ?", bst.search(12))
    print("25 in BST ?", bst.search(25))
    print("9 in BST ?", bst.search(9))

    # Check for BST alone
    tree = BinarySearchTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(8)
    print("BST Satisfied ? ", tree.is_bst_satisfied())

main()
