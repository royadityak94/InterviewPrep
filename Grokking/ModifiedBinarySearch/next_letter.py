
def search_next_letter(arr, key):
    # Time Complexity: O(LogN), Space Complexity: O(1)
    if key < arr[0] or key > arr[-1]:
        return arr[0]
    start, end = 0, len(arr) - 1
    found = 0
    while start <= end:
        mid = start + (end-start)//2
        if key >= arr[mid]:
            start = mid+1
        else:
            end = mid-1

    return arr[start % len(arr)]

def search_next_letter_simple(arr, key):
    # Time Complexity: O(LogN), Space Complexity: O(1)
    if key < arr[0] or key > arr[-1]:
        return arr[0]

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] <= key:
            start = mid + 1
        else:
            end = mid - 1
    return arr[start]


def main():
    print(search_next_letter_simple(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter_simple(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter_simple(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter_simple(['b', 'c', 'f', 'h'], 'a'))
    print ('---------------------------------')
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter(['b', 'c', 'f', 'h'], 'a'))

main()
