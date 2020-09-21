# Finding a missing number in an array of 'N' supposedly containing (N+1) contiguous numbers

def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        j = arr[i]
        if arr[j] != arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    return arr

def find_single_missing_number(arr):
    # Time Complexity: O(N) + O(N-1) ~ O(N)
    i = 0
    while i < len(arr):
        j = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    # Finding the single missing number
    for i in range(len(arr)):
        if arr[i] != i:
            return i

    return len(arr)

def find_all_missing_numbers(arr):
    i, n = 0, len(arr)

    while i < n:
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    all_duplicates = []
    for idx in range(len(arr)):
        if arr[idx] != (idx+1):
            all_duplicates += (idx+1),

    return all_duplicates

def finding_single_duplicate(arr):
    i, n = 0, len(arr)
    while i < n:
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    for i in range(n):
        if arr[i] != (i+1):
            return arr[i]

    return -1

def finding_all_duplicate(arr):
    i, n = 0, len(arr)
    while i < n:
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    all_duplicates = []
    for i in range(n):
        if arr[i] != (i+1):
            all_duplicates += arr[i],

    return all_duplicates

def main():
    print ("Is implementation correct: ", (cyclic_sort([4, 1, 2, 0, 3]) == sorted([4, 1, 2, 0, 3])))
    print (find_single_missing_number([4, 0, 3, 1]))
    print (find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print (find_all_missing_numbers([2, 4, 1, 2]))
    print ('-----')
    print (finding_single_duplicate([2, 1, 3, 3, 5, 4]))
    print (finding_all_duplicate([2, 1, 3, 1, 4, 1, 5, 4, 3, 3, 3,]))
    #print (find_single_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
