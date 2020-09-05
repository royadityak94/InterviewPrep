# Python program to find minimum in a tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left  = self.right = None

    def insert(self, val):
        if val < self.val:
            if self.leftChild:
                self.leftChild.insert(val)
            else:
                self.leftChild = Node(val)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(val)
            else:
                self.rightChild = Node(val)
                return
    def search(self, val):
        if val < self.val:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return False
        elif val > self.val:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return False
        else:
            return True
        return False

    def delete(self, val):
        '''
        if current node's val is less than that of root node, then
        only search in left subtree otherwise right subtree
        '''
        if val < self.val:
            if(self.leftChild):
                self.leftChild = self.leftChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        elif val > self.val:
            if(self.rightChild):
                self.rightChild = self.rightChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        else:
            # deleting node with no children
            if self.leftChild is None and self.rightChild is None:
                self = None
                return None
            # deleting node with right child
            elif self.leftChild is None:
                tmp = self.rightChild
                self = None
                return tmp
            # deleting node with left child
            elif self.rightChild is None:
                tmp = self.leftChild
                self = None
                return tmp
            # deleting node with two children
            else:
                # first get the inorder successor
                current = self.rightChild
                # loop down to find the leftmost leaf
                while(current.leftChild is not None):
                    current = current.leftChild
                self.val = current.val
                self.rightChild = self.rightChild.delete(current.val)

        return self



class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def delete(self, data):
        if self.root is not None:
            self.root = self.root.delete(data)
    def search(self, data):
        if self.root:
            return self.root.search(data)
        return False

def findMin(root):
    if root is None:
        return root
    elif root.left is None:
        return root.val
    else:
        return findMin(root.left)

def main():
    BST = BinarySearchTree(6)
    BST.insert(20)
    BST.insert(-1)
    print (findMin(BST.root))

main()
