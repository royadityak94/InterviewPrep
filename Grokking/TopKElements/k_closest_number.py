# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.
from heapq import heappush, heappop
import math
import bisect

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while high > low:
        mid = low + ((high-low)//2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1

    if low > 0:
        return low-1
    return low

def find_closest_elements(arr, K, X):
    # Time Complexity: O(LogN + KlogK), # Space Complexity: O(K)
    result = []
    closest_idx = binary_search(arr, X)
    low, high = max(0, closest_idx-K), min(len(arr)-1, closest_idx+K)

    closest_heap = []
    for idx in range(low, high+1):
        distance = abs(X - arr[idx])
        heappush(closest_heap, (distance, arr[idx]))

    for _ in range(K):
        bisect.insort(result, heappop(closest_heap)[1])

    return result

def main():
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9, 7, 2, 7], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))

main()
