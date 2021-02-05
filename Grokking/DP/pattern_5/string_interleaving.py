
def interleaved_string_nondp(m, n, p):
    queue1, queue2 = list(m), list(n)
    mIndex, nIndex = 0, 0

    for ch in p:
        if queue1 and queue1[0] == ch:
            queue1.pop(0)
        if queue2 and queue2[0] == ch:
            queue2.pop(0)
    return (not len(queue1)) and (not len(queue2))


def interleaved_string(m, n, p):
    return interleaved_string_recursion(m, n, p, 0, 0, 0)

def interleaved_string_recursion(m, n, p, mIndex, nIndex, pIndex):
    mLen, nLen, pLen = len(m), len(n), len(p)
    if pIndex == pLen:
        if mIndex == mLen and nIndex == nLen:
            return True
        else:
            return False

    b1, b2 = False, False
    if mIndex < mLen and m[mIndex] == p[pIndex]:
        b1 = interleaved_string_recursion(m, n, p, mIndex+1, nIndex, pIndex+1)
    if nIndex < nLen and n[nIndex] == p[pIndex]:
        b2 = interleaved_string_recursion(m, n, p, mIndex, nIndex+1, pIndex+1)
    return b1 or b2

def get_dp_key(mIndex, nIndex, pIndex):
    return '%d|%d|%d' % (mIndex, nIndex, pIndex)

def interleaved_string_td(m, n, p):
    dp = {}
    return interleaved_string_td_recursion(dp, m, n, p, 0, 0, 0)

def interleaved_string_td_recursion(dp, m, n, p, mIndex, nIndex, pIndex):
    mLen, nLen, pLen = len(m), len(n), len(p)
    if pIndex == pLen:
        if mIndex == mLen and nIndex == nLen:
            return True
        else:
            return False

    dp_key = get_dp_key(mIndex, nIndex, pIndex)
    if dp_key not in dp:
        b1, b2 = False, False
        if mIndex < mLen and m[mIndex] == p[pIndex]:
            b1 = interleaved_string_td_recursion(dp, m, n, p, mIndex+1, nIndex, pIndex+1)
        if nIndex < nLen and n[nIndex] == p[pIndex]:
            b2 = interleaved_string_td_recursion(dp, m, n, p, mIndex, nIndex+1, pIndex+1)
        dp[dp_key] = b1 or b2
    return dp[dp_key]

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
