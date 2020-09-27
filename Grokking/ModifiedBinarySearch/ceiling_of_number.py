
def search_ceiling_of_a_number(arr, key):
    # Time Complexity: O(logN), Space Complexity: O(1)
    # TODO: Write your code here
    if key > arr[-1]:
        return -1
    elif key < arr[0]:
        return 1

    start, end = 0, len(arr)-1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid+1
        elif arr[mid] < key:
            start = mid + 1
        else:
            return mid+1

    return start


def main():
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15, 18, 21], 9))
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))

main()
