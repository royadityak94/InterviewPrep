# Python program to compute the size of left and right tree
from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

def insertLevelOrder(arr, root, i, n):
    if i < n:
        # if arr[i] == -1:
        #     insertLevelOrder(arr, root, i+1, n)
        temp = Node(arr[i])
        root = temp
        # insert left child
        root.left = insertLevelOrder(arr, root.left, 2*i+1, n)
        # insert right child
        root.right = insertLevelOrder(arr, root.right, 2*i+2, n)
    return root

def isLeaf(node):
    if node is not None and node.left is None and node.right is None:
        return True
    return False

# Recursive function to compute left view of the tree
def leftLeaveSum(root):
    if root is None:
        return ''
    queue = deque()
    root = root.left
    queue.append(root)
    sum = 0

    while queue:
        i = 0
        while i < len(queue):
            curr = queue.popleft()
            i = i+1
            if i==1:
                sum += curr.data
            if curr.left:
                queue.append(curr.left)

    return sum

def rightLeaveSum(root):
    if root is None:
        return 0
    sum = 0
    if root.right and not root.right.left and not root.right.right:
        sum += root.data
    sum += rightLeaveSum(root.right) + rightLeaveSum(root.left)
    return sum

def leftView(root):
    max_level = [0]
    summmed_val = leftViewUtil(root, 1, max_level, 0)
    return summmed_val

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

def size_of_sides(arr):
    root = None
    root = insertLevelOrder(arr, root, 0, len(arr))
    inOrder(root)
    left_sum = leftLeaveSum(root)
    print ("left sum : ", left_sum)



def main():
    print (size_of_sides([3, 6, 2, 9, -1, 10]))

main()
