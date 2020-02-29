'''
    Python program to implement the AVL trees, and support traversal
    Supported Traversal: PreOrder, InOrder, PostOrder
    Supports: Insertion, Deletion, Search
'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.height = 1

class AVL:

    def __init__(self):
        self.root = None

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def insert(self, root, data):
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.rightRotate(root)
        elif balance < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.left = self.rightRotate(root.left)
                return self.leftRotate(root)
        return root

    def delete(self, root, data):
        if not root or root is None:
            return root
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1:
            if not self.getBalance(root.left) < 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        elif balance < -1:
            if not self.getBalance(root.right) > 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def getMinValueNode(self, root):
        if not root or root is None:
            return root
        return self.getMinValueNode(root.left)
    def leftRotate(self, root):
        y = root.right
        temp = y.left
        y.left = root
        root.right = temp
        # Update heights
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, root):
        y = root.left
        temp = y.right
        y.right = root
        root.left = temp
        # Update heights
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def preOrder(self, root):
        if not root:
            return
        print (root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if not root:
            return
        self.preOrder(root.left)
        print (root.data, end=" ")
        self.preOrder(root.right)

    def postOrder(self, root):
        if not root:
            return
        self.preOrder(root.left)
        self.preOrder(root.right)
        print (root.data, end=" ")
    def search(self, root, data):
        if not root or root is None:
            return False
        elif data == root.data:
            return True
        elif data < root.data:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)


if __name__ == '__main__':
    to_be_inserted = [10, 20, 30, 40, 50, 45, 35, 55, 25]
    tree = AVL()
    root = tree.insert(None, to_be_inserted[0])
    for ele in to_be_inserted[1:]:
        root = tree.insert(root, ele)

    # Traverse in preOrder pattern
    tree.preOrder(root)
    print()
    tree.inOrder(root)
    print()
    tree.postOrder(root)
    print()

    searchables = [35, 41, 51, 55, 25]
    for ele in searchables:
        if tree.search(root, ele):
            print ("Element = %d found in the tree." % ele)
        else:
            print ("Couldn't find Element = %d in the tree." % ele)

    nodes_to_be_deleted = [10, 25]
    for ele in nodes_to_be_deleted:
        tree.delete(root, ele)
        print ("After deleting element=%d" % ele)
        tree.preOrder(root)
        print()
