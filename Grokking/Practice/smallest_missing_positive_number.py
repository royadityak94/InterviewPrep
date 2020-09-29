# Python program to find the smallest missing positive number

def smallest_missing_no(arr):
    idx = 0
    while idx < len(arr) and idx != (arr[idx]-1):
        j = arr[idx] - 1
        if j < len(arr):
            arr[idx], arr[j] = arr[j], arr[idx]
        else:
            idx += 1
        # if idx == j:
        #     break

    # Iterating to find the smallest missing number
    for idx in range(len(arr)):
        if arr[idx] != (idx+1):
            return (idx+1)
    return len(arr)+1


def main():
    print (smallest_missing_no([3, 4, 7, 1]))
    print (smallest_missing_no([1, 2, 6, 9]))
    print (smallest_missing_no([4, 5, 10, 11]))
    print (smallest_missing_no([1, 2, 3]))
    print (smallest_missing_no([1, 2, 3, 4, 5, 6, 7, 10]))

main()
