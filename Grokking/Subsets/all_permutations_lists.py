from itertools import permutations

def find_subsets(nums):
    # Time Complexity: O(N*(2^N)), Space Complexity: O(2^N)
    subsets = []
    # TODO: Write your code here
    subsets.append([])
    for ele in nums:
        for i in range(len(subsets)):
            set = subsets[i] + [ele]
            subsets.append(set)
    return subsets

def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

main()
