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
def find_unique_trees_count(n):
    dp = {}
    return find_unique_trees_count_rec(dp, n)

def find_unique_trees_count_rec(dp, n):
    if n <= 1:
        return 1
    if n not in dp:
        count = 0
        for i in range(1, n+1):
            left = find_unique_trees_count_rec(dp, i-1)
            right = find_unique_trees_count_rec(dp, n-i)
            count += (left * right)
        dp[n] = count
    return dp[n]

def main():
    print("Total trees: " + str(find_unique_trees_count(3)))
    print("Total trees: " + str(find_unique_trees_count(2)))

main()
