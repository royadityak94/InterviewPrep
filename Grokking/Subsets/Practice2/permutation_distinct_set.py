# Given a set of distinct numbers, find all of its permutations.
import sys
from collections import deque

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def find_permutations(arr):
    permutations = []
    find_permutations_rec(arr, 0, permutations)
    return permutations

def find_permutations_rec(arr, currIdx, permutations):
    if currIdx == len(arr):
        permutations += arr[:],
        return
    for j in range(currIdx, len(arr)):
        swap(j, currIdx, arr)
        find_permutations_rec(arr, currIdx+1, permutations)
        swap(j, currIdx, arr)

def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))

main()
