
def find_max_in_bitonic_array(arr):
    # Time Complexity: O(LogN), Space Complexity:O(1)
    start, end = 0, len(arr)-1

    while start != end:
        mid = start + (end-start)//2
        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid] < arr[mid+1]:
            start = mid + 1
        else:
            end = mid - 1
    return arr[start]

def main():
    print (find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print (find_max_in_bitonic_array([3, 8, 3, 1, 0, -1, -2]))
    print (find_max_in_bitonic_array([1, 3, 8, 12]))
    print (find_max_in_bitonic_array([10, 9, 8, 6, 5, 4, 3, 2, 1 ]))

main()
