from itertools import permutations

# O(N* 2^N) time | O(N * 2^N) space
def find_subsets(arr):
    subsets = [[]]

    for ele in arr:
        startIdx, endIdx = 0, len(subsets)

        for j in range(startIdx, endIdx):
            subsets += subsets[j] + [ele],
    return subsets

def main():
    print("Here is the listp of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

main()
