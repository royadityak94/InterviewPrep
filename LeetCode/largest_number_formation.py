'''Largest Number formation
Given a list of non-negative integers arrange them such that they form the largest number:
Ex:
[3, 30, 34, 5, 9] -> 9534330

Naive Case:
    -> Try out all permutations: O(n!)
'''
import itertools
import operator

def getPermuationsHelper(arr, path, visited):
    if len(path) == len(arr):
        yield int(''.join(map(str, path)))
    for ele in arr:
        if ele not in visited:
            visited.add(ele)
            yield from getPermuationsHelper(arr, path+[ele], visited)
            visited.remove(ele)

def getPermuations(arr):
    permutations = []
    if not arr:
        return permutations
    yield from getPermuationsHelper(arr, [], set())

# O(n!) time | O(1) space
def largest_number_naive(arr):
    max_number_found = float('-inf')
    permutations = getPermuations(arr)
    # Alternate: itertools.permutations(arr)
    while True:
        try:
            max_number_found = max(max_number_found, next(permutations))
        except StopIteration:
            break
    return max_number_found

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x # equivalent of -lt (in the sense, we are puting larger number first)

# Optimized approach
def largest_number(arr):
    arr = list(map(str, arr))
    arr.sort(key=LargerNumKey)
    return int(''.join(arr))

if __name__ == '__main__':
    # Naive approach
    assert largest_number_naive([3, 30, 34, 5, 9]) == 9534330
    assert largest_number_naive([9, 80, 71, 8, 90]) == 99088071
    assert largest_number_naive([54, 546, 548, 60]) == 6054854654
    assert largest_number_naive([1, 34, 3, 98, 9, 76, 45, 4]) == 998764543431

    # Optimized approach
    assert largest_number([3, 30, 34, 5, 9]) == 9534330
    assert largest_number([9, 80, 71, 8, 90]) == 99088071
    assert largest_number([54, 546, 548, 60]) == 6054854654
    assert largest_number([1, 34, 3, 98, 9, 76, 45, 4]) == 998764543431
