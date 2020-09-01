# Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists (all input lists)
# Strategy similar to Merge K sorted lists - keep currentMaxNumber registered to update range
from heapq import heappush, heappop
import math

def find_smallest_range(lists):
    # Time Complexity: O(NlogM), Space Complexity: O(M)
    minHeap = []
    observedMax = -math.inf

    for list in lists:
        heappush(minHeap, (list[0], 0, list))
        observedMax = max(observedMax, list[0])

    range_start, range_end = 0, math.inf
    while len(minHeap) == len(lists):
        number, i, list = heappop(minHeap)

        if range_end - range_start > observedMax - number:
            range_start, range_end = number, observedMax

        if i+1 < len(lists):
            heappush(minHeap, (list[i+1], i+1, list))
            observedMax = max(observedMax, list[i+1])

    return [range_start, range_end]


def main():
    print (find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]]))

main()
