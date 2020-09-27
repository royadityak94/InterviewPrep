
def find_range(arr, key):
    # Time Complexity: O(Log N), Space Complexity: O(1)
    result = [- 1, -1]
    if key not in arr:
        return result

    start, end = arr.index(key), len(arr)-1
    result[0] = start

    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] > key:
            end = mid - 1
        else:
            start = mid+1

    result[-1] = start-1

    return result

def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))
    print(find_range([4, 1, 2, 6, 6, 6, 9, 2, 1, 1, 2], 6))

main()
