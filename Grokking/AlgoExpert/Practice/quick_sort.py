'''Trying out quick sort using quick Select
'''
import random

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    # Randomized partition
    pivotIdx = random.randint(low, high)
    swap(pivotIdx, high, arr)

    pivot = arr[high]
    for i in range(low, high):
        if arr[i] < pivot:
            swap(low, i, arr)
            low += 1
    swap(low, high, arr)
    return low

def quick_sort(arr):
    return quick_sort_recursive(arr, 0, len(arr)-1)

def quick_sort_recursive(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_recursive(arr, low, pi-1)
        quick_sort_recursive(arr, pi+1, high)
    return arr



if __name__ == '__main__':
    #arr = [1, 5, 12, 2, 11, 5]
    arr = [random.randint(1, 20) for _ in range(20)]
    print ("Input: ", arr)
    assert quick_sort(arr) == sorted(arr), "Match Failed"
