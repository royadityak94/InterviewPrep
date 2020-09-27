
def binary_search(arr, key):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid+1
        else:
            end = mid-1
    return -1

def search_rotated_array(arr, key):
    # Time Complexity: O(LogN), Space Complexity: O(1)
    # Finding index of bitonic
    start, end = 0, len(arr)-1
    flag_bitonic = False
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        elif arr[mid-1] <= arr[mid] > arr[mid+1]:
            flag_bitonic = True
            break
        elif arr[mid-1] <= arr[mid] and key > arr[mid]:
            start = mid+1
        else:
            end = mid-1

    # Found bitonic
    if flag_bitonic:
        right_search = binary_search(arr[mid+1:], key)
        if right_search != -1:
            return mid + right_search
        return binary_search(arr[:mid], key)
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
    print (search_rotated_array([3, 7, 3, 3, 3], 7))


main()
