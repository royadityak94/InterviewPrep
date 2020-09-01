# Python program to find the first-k missing numbers

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def find_first_k_missing_positive(arr, k=1):
    # Time Complexity: O(N+k) ~ O(N), Space Complexity: O(k)
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if j < len(arr) and arr[i] > 0 and i!=j and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    # Iterating over the sorted array to find all the missing numbers
    missing_numbers, ignored_numbers = [], []

    for i in range(len(arr)):
        if arr[i] != (i+1):
            missing_numbers.append((i+1))
        if arr[i] > len(arr):
            ignored_numbers.append(arr[i])

    i = len(arr) + 1
    while len(missing_numbers) < k:
        if i not in ignored_numbers:
            missing_numbers.append(i)
        i += 1

    return missing_numbers[:k]


def main():
    test([1, 2, 6], find_first_k_missing_positive([3, -1, 4, 5, 5], 3), "Test - 1")
    test([1, 5, 6], find_first_k_missing_positive([2, 3, 4], 3), "Test - 2")
    test([1, 2], find_first_k_missing_positive([-2, -3, 4], 2), "Test - 3")

main()
