# Program to compute the max sum subarray of size K.
"""
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""
def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Failed Test Case: %s" % msg)

def max_sum_subarray_size_K_Naive(input_arr, size_K):
    # Time Complexity: O(N*K)
    output_arr = []
    for itr in range(len(input_arr)-size_K+1):
        slice = input_arr[itr:itr+size_K]
        output_arr.append(sum(slice)/float(size_K))

    return output_arr

def max_sum_subarray_size_K_Optimized(input_arr, size_K):
    # Time Complexity: O(N)
    running_sum = input_arr[0:size_K]
    output_arr = []
    output_arr.append(sum(running_sum)/float(size_K))
    for itr in range(1, len(input_arr)-size_K+1):
        running_sum.pop(0)
        running_sum.append(input_arr[itr+size_K-1])
        output_arr.append(sum(running_sum)/float(size_K))

    return output_arr

def max_sum_subarray_size_K_Space_Optimized(input_arr, size_K):
    # Time Complexity: O(N)
    running_sum = sum(input_arr[0:size_K])
    output_arr = [running_sum/float(size_K)]
    for itr in range(1, len(input_arr)-size_K+1):
        running_sum = running_sum - input_arr[itr-1] + input_arr[itr+size_K-1]
        output_arr.append(running_sum/float(size_K))

    return output_arr

def main():
    input_arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    K = 5
    expected_op = [2.2, 2.8, 2.4, 3.6, 2.8]
    test(expected_op, max_sum_subarray_size_K_Naive(input_arr, K), "Naive Case")
    test(expected_op, max_sum_subarray_size_K_Optimized(input_arr, K), "Optimized Case")
    test(expected_op, max_sum_subarray_size_K_Space_Optimized(input_arr, K), "Space Optimized Case")

main()
