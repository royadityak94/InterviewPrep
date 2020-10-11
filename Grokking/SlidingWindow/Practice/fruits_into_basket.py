# Given an array of characters where each character represents a fruit tree,
# are given two baskets and your goal is to put maximum number of fruits in each basket.
# The only restriction is that each basket can have only one type of fruit.

# Answer : Problem is exactly similar to k distinct characters where k = 2

from collections import defaultdict

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg, expected, output)
    else:
        print ("Failed Test Case: %s" % msg, expected, output)

def maximum_fruits_in_two_baskets(arr):
    # Time Complexity: O(N+N) ~ O(N)
    # Space Complexity: O(1)
    ws_start = 0
    max_fruits = float('-inf')
    charMap = defaultdict(int)

    for ws_end in range(len(arr)):
        rightFruit = arr[ws_end]
        charMap[rightFruit] += 1

        while len(charMap) > 2:
            leftFruit = arr[ws_start]
            charMap[leftFruit] -= 1
            if not charMap[leftFruit]:
                del charMap[leftFruit]
            ws_start += 1
        max_fruits = max(max_fruits, ws_end-ws_start+1)
    return max_fruits

if __name__ == '__main__':
    test(3, maximum_fruits_in_two_baskets(['A', 'B', 'C', 'A', 'C']))
    test(5, maximum_fruits_in_two_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
