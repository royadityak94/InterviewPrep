# Source: https://www.hackerrank.com/challenges/flipping-bits/problem

def flippingBits(n):
    n_bin = '{:032b}'.format(n)[2:]
    n_bin = n_bin.replace('0', 't')
    n_bin = n_bin.replace('1', '0')
    n_bin = n_bin.replace('t', '1')

    return int(n_bin, 2)


# Another solution
# for _ in range(input()):
#     s = 2**32 ^ int(raw_input())
#     t = str(bin(s))[2:]
#     t = t.replace('0','2')
#     t = t.replace('1','0')
#     t = t.replace('2','1')
#     print int(t,2)


if __name__ == '__main__':
    print (1, flippingBits(1))

#
# 0b1111111111111111111111111111
# 00000000000000000000000000000001
