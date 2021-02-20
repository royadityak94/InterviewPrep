'''
Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?
"2" => List containing root nodes of all structurally unique BSTs.
'''

def find_unique_trees_count(n):
    if n < 2:
        return 1

    count = 0
    for i in range(1, n+1):
        left = find_unique_trees_count(i-1)
        right = find_unique_trees_count(n-i)
        count += left*right
    return count
    
def main():
    print("Total trees: " + str(find_unique_trees_count(3)))
    print("Total trees: " + str(find_unique_trees_count(2)))

main()
