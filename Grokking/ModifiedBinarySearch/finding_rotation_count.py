def count_rotations_alternate(arr):
    # Time Complexity: O(N), Space Complexity: O(1)
    # TODO: Write your code here
    start, end = 0, len(arr)-1

    for idx in range(1, len(arr)-1):
        if arr[idx-1] < arr[idx] > arr[idx+1]:
            return idx+1
    return 0

def count_rotations(arr):
    # Time Complexity: O(LogN), Space Complexity: O(1)
    start, end = 0, len(arr)-1
    while start < end:
        mid = start + (end-start)//2
        if arr[mid-1] > arr[mid] < arr[mid+1]:
            return mid
        elif arr[mid] < arr[mid+1]:
            start = mid+1
        else:
            end = mid - 1
    return 0

def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))

main()
