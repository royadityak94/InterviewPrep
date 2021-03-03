'''
Based on the classical two missing numbers in array: We use left-shift or right-shift to find the two numbers
'''

# O(n + n ~ n) time | O(1) space
def two_missing_numbers_in_pattern(arr):
    num1_xor_num2 = 0
    for ele in arr:
        num1_xor_num2 ^= ele
    rightmost_set_bit = 1
    while not num1_xor_num2 & rightmost_set_bit:
        rightmost_set_bit <<= 1

    num1 = num2 = 0
    for ele in arr:
        if rightmost_set_bit & ele:
            num1 ^= ele
        else:
            num2 ^= ele
    return sorted([num1, num2])

if __name__ == '__main__':
    assert two_missing_numbers_in_pattern([1, 9, 2, 1, 3, 5, 7, 2, 3, 5]) == [7, 9]
    assert two_missing_numbers_in_pattern([2, 1, 3, 2]) == [1, 3]
