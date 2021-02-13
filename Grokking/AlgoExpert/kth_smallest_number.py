'''
Find the kth smallest number in an unsorted matrix:
Ex:
    1. I/p -> [1, 5, 12, 2, 11, 5], 3 => 5
    2. I/p -> [1, 5, 12, 2, 11, 5], 5 => 11
    3. I/p -> [5, 12, 11, -1, 2], 3 => 11

Variants:
    1. kth-largest number
    2. Median of the array
'''
from heapq import heappush, heappop

# O(nlogn) time | O(1) space
def kth_smallest_naive(arr, k):
    arr.sort()
    print ("Sorted = ", arr)
    return (arr[k-1])

# O(nlogK) time | O(K) space
def kth_smallest_optimized1(arr, k):
    maxHeap = []
    for i in range(k):
        heappush(maxHeap, -arr[i])

    for i in range(k, len(arr)):
        if -arr[i] < -maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -arr[i])
    return -heappop(maxHeap)

# O(n+ klogN) time | O(n) space
def kth_smallest_optimized2(arr, k):
    n = len(arr)
    minHeap = []
    for i in range(n):
        heappush(minHeap, arr[i])

    for i in range(k-1):
        heappop(minHeap)
    return heappop(minHeap)


def partition(arr, low, high):
    def swap(i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

    pivot = arr[high]
    for i in range(low, high):
        if arr[i] < pivot:
            swap(low, i, arr)
            low += 1
    swap(low, high, arr)
    return low

# O(N) time | O(N) space
def kth_smallest_quickSelect(arr, k):
    return kth_smallest_quickSelect_recursive(arr, k, 0, len(arr)-1)

def kth_smallest_quickSelect_recursive(arr, k, low, high):
    pi = partition(arr, low, high)
    if pi == (k-1):
        return arr[k-1]
    elif pi > (k-1):
        return kth_smallest_quickSelect_recursive(arr, k, low, pi-1)
    else:
        return kth_smallest_quickSelect_recursive(arr, k, pi+1, high)

if __name__ == '__main__':
    # Naive solution - using simple sort: O(NLogN), O(N) space
    assert kth_smallest_naive([1, 5, 12, 2, 11, 5], 3) == 5
    assert kth_smallest_naive([1, 5, 12, 2, 11, 5], 5) == 11
    assert kth_smallest_naive([5, 12, 11, -1, 2], 4) == 11

    # Optimized Max Heap solution - using maxHeap: O(NLogK), O(K) space
    assert kth_smallest_optimized1([1, 5, 12, 2, 11, 5], 5) == 11
    assert kth_smallest_optimized1([1, 5, 12, 2, 11, 5], 5) == 11
    assert kth_smallest_optimized1([5, 12, 11, -1, 2], 4) == 11

    # Optimized Max Heap solution - using minHeap: O(N + KLogN), O(N) space
    assert kth_smallest_optimized2([1, 5, 12, 2, 11, 5], 3) == 5
    assert kth_smallest_optimized2([1, 5, 12, 2, 11, 5], 5) == 11
    assert kth_smallest_optimized2([5, 12, 11, -1, 2], 4) == 11

    # Optimized Quick Select Algorithm: [{Avg: O(n) time | O(n) space}. {O(n^2) time | O(n) space}
    assert kth_smallest_quickSelect([1, 5, 12, 2, 11, 5], 3) == 5
