# Python program to implement max-heap over an array
from heapq import heappush, heappop
from functools import reduce
import operator

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def max_array_element(arr):
    maxHeap = []

    for ele in arr:
        heappush(maxHeap, -ele)

    return -heappop(maxHeap)

def test_for_kth_max(array_of_arr, k):
    final_arr = sorted(reduce(lambda x, y: x+y, array_of_arr), reverse=True)
    return final_arr[k]

def kth_max_element(array_of_arr, k):
    maxHeap = []

    itr = 0
    for arr in array_of_arr:
        heappush(maxHeap, (-arr[0], itr, arr))

    while maxHeap:
        number, idx, list = heappop(maxHeap)
        if itr == k:
            break
        if idx+1 < len(list):
            heappush(maxHeap, (-list[idx+1], idx+1, list))

        itr += 1
    return(-number)

def main():
    arr = [87, 19, 0, 55, 12, 2, 11, 9, 91]
    test (max(arr), max_array_element(arr), "Test - 1")

    arr_of_arr, k = [sorted(arr, reverse=True), [45, 24], [113, 1]], 4
    test (test_for_kth_max(arr_of_arr, k), kth_max_element(arr_of_arr, k), "Test - 2")

    # Three ways of reducing arrays of array to flattened form
    scheme1 = reduce(lambda x, y: x+y, arr_of_arr)
    scheme2 = reduce(operator.concat, arr_of_arr)

    for _ in range(len(arr_of_arr)):
        if isinstance(arr_of_arr, list):
            curr = arr_of_arr.pop(0)
            arr_of_arr.extend(curr)
        else:
            break
    print ("Is transformation successful? ", scheme1 == scheme2 == arr_of_arr)

main()
