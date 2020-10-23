import math

def primality(n):
    # Time Complexity: O(sqrt(N))
    if n == 2:
        return "Prime"
    elif n == 1 or (not n&1):
        return "Not prime(x1)"
    else:
        for i in range(3, math.ceil(math.sqrt(n)+1)):
            if not n % i:
                return "Not prime(x2)"
        return "Prime"

if __name__ == '__main__':
    for ele in [5, 11, 2, 3, 6, 18, 21, 23]:
        print (ele, " : ", primality(ele))
