# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

def search_min_diff_element(arr, key):
    # Time Complexity: O(LogN), Space Complexity: O(1)
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            return key
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    if start < len(arr) and (arr[start] - key) < (key - arr[end]):
        return arr[start]
    else:
        return arr[end]

def main():
    print (search_min_diff_element([4, 6, 10], 7))
    print (search_min_diff_element([4, 6, 10], 4))
    print (search_min_diff_element([1, 3, 8, 10, 15], 12))
    print (search_min_diff_element([4, 6, 10, 12], 17))

main()
