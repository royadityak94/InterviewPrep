# Prob Nicknamed: Dutch National Flag Prob
# Given input with only three numbers (0, 1, 2) [Dutch flag has three colors, RWB], sort them in place
# You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# Important Information:
# With in-place sorting algorithm like Heapsort, our complexity is O(NLogN), however we can do it in O(N) for this problem using the propery that:
# Maintain two pointers: left and right, bring all 0s before low and all 1s after high in single pass

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def dutch_national_flag_problem(arr):
    # Time Complexity: O(N), Space Complexity: O(1)
    low, high = 0, len(arr)-1
    idx = 0
    while idx <= high:
        if arr[idx] == 0:
            arr[low], arr[idx] = arr[idx], arr[low]
            low += 1
            idx += 1
        elif arr[idx] == 2:
            while arr[high] == 2:
                high -= 1
            arr[high], arr[idx] = arr[idx], arr[high]
            high -= 1
        else:
            idx += 1
    return arr

def main():
    test([0, 0, 1, 1, 2], dutch_national_flag_problem([1, 0, 2, 1, 0]), "Test - 1")
    test([0, 0, 1, 2, 2, 2], dutch_national_flag_problem([2, 2, 0, 1, 2, 0]), "Test - 2")

main()
