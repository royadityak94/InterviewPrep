from itertools import permutations

# O(N * 2^N) time | O(N * 2^N) space
def find_subsets(nums):
    all_subsets = [[]]
    for ele in nums:
        startIdx = 0
        endIdx = len(all_subsets)
        for j in range(startIdx, endIdx):
            current_list = all_subsets[j] + [ele]
            all_subsets += current_list,
    return all_subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

main()
