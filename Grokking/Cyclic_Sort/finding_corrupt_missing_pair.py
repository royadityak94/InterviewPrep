# Python program to find the corrupt pairs in O(N) time and O(1) space
def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def finding_corrupt_missing_pair(arr):
    # Time Complexity: O(N), Space Complexity: O(1)
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[j] != arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    # Finding the corrupt pairs
    for i in range(len(arr)):
        if arr[i] != (i+1):
            return [arr[i], (i+1)]
    return [-1, -1]

def main():
    test([2, 4], finding_corrupt_missing_pair([3, 1, 2, 5, 2]), "Test - 1")
    test([3, 5], finding_corrupt_missing_pair([3, 1, 2, 3, 6, 4]), "Test - 2")

main()
