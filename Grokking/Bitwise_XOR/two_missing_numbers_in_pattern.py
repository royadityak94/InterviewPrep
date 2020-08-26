# Python program to compute the two missing numbers in a given pattern
def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def two_missing_numbers_in_pattern(arr):
    # Runtime : O(N), Space Complexity: O(1)
    num1_xor_num2 = 0
    for num in arr:
        num1_xor_num2 ^= num
    # Finding the rightmost set bit
    rightmost_set_bit = 1
    while (rightmost_set_bit & num1_xor_num2) == 0:
        print ("Righmost val = ", rightmost_set_bit)
        rightmost_set_bit = rightmost_set_bit << 1

    # Finding the two numbers: num1, num2
    num1 = num2 = 0

    for num in arr:
        if rightmost_set_bit & num != 0:
            num1 ^= num
        else:
            num2 ^= num

    return_val = [num1, num2]
    return_val.sort()
    return return_val

def main():
    test([4, 7], two_missing_numbers_in_pattern([1, 4, 2, 1, 3, 5, 7, 2, 3, 5]), "Test - 1")
    test([1, 3], two_missing_numbers_in_pattern([2, 1, 3, 2]), "Test - 2")

main()
