# Python program to compute the smallest known missing number
def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def smallest_missing_positive_number(arr):
    # Time Complexity: O(N), Space Complexity: O(1)
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if 0 <= arr[i] < len(arr) and i!=j and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    # Iterating through the array to find the missing number
    for i in range(len(arr)):
        if arr[i] != (i+1):
            return (i+1)
    return -1

def main():
    test(3, smallest_missing_positive_number([-3, 1, 5, 4, 2]), "Test - 1")
    test(4, smallest_missing_positive_number([3, -2, 0, 1, 2, 5]), "Test - 2")
    test(4, smallest_missing_positive_number([3, 2, 5, 1]), "Test - 3")
    test(5, smallest_missing_positive_number([3, 2, 4, 1, -2]), "Test - 4")

main()
