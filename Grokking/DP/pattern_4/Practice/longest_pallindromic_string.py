'''
    Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.
    I/p('abdbca') -> 3, 'bdb'
    I/p('cddpd') -> 3, 'dpd'
    I/p('pqr') -> 1, 'p'|'q'|'r'
'''
from unittest import TestCase, main

def find_LPS_length(s1):
    return find_LPS_length_recursive(s1, 0, len(s1)-1)

def find_LPS_length_recursive(s1, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if s1[startIdx] == s1[endIdx]:
        remaining = endIdx - startIdx - 1
        if remaining == find_LPS_length_recursive(s1, startIdx+1, endIdx-1):
            return remaining + 2
    withoutStart = find_LPS_length_recursive(s1, startIdx+1, endIdx)
    withoutEnd = find_LPS_length_recursive(s1, startIdx, endIdx-1)
    return max(withoutStart, withoutEnd)

def find_LPS_length_td(s1):
    n = len(s1)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_LPS_length_td_recursive(dp, s1, 0, len(s1)-1)

def find_LPS_length_td_recursive(dp, s1, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if dp[startIdx][endIdx]:
        if s1[startIdx] == s1[endIdx]:
            remaining = endIdx - startIdx - 1
            if remaining == find_LPS_length_td_recursive(dp, s1, startIdx+1, endIdx-1):
                return remaining + 2
        withoutStart = find_LPS_length_td_recursive(dp, s1, startIdx+1, endIdx)
        withoutEnd = find_LPS_length_td_recursive(dp, s1, startIdx, endIdx-1)
        dp[startIdx][endIdx] = max(withoutStart, withoutEnd)
    return dp[startIdx][endIdx]

def find_LPS_length_btmup(s1):
    n = len(s1)
    dp = [[False for _ in range(n)] for _ in range(n)]
    maxLength = 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n)[::-1]:
        for j in range(i+1, n):
            if s1[i] == s1[j]:
                if (j-i) == 1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    maxLength = max(maxLength, (j-i+1))
    return maxLength

if __name__ == '__main__':
    #main()
    # Plain Recursion
    print (find_LPS_length('abdbca'))
    print (find_LPS_length('cddpd'))
    print (find_LPS_length('pqr'))
    # TopDown DP
    print (find_LPS_length_td('abdbca'))
    print (find_LPS_length_td('cddpd'))
    print (find_LPS_length_td('pqr'))
    # Bottomup DP
    print (find_LPS_length_btmup('abdbca'))
    print (find_LPS_length_btmup('cddpd'))
    print (find_LPS_length_btmup('pqr'))
