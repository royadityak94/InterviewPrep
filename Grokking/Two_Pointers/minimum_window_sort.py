# Finding a minimum window which when sorted will sort the whole array

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def minimum_window_sort(arr):
    # Finding first deviation on either sides: low, high
    low, high = 0, len(arr) - 1

    while low < high and arr[low] <= arr[low+1]:
        low += 1
    while low < high and arr[high] >= arr[high-1]:
        high -= 1

    if low == high:
        return 0

    # Finding the extremes of the dataset
    min, max = arr[low], arr[high]
    for idx in range(len(arr)):
        if arr[idx] < min:
            min = arr[idx]
        elif arr[idx] > max:
            max = arr[idx]

    # Expanding the window of sort (if the need be)
    for idx in range(0, low):
        if arr[idx] > min and idx < low:
            low = idx
    for idx in range(high, len(arr)-1):
        if arr[idx] <  max and high < idx:
            high = idx

    return len(arr[low:high+1])


def main():
    test(6, minimum_window_sort([1, 2, 5, 3, 7, 10, 9, 12]), "Test - 1")
    test(9, minimum_window_sort([1, 1.5, 1.8, 3, 2, 0, -1, 12, 10]), "Test - 2")
    test(0, minimum_window_sort([1, 2, 3]), "Test - 3")
    test(3, minimum_window_sort([3, 2, 1]), "Test - 4")
    test(0, minimum_window_sort([11, 12, 13, 15, 26, 28]), "Test - 5")
    test(6, minimum_window_sort([0, 0, 1, 2, 0, 3, 21, 12, 25]), "Test - 6")


main()
