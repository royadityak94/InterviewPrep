# Given a sorted array (we don't know whether it's ascending or descending), search for a given key
# Find the order by comparing the first and last elements

def binary_search(arr, key):
    # Time Complexity: O(logN), Space Complexity: O(1)
    order = [-1, 1][arr[0] < arr[-1]]

    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return mid+1
        elif (arr[mid] - key)*order < 0:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))
    print(binary_search([10, 10, 6, 6, 6, 6, 6, 5, 5, 5, 4, 3], 4))


main()
