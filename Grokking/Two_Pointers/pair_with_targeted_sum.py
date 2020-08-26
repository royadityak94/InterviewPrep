# Two pointers are particularly useful when we are trying to find a set of elements in input array satisfying a constraint
# Given: Sorted Array, Target Sum. Output: Any pair of elements meeting the requisite sum
def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')

def pair_with_targeted_sum(arr, sum):
    # Time Complexity: O(N), Space Complexity: O(1)
    start, end = 0, len(arr) - 1

    while start < end:
        new_sum = arr[start] + arr[end]
        if new_sum == sum:
            return [arr[start], arr[end]]
        elif new_sum < sum:
            start += 1
        else:
            end -= 1

    return -1

def pair_with_targeted_sum_using_hashtable(arr, sum):
    # Time Complexity: O(N), Space Complexity: O(N)
    hash_vals = {}

    for num in arr:
        if (sum-num) in hash_vals:
            return [sum-num, num]
        hash_vals[num] = 0

    return -1


def main():
    test([2, 4], pair_with_targeted_sum([1, 2, 3, 4, 6], 6), "Test-1")
    test([2, 9], pair_with_targeted_sum([2, 5, 9, 11], 11), "Test-2")

    # Test using Hashmpa
    test([2, 4], pair_with_targeted_sum([1, 2, 3, 4, 6], 6), "Test-1 using Hashmap")
    test([2, 9], pair_with_targeted_sum([2, 5, 9, 11], 11), "Test-2 using Hashmap")

main()
