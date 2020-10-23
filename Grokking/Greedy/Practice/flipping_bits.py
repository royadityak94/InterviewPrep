# Source: https://www.hackerrank.com/challenges/flipping-bits/problem

def flippingBits(n):
    return n ^ 0xFFFFFFFF


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
