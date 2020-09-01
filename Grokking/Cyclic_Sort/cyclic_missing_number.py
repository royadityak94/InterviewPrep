def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def find_missing_number(arr):
    # Strategy: Sort in O(N) and then search for inequality with index in another O(N)
    # Asymptotical Complexity: O(N), Space Complexity: O(1)
    i, n = 0, len(arr)
    while i < n:
        j = arr[i]
        if arr[i] < n and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    # Traversal in O(N)
    for i in range(len(arr)):
        if arr[i] != i:
            return i

    return -1

def main():
    test(2, find_missing_number([4, 0, 3, 1]), "Test - 1")
    test(7, find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]), "Test - 2")

main()
