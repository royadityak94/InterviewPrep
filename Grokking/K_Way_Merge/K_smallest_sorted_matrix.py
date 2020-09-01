# Given a N*N sorted matrix (across rows and columns), find Kth smallest element in a matrix
# Ans: Similar pattern to Kth smallest number in M sorted list - sorted list can be either row/column wise
from heapq import heappush, heappop

def find_Kth_smallest(matrix, k):
    # Time Complexity : O(min(K, N)), Space Complexity: O(K)
    minHeap = []
    for arr in matrix:
        heappush(minHeap, (arr[0], 0, arr))

    count = 0
    while minHeap:
        number, idx, list = heappop(minHeap)
        count += 1
        if count == k:
            break

        if idx + 1 < len(list):
            heappush(minHeap, (list[idx+1], idx+1, list))

    return number

def main():
    print (find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5))

main()
