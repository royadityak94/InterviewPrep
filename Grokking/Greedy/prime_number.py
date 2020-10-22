import math

def primality(n):
    # Time Complexity: O(sqrt(N))
    if n == 2:
        return "Prime"
    elif (n == 1) or (n&1 == 0):
        return "Not prime(x1)"
    else:
        for itr in range(2, math.ceil(math.sqrt(n)+1)):
            if not n % itr:
                return "Not prime"
    return "Prime"


if __name__ == '__main__':
    for ele in [5, 11, 2, 3, 6, 18, 21, 23]:
        print (ele, " : ", primality(ele))
