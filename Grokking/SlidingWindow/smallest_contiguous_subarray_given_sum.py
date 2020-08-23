# Python program to find the smallest contiguous subarray for a given input sum
def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def smallest_contiguous_subarray_given_sum(arr, S):
    smallest_observed = len(arr)
    for itr in range(len(arr)):
        if arr[itr] >= S:
            return 1
        start, end = itr, itr+1
        while end < len(arr) and start < len(arr) and (end-start) > 0:
            if sum(arr[start:end]) >= S and (end - start) < smallest_observed:
                smallest_observed = end - start
                start = start + 1
            end = end + 1
    return smallest_observed

def main():
    test_cases = {'t1': ([2, 1, 5, 2, 3, 2], 7, 2), 't2': ([2, 1, 5, 2, 8], 7, 1), 't3': ([3, 4, 1, 1, 6], 8, 3)}

    for test_case in test_cases.keys():
        # if test_case != 't2':
        #     continue
        input_arr, sum_S, expected_op = test_cases.get(test_case)
        test(expected_op, smallest_contiguous_subarray_given_sum(input_arr, sum_S), test_case)

main()
