

def compute_merged(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)
    i, j, k = 0, 0, 0
    merged = [None] * (l1 + l2)
    while i < l1 and j < l2:
        if arr1[i] <= arr2[j]:
            merged[k], i, k = arr1[i], i+1, k+1
        else:
            merged[k], j, k = arr2[j], j+1, k+1
    # Completing merging of the uncompleted list
    while i < l1:
        merged[k], i, k = arr1[i], i+1, k+1
    while j < l2:
        merged[k], j, k = arr2[j], j+1, k+1
    return merged

def median(arr1, arr2):
    merged = compute_merged(arr1, arr2)
    print (merged)
    len_merged = len(merged)
    if len_merged % 2 != 0:
        return merged[int(len_merged/2)]
    else:
        return 0.5 * (merged[int(len_merged/2)-1] + merged[int(len_merged/2)])

if __name__ == '__main__':
    arr1 = [1, 3, 5]
    arr2 =  [2, 4, 6]

    print (median(arr1, arr2))