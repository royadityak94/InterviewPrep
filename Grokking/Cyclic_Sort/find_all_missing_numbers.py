# Python program to find all missing numbers using cyclic sort pattern

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def find_all_missing_number(arr):
    # Time Complexity: O(N), Space Complexity: O(1)
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    # Finding all the missing numbers
    missing_numbers = []
    for i in range(len(arr)):
        if arr[i] != (i+1):
            missing_numbers.append(i+1)

    return missing_numbers

def main():
    test([4, 6, 7], find_all_missing_number([2, 3, 1, 8, 2, 3, 5, 1]), "Test - 1")
    test([3], find_all_missing_number([2, 4, 1, 2]), "Test - 2")
    test([4], find_all_missing_number([2, 3, 2, 1]), "Test - 3")
    pass

main()
