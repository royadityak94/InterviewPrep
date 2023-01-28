"""Practice various sorting algorithms
Insertion Sort - Small/Nearly- Sorted datasets: O(NLogN) time | O(1) space [Stable] -> Binary Insertion Sort {reduces insertion space from O(N) to O(Log N)}
Merge Sort - Sorting Medium-sized datasets/Best for linked List: O(NLogN) time | O(1) space [Stable]
Quick Sort - Sorting Medium-sized datasets/Best for Array: O(NLogN - N^2) time | O(1) space [Unstable]
Heap Sort - Large Datasets: O(NLogN) time | O(1) space [Stable]
Counting Sort - Limited data cardinality: O(N) time | O(1) space [Stable] (Like, 0-9 or 0-999, etc. as array needs to be initialized of similar size)
Radix Sort - Large data cardinality : O(N) time | O(1) space {uses Counting Sort as subprocedure] [Stable]
"""
import random
from heapq import heappush, heappop
from copy import deepcopy

def test(output, expected, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)


"""Logic: Push into Heap, Extract from Heap"""
def heap_sort(input_arr):
    min_heap = []
    for ele in input_arr:
        heappush(min_heap, ele)
    idx = 0
    while min_heap:
        input_arr[idx] = heappop(min_heap)
        idx += 1
    return input_arr

"""Logic: Create subarray left, right equals based on pivot, that is recursively called on quick sort"""
def quick_sort(input_arr):
    if len(input_arr) < 2:
        return input_arr 
    pivot = random.choice(input_arr)

    left = [ele for ele in input_arr if ele < pivot]
    equals = [ele for ele in input_arr if ele == pivot]
    right = [ele for ele in input_arr if ele > pivot]

    return quick_sort(left) + equals + quick_sort(right)


def insertion_sort(input_arr):
    n = len(input_arr)
    for i in range(1, n):
        key = input_arr[i]
        j = i - 1
        while j >= 0 and key < input_arr[j]:
            input_arr[j+1] = input_arr[j]
            j -= 1
        input_arr[j+1] = key 
    return input_arr

def merge_sort(input_arr):
    if len(input_arr) < 2:
        return input_arr
    pivot = len(input_arr) // 2
    left = merge_sort(input_arr[:pivot])
    right = merge_sort(input_arr[pivot:])

    i = j = k = 0
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            input_arr[k] = left[i]
            i += 1
        else:
            input_arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        input_arr[k] = left[i]
        k, i = k+1, i+1
    
    while j < len(right):
        input_arr[k] = right[j]
        k, j = k+1, j+1
    
    return input_arr

""" Ref: https://favtutor.com/blogs/counting-sort-python
1. Find the max element
2. Create a counter from 0 to max: each index contains count of the element found 
3. Adjust the counter to be cummulative sum (curr_index val += prev index value )
4. In the output array, place the element at the index found in the counter, and decrease the counter map value by 1.
""" 
def counting_sort(input_arr):
    if len(input_arr) < 2:
        return input_arr
    # Find max element 
    _max = float('-inf')
    for ele in input_arr:
        _max = max(_max, ele)

    # Initialize counter 
    counter_map = [0] * (_max + 1)
    for ele in input_arr:
        counter_map[ele] += 1
    # Prepare cummulative sum
    for i in range(1, len(counter_map)):
        counter_map[i] += counter_map[i-1]
    
    output_arr = [None] * len(input_arr)

    for ele in input_arr:
        _index_val = counter_map[ele]
        output_arr[_index_val-1] = ele 
        counter_map[ele] -= 1
    return output_arr
        

def main():
    #input_arr = random.sample(range(5, 25), 5)
    input_arr = [8, 13, 4, 6, 1]
    expected_output = sorted(input_arr)
    
    # Heap sort 
    test(heap_sort(deepcopy(input_arr)), expected_output, "Test Case: Heap Sort algorithm")

    # # Quick Sort
    test(quick_sort(deepcopy(input_arr)), expected_output, "Test Case: Quick Sort algorithm")

    # Insertion Sort 
    test(insertion_sort(deepcopy(input_arr)), expected_output, "Test Case: Insertion Sort algorithm")

    # Merge Sort 
    test(merge_sort(deepcopy(input_arr)), expected_output, "Test Case: Merge Sort algorithm")

    # Counting Sort - Limited count of array values, i.e., 0-9 (3, 5, 1, 6, 7, 8, 3)
    input_arr = [3, 5, 1, 6, 7, 8, 3]
    expected_output = sorted(input_arr)
    test(counting_sort(deepcopy(input_arr)), expected_output, "Test Case: Counting Sort algorithm")

main()