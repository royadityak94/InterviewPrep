# Python program to find the triplets as close to sum as possible
# Desc: find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
import math

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')

def unique_triplet_sum_closeto_target(arr, target):
    # Time Complexity: O(NlogN + N**2), Space Complexity: O(N)
    arr.sort() #NLogN
    observed_diff = math.inf

    for idx in range(len(arr)-1):
        target_sum = target - arr[idx]
        left, right = idx+1, len(arr)-1

        while left < right:
            current_sum = arr[left] + arr[right]
            current_diff = target_sum - current_sum

            if current_diff == 0:
                return target
            if abs(current_diff) < abs(observed_diff) or \
                (abs(current_diff) == abs(observed_diff) and current_diff > observed_diff):
                observed_diff = current_diff

            if current_diff > 0:
                left += 1
            else:
                right -= 1

    return target - observed_diff

def main():
    test(1, unique_triplet_sum_closeto_target([-2, 0, 1, 2], 2), "Test-1")
    test(0, unique_triplet_sum_closeto_target([-3, -1, 1, 2], 1), "Test-2")
    test(3, unique_triplet_sum_closeto_target([1, 0, 1, 1], 100), "Test-3")

main()
