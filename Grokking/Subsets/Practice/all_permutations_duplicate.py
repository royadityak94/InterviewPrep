# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

# O(N * 2^N) time | O(N * 2^N) space
def find_subsets(arr):
    arr.sort()
    subsets = [[]]
    for idx, ele in enumerate(arr):
        endIdx = len(subsets)
        startIdx = 0
        if idx > 0 and arr[idx] == arr[idx-1]:
            startIdx = endIdx - 1

        for j in range(startIdx, endIdx):
            subsets += subsets[j] + [ele],
    return subsets

def find_subsets_alternate(arr):
    subsets = [[]]
    for ele in arr:
        startIdx, endIdx = 0, len(subsets)
        for j in range(startIdx, endIdx):
            pair = subsets[j] + [ele]
            if pair not in subsets:
                subsets += pair,
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3, 5])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets_alternate([1, 5, 3, 3])))

main()
