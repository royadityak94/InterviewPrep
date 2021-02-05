
# O(n + n ~ n) time | O(n+n ~ n) space
def interleaved_string_nondp(m, n, p):
    queue1, queue2 = list(m), list(n)

    for ch in p:
        if queue1 and ch in queue1[0]:
            queue1.pop(0)
        if queue2 and ch in queue2[0]:
            queue2.pop(0)
    return (not queue1) and (not queue2)

# O(2^n) time | O(n) space
def interleaved_string(m, n, p):
    return interleaved_string_recursive(m, n, p, 0, 0, 0)

def interleaved_string_recursive(m, n, p, mIndex, nIndex, pIndex):
    if pIndex == len(p):
        if mIndex == len(m) and nIndex == len(n):
            return True
        return False

    b1, b2 = False, False
    if mIndex < len(m) and m[mIndex] == p[pIndex]:
        b1 = interleaved_string_recursive(m, n, p, mIndex+1, nIndex, pIndex+1)
    if nIndex < len(n) and n[nIndex] == p[pIndex]:
        b2 = interleaved_string_recursive(m, n, p, mIndex, nIndex+1, pIndex+1)
    return b1 or b2

# O(mn) time | O(mnp) space
def interleaved_string_td(m, n, p):
    dp = [[[-1 for _ in range(len(p)+1)] for _ in range(len(n)+1)] for _ in range(len(m)+1)]
    return interleaved_string_td_recursive(dp, m, n, p, 0, 0, 0)

def interleaved_string_td_recursive(dp, m, n, p, mIndex, nIndex, pIndex):
    if pIndex == len(p):
        if mIndex == len(m) and nIndex == len(n):
            return True
        return False

    if dp[mIndex][nIndex][pIndex] == -1:
        b1, b2 = False, False
        if mIndex < len(m) and m[mIndex] == p[pIndex]:
            b1 = interleaved_string_td_recursive(dp, m, n, p, mIndex+1, nIndex, pIndex+1)
        if nIndex < len(n) and n[nIndex] == p[pIndex]:
            b2 = interleaved_string_td_recursive(dp, m, n, p, mIndex, nIndex+1, pIndex+1)
        dp[mIndex][nIndex][pIndex] = b1 or b2
    return dp[mIndex][nIndex][pIndex]



if __name__ == '__main__':
    # Non-DP Optimized Implementations
    print (interleaved_string_nondp('abd', 'cef', 'abcdef')) # True
    print (interleaved_string_nondp('abd', 'cef', 'abcbef')) # False
    print (interleaved_string_nondp('abc', 'def', 'abdccf')) # False
    print (interleaved_string_nondp('abcdef', 'mnop', 'mnaobcdepf')) # True
    print (interleaved_string_nondp('abc', 'cef', 'abecdf')) # False

    # DP (Plain Recursion)
    print ('----------------------------')
    print (interleaved_string('abd', 'cef', 'abcdef')) # True
    print (interleaved_string('abd', 'cef', 'abcbef')) # False
    print (interleaved_string('abc', 'def', 'abdccf')) # False
    print (interleaved_string('abcdef', 'mnop', 'mnaobcdepf')) # True
    print (interleaved_string('abc', 'cef', 'abecdf')) # False

    # DP (Top-Down)
    print ('----------------------------')
    print (interleaved_string_td('abd', 'cef', 'abcdef')) # True
    print (interleaved_string_td('abd', 'cef', 'abcbef')) # False
    print (interleaved_string_td('abc', 'def', 'abdccf')) # False
    print (interleaved_string_td('abcdef', 'mnop', 'mnaobcdepf')) # True
    print (interleaved_string_td('abc', 'cef', 'abecdf')) # False
