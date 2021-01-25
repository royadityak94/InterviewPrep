# Python program to compute the largest values in tree rows:
'''
Example:
L0: -1
L1: 5 7
L2: -1 None None 1
L3: 10 None None None None None 5 None
'''
class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def traverse_levels(t):
    queue = [t]
    largest_vals = []
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.pop(0)
            currentLevel += currentNode.value,

            if currentNode.left:
                queue += currentNode.left,
            if currentNode.right:
                queue += currentNode.right,
        print ("Found: ", currentLevel)
        largest_vals += max(currentLevel),
    return largest_vals





if __name__ == '__main__':
    root = Node(-1)
    root.left = Node(5)
    root.left.left = Node(-1)
    root.left.left.left = Node(10)

    root.right = Node(7)
    root.right.right = Node(1)
    root.right.right.left = Node(5)

    print ("Max: ", traverse_levels(root))
