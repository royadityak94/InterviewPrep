def find_duplicates_case1(arr):
    duplicates = []
    for i in range(len(arr)):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = - arr[abs(arr[i])]
        else:
            duplicates.append(abs(arr[i]))
    return duplicates

def find_duplicates_general(arr):
    seen, duplicates = [], []
    for i in range(len(arr)):
        if arr[i] in seen:
            duplicates.append(arr[i])
        else:
            seen.append(arr[i])
    return duplicates

if __name__ == '__main__':
    arr = [1, 3, 1, 0, 1, 2, 2, 1, 2, 3, 4, 4]
    print (find_duplicates_case1(arr))

    arr2 = [1e9, 1e7, 1e9, 1e2, 1e2]
    print (find_duplicates_general(arr2))

