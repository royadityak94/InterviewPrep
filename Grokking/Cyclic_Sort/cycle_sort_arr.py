def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def cyclic_sort(arr):
    # Sort in place in O(N) without using extra space, Space Complexity: O(1)
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            # Swap elements at index i, j
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr

def main():
    arr1, arr2, arr3 = [3, 1, 5, 4, 2], [2, 6, 4, 3, 1, 5], [1, 5, 6, 4, 3, 2]
    arr4 = [4, 2, 3, 1]
    test(sorted(arr1), cyclic_sort(arr1), "Test - 1")
    test(sorted(arr2), cyclic_sort(arr2), "Test - 2")
    test(sorted(arr3), cyclic_sort(arr3), "Test - 3")
    test(sorted(arr4), cyclic_sort(arr4), "Test - 4")

main()
