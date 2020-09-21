# Microsoft Interview Question
# Finding all possible permutations
from copy import deepcopy
from itertools import permutations

# def return_all_permutations(arr):
#     if len(arr) < 2:
#         return []
#     elif len(arr) == 2:
#         return [arr, arr[::-1]]
#
#     all_permutations = []
#     for idx in range(len(arr)):
#         others = return_all_permutations(arr[:idx] + arr[idx+1:])
#         for permutation in others:
#             all_permutations += [arr[idx]] + permutation,
#
#     return all_permutations

def return_all_permutations(arr):
    if len(arr) < 2:
        return []
    if len(arr) == 2:
        return [arr, arr[::-1]]

    all_permutations = []
    for idx in range(len(arr)):
        other_permutations = return_all_permutations(arr[:idx]+arr[idx+1:])

        for permute in other_permutations:
            print ("Iterating with: ", permute, " ----- ", arr[idx])
            all_permutations += [arr[idx]] + permute,
    return all_permutations


def one_liner(arr):
    return list(map(list, permutations(arr)))


def main():
    arr = [1, 2, 3, 6, 7, 8, 9]
    print (return_all_permutations(arr))
    print ('--------------------')
    print (one_liner(arr))


main()
