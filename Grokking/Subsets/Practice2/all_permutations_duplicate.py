# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

# O(n * 2^n) time | O(n * 2^n) space
def find_subsets(arr):
    arr.sort()
    subsets = [[]]

    for idx in range(len(arr)):
        startIdx, endIdx = 0, len(subsets)
        if idx > 0 and arr[idx] == arr[idx-1]:
            startIdx = endIdx - 1

        for j in range(startIdx, endIdx):
            subsets += subsets[j] + [arr[idx]],
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))

main()
