'''Sorting algorithms (quick revision)
Insertion Sort (ideal for almost sorted list) -> O(n) avg time, O(n^2) worst
Merge Sort (ideal for large lists) -> O(nlogn) time
Quick Sort (ideal for small lists) -> O(nlogn) time
'''
from copy import deepcopy
import random

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i-1  # Most important part
        key = arr[i]  # Most important part
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]  # Most important part
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]  # Most important part
    right = arr[mid:]  # Most important part
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr

def random_pivot_selection(arr):
    n = len(arr)
    random_idx = random.randint(1, len(arr))
    return random_idx

def partition(arr, low, high):
    j = low - 1
    # random pivot selection, instead of, key=arr[high]
    random_id = random.randint(low, high) # two extra lines for random pivot
    swap(high, random_id, arr) # two extra lines for random pivot
    key = arr[high]
    for i in range(low, high):
        if key > arr[i]: # Most important part
            j += 1
            swap(i, j, arr)
    swap(high, j+1, arr)  # Most important part
    return j+1

def quick_sort(arr):
    return quick_sort_recursive(arr, 0, len(arr)-1)

def quick_sort_recursive(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_recursive(arr, low, pi-1)
        quick_sort_recursive(arr, pi+1, high)
    return arr

def quickSelect(arr, requiredIdx):
    return quickSelect_recursive(arr, 0, len(arr)-1, requiredIdx)

def quickSelect_recursive(arr, low, high, position):
    if low < high:
        pi = partition(arr, low, high)
        if pi == position - 1:
            return arr[pi]
        elif pi >= position:
            return quickSelect_recursive(arr, low, pi, position)
        else:
            return quickSelect_recursive(arr, pi, high, position)
    return -1

if __name__ == '__main__':
    arr = [3, 11, 8, 2, 6, 5, 9, 4, 1, 10]
    print (insertion_sort(deepcopy(arr)))
    print (merge_sort(deepcopy(arr)))
    print (quick_sort(deepcopy(arr)))

    # Quick select element - fourth smallest element
    for i in range(len(arr)+4):
        print(i+1, quickSelect(deepcopy(arr), i+1))
