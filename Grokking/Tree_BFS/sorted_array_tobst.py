# Constructing Binary Search Tree (BST) from a sorted array

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preOrderTraversal(root):
    stack = [root]
    while stack:
        popped = stack.pop()
        print (popped.data, end=' -> ')
        if popped.right:
            stack += popped.right,
        if popped.left:
            stack += popped.left,
    return

def inOrderTraversal(root):
    if not root:
        return

    stack, current = [], root
    while stack or current:
        if current:
            stack += current,
            current = current.left
        else:
            popped = stack.pop()
            print (popped.data, end=' -> ')
            current = popped.right
    return

def postOrderTraversal(root):
    if not root:
        return

    stack, stack_reverse = [root], []
    while stack:
        popped = stack.pop()
        stack_reverse += popped,
        if popped.left:
            stack += popped.left,
        if popped.right:
            stack += popped.right,

    while stack_reverse:
        print (stack_reverse.pop().data, end=' -> ')
    pass

def sortedArrayToBst(arr):
    if not arr:
        return None
    mid = (len(arr) // 2)
    
    root = Node(arr[mid])
    root.left = sortedArrayToBst(arr[:mid])
    root.right = sortedArrayToBst(arr[mid+1:])
    return root

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    root = sortedArrayToBst(arr)
    print ("Inorder Traversal of BST : ")
    inOrderTraversal(root)
    print()
    print ("Preorder Traversal of BST : ")
    preOrderTraversal(root)
    print()
    print ("Postorder Traversal of BST : ")
    postOrderTraversal(root)
    print()
