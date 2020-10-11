# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg, expected, output)
    else:
        print ("Failed Test Case: %s" % msg, expected, output)

def smallest_subarray_sum(input_arr, desired_sum):
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    ws_start = 0
    min_length = float('inf')
    ws_sum = 0

    for ws_end in range(len(input_arr)):
        ws_sum += input_arr[ws_end]

        while ws_sum >= desired_sum:
            min_length = min(min_length, (ws_end-ws_start+1))
            ws_sum -= input_arr[ws_start]
            ws_start += 1

    if min_length == float('inf'):
        return 0
    return min_length


if __name__ == '__main__':
    test(2, smallest_subarray_sum([2, 1, 5, 2, 3, 2], 7))
    test(1, smallest_subarray_sum([2, 1, 5, 2, 8], 7))
    test(3, smallest_subarray_sum([3, 4, 1, 1, 6], 8))
