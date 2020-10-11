# Creating a balanced bst using unsorted array and then support streaming insert into a balanced bst

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def merge_sort(arr):
    if len(arr) == 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


def sorted_arr_to_bst(arr):
    if not arr:
        return

    mid = len(arr)//2
    if len(arr)%2 == 0:
        mid = mid - 1
    root = Node(arr[mid])
    root.left = sorted_arr_to_bst(arr[:mid])
    root.right = sorted_arr_to_bst(arr[mid+1:])
    return root

def preOrderTraversal(root):
    if not root:
        return
    stack = [root]
    while stack:
        popped = stack.pop()
        print (popped.val, end=' -> ')
        if popped.right:
            stack += popped.right,
        if popped.left:
            stack += popped.left,
    print()
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
            print (popped.val, end=' -> ')
            current = popped.right
    print()
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
        print (stack_reverse.pop().val, end=' -> ')
    print()
    return

# Insertion into BST
def insert(root, key):
    if not root:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

if __name__ == '__main__':
    arr = [21, 10, 5, 8, 11, 14, 12, 3, 1, 22]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
    root = sorted_arr_to_bst(sorted_arr)
    print ("PreOrder Traversal")
    preOrderTraversal(root)
    # print ("InOrder Traversal")
    # inOrderTraversal(root)
    # print ("PostOrder Traversal")
    # postOrderTraversal(root)

    new_stream = [6, 26, 19, 17, 2]
    for ele in new_stream:
        root = insert(root, ele)

    print ('-------------------------')
    print ("PreOrder Traversal")
    preOrderTraversal(root)
    print ("InOrder Traversal")
    inOrderTraversal(root)
    print ("PostOrder Traversal")
    postOrderTraversal(root)
