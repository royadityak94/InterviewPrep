# Python program to find the single duplicate in a fixed range of numbers: 1->n

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def finding_single_duplicate(arr):
    # Time Complexity: O(N), Space Complexity: O(1)
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] == arr[j] and i!=j:
            return arr[i]
        elif arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return -1

def main():
    test(2, finding_single_duplicate([1, 2, 2, 3, 2]), "Test - 1")
    test(4, finding_single_duplicate([1, 4, 4, 3, 2]), "Test - 2")
    test(3, finding_single_duplicate([2, 1, 3, 3, 5, 4]), "Test - 3")
    test(4, finding_single_duplicate([2, 4, 1, 4, 4]), "Test - 4")

main()
