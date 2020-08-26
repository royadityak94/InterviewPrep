# Removing duplicates (in-place) from an array of sorted numbers

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')


def inplace_duplicate_removal(arr):
    next_non_duplicate = next = 1

    while next < len(arr):
        if arr[next_non_duplicate-1] != arr[next]:
            arr[next_non_duplicate] = arr[next]
            next_non_duplicate += 1
        next += 1

    return next_non_duplicate

def main():
    test(4, inplace_duplicate_removal([2, 3, 3, 3, 6, 9, 9]), "Test-1")
    test(2, inplace_duplicate_removal([2, 2, 2, 11]), "Test-2")

main()
