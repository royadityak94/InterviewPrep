# Replace 0 with 1s to create a contiguous subarray of all 1 in the given subarray
# Input: [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2, Output: 6 (Replace index(s): 5, 8)
# Input: [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3 Output: 9 (Replace index(s): 6, 9, 10)

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def longest_subarray_with_ones_after_replacement(input_arr, k):
    # Runtime Complexity : O(N), Space Complexity: O(1)
    max_length = 0
    window_start = 0
    maxOnesCount = 0

    for window_end in range(len(input_arr)):
        maxOnesCount = max(maxOnesCount, input_arr[window_start:window_end+1].count(1))

        if (window_end-window_start+1-maxOnesCount) > k:
            window_start += 1

        max_length = max(max_length, window_end-window_start+1)
    return max_length

def main():
    test(6, longest_subarray_with_ones_after_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2), "Test 1")
    test(9, longest_subarray_with_ones_after_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3), "Test 2")

main()
