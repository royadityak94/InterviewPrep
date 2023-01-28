"""Practice Heaps"""
from typing import List
from collections import Counter 
from heapq import heappush, heappop
import random

def test(output, expected, msg=''):
    if isinstance(expected, str):
        expected = [expected]
    if output in expected:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

"""Reorganize input string such that, no two characters are adjacent to each other. Return '' (empty string), if not possible
EO: (('aab' -> 'aba'), ('aaab' -> ''), ('aabc'-> 'abac'))
Logic: Build a frequency counter that is put into max heap, pop 2 at a time (to avoid same char coming out twice - in case they have a high value), form the resultant 
    string, until one item in heap is left -> if that item has frequency higher than one, than the string can't be formed 
"""
def reorganize_string(input):
    # Build a frequency counter 
    input_frequency = Counter(input)

    # Put into heap 
    input_freq_heap = []
    for k in input_frequency:
        heappush(input_freq_heap, (-input_frequency[k], k))

    # Form the resultant string 
    resultant_string = ''
    while len(input_freq_heap) > 1:
        value_c1, key_c1 = heappop(input_freq_heap)
        value_c2, key_c2 = heappop(input_freq_heap)

        resultant_string += (key_c1 + key_c2)

        if value_c1 < -1:
            heappush(input_freq_heap, (value_c1+1, key_c1))
        if value_c2 < -1:
            heappush(input_freq_heap, (value_c2+1, key_c2))

    if input_freq_heap:
        value, key = heappop(input_freq_heap)
        if value < -1:
            return ''
        resultant_string += key 
    
    if len(resultant_string) == len(input):
        return resultant_string
    return ''
"""
Keep adding to the heap using heappush, extract using heappop
"""
def heap_sort(input_arr: List[int]) -> List[int]:
    heap_values =  []
    for input in input_arr:
        heappush(heap_values, input)

    resultant_set = []
    while heap_values:
        resultant_set += heappop(heap_values),
    return resultant_set

def median_of_sliding_window(input_arr: List[int], window_k: int) -> List[float]:
    # Initializations 
    input_arr_len = len(input_arr)
    # Construct the heap 
    min_heap = []
    max_heap = []

    for ele in input_arr: 
        if (not max_heap) or (-max_heap[0] >= ele):
            heappush(max_heap, -ele)
        else:
            heappush(min_heap, ele)

        if (len(max_heap) - len(min_heap)) > 1:
            heappush(min_heap, -heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))

    
    resultant_medians: List[float] = []

    for i in range(input_arr_len-window_k+1):
        if len(min_heap) == len(max_heap):
            resultant_medians += (-heappop(max_heap) + heappop(min_heap))/2.0,
        else:
            resultant_medians += -heappop(max_heap)/1.0, 
            heappush(max_heap, heappop(min_heap))
        print ("Median now: ", resultant_medians)

    print (f'Output = {resultant_medians}')
    return resultant_medians

def main():
    test(reorganize_string('aab'), 'aba', 'reorganize_string: Test-1')
    test(reorganize_string('aaab'), '', 'reorganize_string: Test-2')
    test(reorganize_string('aabc'), ['abac', 'abca'], 'reorganize_string: Test-3')

    # Heap Sort algorithm
    input_arr =  random.sample(range(5, 75), 20)
    test(','.join(map(str, heap_sort(input_arr))), ','.join(map(str, sorted(input_arr))), "heap_sort: Test Case - 1")

    # Two Heap Problem Practice 
    # Median of sliding window 
    median_of_sliding_window([1, 2, -1, 3, 5], 2)


main()