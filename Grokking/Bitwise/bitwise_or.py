'''
Problem solving using bitwise OR
'''
'''
Source: https://www.educative.io/collection/page/6726373949308928/6138754633826304/5645966360182784
Suppose, a = 0010 and b = 0110, so c = 0101
after flipping one bits in a, b, we obtain: 0001 and 0100 == c.
'''
# O(32 ~ 1) time | O(1)
# 2x speedup over required_flips_1
def required_flips(a, b, c):
    flips = 0
    for i in range(32):
        bitC = (c >> i) & 1
        bitB = (b >> i) & 1
        bitA = (a >> i) & 1

        if (bitA | bitB) != bitC:
            if bitA and bitB:
                flips += 2
            else:
                # Cases: {bitC = 0}, {bitA and bitB = 0}
                flips += 1

    return flips

# O(log(max(a, b, c))) time | O(1) space
def required_flips_1(a, b, c):
    flips = 0
    while (a | b | c):
        bitC = c & 1
        bitB = b & 1
        bitA = a & 1

        if (bitA | bitB) != bitC:
            if bitA and bitB:
                flips += 2
            else:
                # Cases: {bitC = 0}, {bitA and bitB = 0}
                flips += 1
        a = a >> 1
        b = b >> 1
        c = c >> 1
    return flips

# 3x speedup over required_flips, 6x speedup over required_flips_1
def required_flips_optimized(a, b, c):
    flips = 0
    for i in range(32):
        bit = 1 << i
        if bit & c:
            if not ((bit & a) or (bit & b)):
                # i.e. when LSB for c is set, and not for a or b
                flips += 1
        else:
            # if a is set, flip, same for b => both (flips + 2), only one (flips + 1)
            if bit & a:
                flips += 1
            if bit & b:
                flips += 1
    return flips



if __name__ == '__main__':
    # Minimum number of flips Required To Make a|b Equal to c, i.e. a | b = c.
    # The flip operation consists of changing any single bit 1 to 0 or changing the bit 0 to 1 in their binary representation
    assert required_flips(2, 6, 5) == 3
    assert required_flips_1(2, 6, 5) == 3
    assert required_flips_optimized(2, 6, 5) == 3
