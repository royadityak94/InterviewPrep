'''
Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?
"2" => List containing root nodes of all structurally unique BSTs.
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# O(N * 2^N ~ (4^N/root(N)) time | O(N * 2^N) space 
def find_unique_trees(n):
    if n < 1:
        return []
    return find_unique_trees_rec(1, n)

def find_unique_trees_rec(start, end):
    resultant = []
    if start > end:
        resultant += None,
        return resultant
    for i in range(start, end+1):
        left = find_unique_trees_rec(start, i-1)
        right = find_unique_trees_rec(i+1, end)
        for lTree in left:
            for rTree in right:
                root = TreeNode(i)
                root.left = lTree
                root.right = rTree
                resultant += root,
    return resultant

def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))

main()
