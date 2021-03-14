'''Largest Number formation
Given a list of non-negative integers arrange them such that they form the largest number:
Ex:
[3, 30, 34, 5, 9] -> 9534330

Naive Case:
    -> Try out all permutations: O(n!)
'''

def getPermutationsHelper(arr, path, visited):
    if len(path) == len(arr):
        yield int(''.join(map(str, path)))
    for ele in arr:
        if ele not in visited:
            visited.add(ele)
            yield from getPermutationsHelper(arr, path+[ele], visited)
            visited.remove(ele)


def getPermutations(arr):
    yield from getPermutationsHelper(arr, [], set())


def largest_number_naive(arr):
    largestNumberFound = float('-inf')
    permutations = getPermutations(arr)
    while True:
        try:
            largestNumberFound = max(largestNumberFound, next(permutations))
        except StopIteration:
            break
    return largestNumberFound

class Comparator(str):
    def __lt__(x, y):
        return x+y > y+x

def largest_number(arr):
    arr = sorted(map(str, arr), key=Comparator)
    #print ("Found: ", ''.join(arr))
    arr = int(''.join(arr).lstrip('0'))
    return arr

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
