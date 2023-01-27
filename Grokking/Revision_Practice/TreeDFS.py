"""Python to practice tree problems"""
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value 
        self.left = left 
        self.right = right 

def inorder_traversal(root):
    print ('Inorder Traversal: ')
    stack = []
    current = root 
    while stack or current: 
        if current: 
            stack += current, 
            current = current.left
        else:
            popped = stack.pop()
            print (popped.value, end='->')
            current = popped.right
    print ()

def preorder_traversal(root):
    print ('Preorder Traversal: ')
    stack = [root]
    while stack: 
        current = stack.pop()
        print (current.value, end='->')
        if current.right:
            stack += current.right, 
        if current.left:
            stack += current.left, 
    print ()
    
def postorder_traversal(root):
    print ('Postorder Traversal: ')
    stack = [root]
    stack_reversed = []
    while stack: 
        current = stack.pop()
        stack_reversed += current, 
        if current.left:
            stack += current.left, 
        if current.right: 
            stack += current.right, 
    
    while stack_reversed:
        current = stack_reversed.pop()
        print (current.value, end='->')
    print ()

def all_path_sum_recursive(node, current_sum, all_path_sum):
    if not node:
        return
    current_sum = (current_sum * 10) + node.value 
    if (not node.left) and (not node.right):
        all_path_sum[0] += current_sum
    else:
        all_path_sum_recursive(node.left, current_sum, all_path_sum)
        all_path_sum_recursive(node.right, current_sum, all_path_sum)
    return

def all_path_sum(root):
    all_path_sum = [0]
    all_path_sum_recursive(root, 0, all_path_sum)
    return all_path_sum[0]


def path_with_maximum_sum_recursive(node, current_sum, global_maximum):
    if not node:
        return 
    current_sum = (current_sum * 10) + node.value 
    if (not node.left) and (not node.right):
        global_maximum[0] = max(global_maximum[0], current_sum)
    else:
        path_with_maximum_sum_recursive(node.left, current_sum, global_maximum)
        path_with_maximum_sum_recursive(node.right, current_sum, global_maximum)
    return

def path_with_maximum_sum(root):
    global_maximum = [float('-inf')]
    path_with_maximum_sum_recursive(root, 0, global_maximum)
    return global_maximum[0]

def tree_diameter_recursive(root, max_diameter):
    if not root: 
        return 0 
    left = tree_diameter_recursive(root.left, max_diameter)
    right = tree_diameter_recursive(root.right, max_diameter)
    current_diameter = left + right 
    max_diameter[0] = max(max_diameter[0], current_diameter)
    return 1 + max(left, right)

def tree_diameter(root):
    max_diameter = [float('-inf')]
    tree_diameter_recursive(root, max_diameter)
    return max_diameter[0]


def main():
    tree = Node(4)
    tree.left = Node(7)
    tree.left.left = Node(2)
    tree.left.right = Node(1)
    tree.right = Node(6)
    tree.right.left = Node(5)
    tree.right.right = Node(3)

    # Inorder Traversal 
    inorder_traversal(tree)

    # Preorder Traversal
    preorder_traversal(tree)

    # Postorder Traversal
    postorder_traversal(tree)

    # All Path Sum
    print (f'All Path Sum: {all_path_sum(tree)}')

    # Path with maximum sum 
    print (f'Maximum Sum Path: {path_with_maximum_sum(tree)}')

    # Tree Diameter = Maximum Path between any two nodes (may not pass through root)
    print (f'Maximum Tree Diamter: {tree_diameter(tree)}')

main()