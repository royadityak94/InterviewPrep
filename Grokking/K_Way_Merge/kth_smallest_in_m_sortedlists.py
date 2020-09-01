# Note: Programs in both merge_K_sorted_lists and this file are same -
# Demonstrates working with ListNode and simple array list
# Given M sorted arrays, finding the K'th smallest number among them
from __future__ import print_function
from heapq import heappush, heappop

# def find_Ksmallest_Msorted_lists(lists, k):
#     minHeap = []
#     count = 0
#
#     for i in range(len(lists)):
#         heappush(minHeap, (lists[i][0], count, lists[i]))
#
#     while minHeap:
#         number, i, list = heappop(minHeap)
#         count += 1
#         if count == k:
#             break
#         if len(list) > i+1:
#             heappush(minHeap, (list[i+1], i+1, list))
#
#     return number

def merge_K_sorted_lists(lists):
    # Time Complexity: O(NLogM), Space Complexity: O(M)
    minHeap  = []
    sorted_vals = []

    for i in range(len(lists)):
        heappush(minHeap, (lists[i][0], 0, lists[i]))

    while minHeap:
        number, idx, list = heappop(minHeap)
        sorted_vals.append(number)
        if idx+1 < len(list):
            heappush(minHeap, (list[idx+1], idx+1, list))

    return sorted_vals

def find_Ksmallest_Msorted_lists(lists, k):
    # Time Complexity: O(Klog M), Space Complexity: O(M)
    minHeap = []
    count = 0

    for i in range(len(lists)):
        heappush(minHeap, (lists[i][0], 0, lists[i]))

    while minHeap:
        number, idx, list = heappop(minHeap)
        count += 1
        if count == k:
            break
        if idx+1 < len(list):
            heappush(minHeap, (list[idx+1], idx+1, list))

    return number

def main():
    arr = [[12, 16, 42], [3, 26, 27], [1, 3, 41, 45]]
    print ("M sorted list is ", merge_K_sorted_lists(arr))
    print ("Kth smallest number in M sorted list is: ", find_Ksmallest_Msorted_lists(arr, 5))

main()
