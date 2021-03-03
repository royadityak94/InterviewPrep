'''
Solving problems using bitwise and operator
'''
from typing import List
import random
import math

# O(b) time | O(1) space, b=Total bits in n
def count_set_bits(n: int) -> int:
    setBitCounter = 0
    while n:
        # or, setBitCounter += (n & 1)
        if n & 1:
            setBitCounter += 1
        n >>= 1
    return setBitCounter

# Brian Kernighan’s algorithm
# O(s_b) time | O(1) space, s_b=Total set bits in n
def count_set_bits_bk(n: int) -> int:
    setBitCounter = 0
    while n:
        n &= n-1
        setBitCounter += 1
    return setBitCounter

# O(1) time | O(1) space
def odd_even_check(n: int) -> bool:
    return 'even' if n & 1 == 0 else 'odd'

# O(1) time | O(1) space - Brian Kernighan’s algorithm
def power_of_two(n: int) -> bool:
    return (n & (n-1) == 0)


if __name__ == '__main__':
    # count set bits in a given integer
    arr = [4, 3, 6, 9, 13, 15, 19, 24, 22, 125]
    for ele in arr:
        brepr = '{:b}'.format(ele)
        assert count_set_bits(ele) == brepr.count('1')
        assert count_set_bits_bk(ele) == brepr.count('1')

    # Even/Odd Number usign LSB
    arr = random.sample(range(0, 255), 30)
    for ele in arr:
        actual = 'odd' if ele % 2 else 'even'
        assert odd_even_check(ele) == actual

    # Power of 2 check
    arr = [2, 4, 6, 8, 10, 12, 16, 20, 32, 40, 50, 64, 100, 128, 250, 256]
    all_power_of_two = [2**i for i in range(math.floor(math.log2(max(arr)))+1)]
    for ele in arr:
        assert power_of_two(ele) == (ele in all_power_of_two), "Failed for %d: %r" % (ele, power_of_two(ele))
