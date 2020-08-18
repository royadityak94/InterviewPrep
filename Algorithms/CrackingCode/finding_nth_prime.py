# Finding nth prime using Seive of Eratosthenes
# Ref: https://codereview.stackexchange.com/questions/185219/finding-nth-prime-using-python-and-sieve-of-eratosthenes

# Importing the requisite packages
from itertools import islice
from math import log, ceil, pow

def upper_bound_for_nth_prime(n: int):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))

def find_prime(limit: int):
    num = [True] * (limit + 1)
    num[0] = num[1] = False
    
    for (i, is_prime) in enumerate(num):
        if is_prime:
            yield i
            for n in range(int(pow(i, 2)), limit+1, i):
                num[n] = False
                
def find_nth_prime(n: int):
    primes = find_prime(upper_bound_for_nth_prime(n))
    return next(islice(primes, n-1, n))

def test_find_nth_prime():
    assert find_nth_prime(2) == 3
    assert find_nth_prime(3) == 5

    assert find_nth_prime(10) == 29
    assert find_nth_prime(15) == 47
    assert find_nth_prime(81) == 419

    assert find_nth_prime(941) == 7417
    assert find_nth_prime(1000) == 7919

    assert find_nth_prime(10001) == 104743
    
if __name__ == '__main__':
    test_find_nth_prime()
