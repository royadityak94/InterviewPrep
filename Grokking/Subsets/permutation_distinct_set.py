# Given a set of distinct numbers, find all of its permutations.
import sys
from collections import deque

def find_permutations(nums):
    # Time Complexity: O(N*N!), Space Complexity: O(N*N!)
    subsets = []
    subsets.append([])

    for idx in range(len(nums)):
        queue = deque()
        # Mark all the contenders
        for set in subsets:
            queue.append(set)
        # Iterate over the contenders
        new_set = []
        while queue:
            current_set = queue.popleft()
            for j in range(len(current_set)+1):
                temp_set = list(current_set)
                temp_set.insert(j, nums[idx])
                new_set.append(temp_set)

        subsets = new_set
    return subsets

def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))

main()
