'''
Bitwise Left Shift (<<):
 - Applies to both arithmetic (signed) and logical (unsigned) operations
 - a << b = a*(2^b)
'''
# O(1) time | O(1) space
def check_kth_bit_set(n, k):
    return (n & (1 << (k-1)) != 0)

# O(1) time | O(1) space
def first_set_bit(n):
    max_k = len('{:b}'.format(n))
    k = 1
    while k <= max_k :
        if check_kth_bit_set(n, k):
            return k
        k += 1

# O(log b) time | O(1) space
# def count_bits(n: int) -> int:
#     bitsCounter = 0
#     while ((1 << bitsCounter)) <= n:
#         bitsCounter += 1
#     return bitsCounter

def count_bits(n: int) -> int:
    bitsCount = 0
    while (1 << bitsCount) <= n:
        bitsCount += 1
    return bitsCount

if __name__ == '__main__':
    # Check whether a kth bit is set or not : n & (1 << (k-1))
    # 12 = 1100
    assert check_kth_bit_set(12, 1) == False
    assert check_kth_bit_set(12, 2) == False
    assert check_kth_bit_set(12, 3) == True
    assert check_kth_bit_set(12, 4) == True

    arr = [5, 10, 15, 16, 26, 13, 10, 42, 8, 18]
    for ele in arr:
        print ("First set bit for %d -> %s = %d" % (ele, '{:b}'.format(ele), first_set_bit(ele)))

    # Counting bits in an integer
    arr = [5, 10, 15, 16, 26, 13, 10, 42, 8, 18]
    for ele in arr:
        ground_truth = '{:b}'.format(ele)
        assert len(ground_truth) == count_bits(ele), "Mismatch for %d: %d => %d" % (ele, ground_truth, count_bits(ele))
