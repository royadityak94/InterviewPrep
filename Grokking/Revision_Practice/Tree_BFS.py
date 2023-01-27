"""Practice BFS using Tree"""
class Node: 
    def __init__(self, value, left=None, right=None):
        self.value = value 
        self.left = left 
        self.right = right

def print_tree(root):
    print ('Tree: ')
    stack = [root]
    while stack:
        current = stack.pop(0)
        print (current.value, end='->')
        if current.left:
            stack += current.left, 
        if current.right: 
            stack += current.right,
        
    print()

def invert_tree(root):
    if not root:
        return 
    invert_tree(root.left)
    invert_tree(root.right)
    root.left, root.right = root.right, root.left

def main():
    tree = Node(12)
    tree.left = Node(7)
    tree.left.left = Node(9)
    tree.left.right = Node(8)
    tree.left.left.left = Node(2)
    tree.left.left.right = Node(3)
    tree.right = Node(1) # Right Tree
    tree.right.left = Node(10)
    tree.right.right = Node(5)

    # Print Tree 
    print_tree(tree)

    # Invert Tree
    invert_tree(tree)
    print_tree(tree)

main()