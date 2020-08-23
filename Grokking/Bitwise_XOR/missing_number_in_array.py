# Python program to find the missing number in the sequence using Bitwise XOR
# Time Complexity: O(N), Space Complexity: O(1)
# Properties: 1 ^ 0 = 1, 31 ^ 0 = 31

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def missing_number_in_array(arr):
    # Time Complexity: O(N), Space Complexity: O(1)
    N = max(arr)
    if len(arr) == N:
        return -1 # No missing element
    predicted = 1
    actual = arr[0] ^ arr[1]

    for i in range(2, N-1):
        predicted ^= i
        actual ^= arr[i]

    predicted ^= (N-1 ^ N)
    return actual ^ predicted

def main():
    test(3, missing_number_in_array([1, 5, 2, 6, 4]), "Test - 1")
    test(-1, missing_number_in_array([1, 2, 3, 4, 5]), "Test - 2")

main()
