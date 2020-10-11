# Program to compute the max sum subarray of size K.
def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg, expected, output)
    else:
        print ("Failed Test Case: %s" % msg, expected, output)

def max_sum_subarray_size_K_Naive(input_arr, size_K):
    # Time Complexity: O(N*K)
    max_output = float('-inf')
    for itr in range(len(input_arr)-size_K+1):
        slice = input_arr[itr:itr+size_K]
        max_output = max(max_output, sum(slice))

    return max_output

def max_sum_subarray_size_K_Optimized(input_arr, size_K):
    # Time Complexity: O(N), Space Complexity: O(1)
    if len(input_arr) < size_K:
        return sum(input_arr)

    left = 0
    ws_sum = sum(input_arr[:size_K])
    max_sum = ws_sum

    for right in range(size_K, len(input_arr)):
        ele_right = input_arr[right]
        ele_left = input_arr[right-size_K]
        ws_sum +=  -input_arr[right-size_K] + input_arr[right]
        max_sum = max(max_sum, ws_sum)
    return max_sum


def main():
    input_arr = [2, 1, 5, 1, 3, 2]
    K = 3
    expected_op = 9
    test(expected_op, max_sum_subarray_size_K_Naive(input_arr, K), "Naive Case")
    test(expected_op, max_sum_subarray_size_K_Optimized(input_arr, K), "Optimized Case")

main()
