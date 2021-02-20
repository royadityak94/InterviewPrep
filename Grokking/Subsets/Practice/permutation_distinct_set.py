# Given a set of distinct numbers, find all of its permutations.
import sys
from collections import deque

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

# O(N * N!) time | O(N * N!) space
def find_permutations(arr):
    all_permutations = []
    find_permutations_recursive(arr, 0, all_permutations)
    return all_permutations

def find_permutations_recursive(arr, currIdx, all_permutations):
    if currIdx == len(arr):
        all_permutations += arr[:],
        return
    for j in range(currIdx, len(arr)):
        swap(currIdx, j, arr)
        find_permutations_recursive(arr, currIdx+1, all_permutations)
        swap(currIdx, j, arr)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
    print("Here are all the permutations (Educative approach): " + str(find_permutations_alt([1, 3, 5])))

main()

# [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
