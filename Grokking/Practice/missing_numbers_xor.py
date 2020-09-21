# In a non-empty array of integers, every number appears twice except for one, find that single number
# xor(a, a) = 0; xor(a, b) = 1
# Hashmap soln : (increment when not in map, decrement when in map) -> O(N) time, O(N) space
# XOR soln: xor the entire array, all except one will cancel out -> O(N) time, O(1) space

def finding_single_missing_number(arr):
    result = arr[0]
    for ele in arr[1:]:
        result ^= ele
    return (result)

def finding_two_missing_numbers(arr):
    n1xn2 = 0
    for ele in arr:
        n1xn2 ^= ele

    # Currently, n1xn2 = a^b, wherein (a,b) are the two missing numbers
    # Step 1: Finding the rightmost set bit
    rightmostSetBit = 1
    while (rightmostSetBit & n1xn2) == 0:
        rightmostSetBit = rightmostSetBit << 1

    a = b = 0
    for ele in arr:
        if (ele & rightmostSetBit) == 0:
            a ^= ele
        else:
            b ^= ele
    return [a, b]

def base_10_complement(num):
    bit_count, n = 0, num
    while n > 0:
        n = n >> 1
        bit_count += 1
    all_bits_set = (2 ** bit_count) - 1

    return num ^ all_bits_set



def main():
    arr = [1, 4, 2, 1, 4, 2, 3]
    print (finding_single_missing_number(arr))
    print (finding_two_missing_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
    num = 8
    print ("Complement of %d is " % num, base_10_complement(num))

main()
