'''
Given a string, find the minimum number of characters that we can remove to make it a palindrome.
'''

def min_del_make_pal(s1):
    c = min_del_make_pal_recursion(s1, 0, len(s1)-1)
    return len(s1)-c

def min_del_make_pal_recursion(s1, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if s1[startIdx] == s1[endIdx]:
        return 2 + min_del_make_pal_recursion(s1, startIdx+1, endIdx-1)
    withoutStart = min_del_make_pal_recursion(s1, startIdx+1, endIdx)
    withoutEnd = min_del_make_pal_recursion(s1, startIdx, endIdx-1)
    return max(withoutStart, withoutEnd)

def min_del_make_pal_td(s1):
    n = len(s1)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    c = min_del_make_pal_td_recursion(dp, s1, 0, len(s1)-1)
    return len(s1)-c

def min_del_make_pal_td_recursion(dp, s1, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1
    if dp[startIdx][endIdx] == -1:
        if s1[startIdx] == s1[endIdx]:
            return 2 + min_del_make_pal_td_recursion(dp, s1, startIdx+1, endIdx-1)
        withoutStart = min_del_make_pal_td_recursion(dp, s1, startIdx+1, endIdx)
        withoutEnd = min_del_make_pal_td_recursion(dp, s1, startIdx, endIdx-1)
        dp[startIdx][endIdx] = max(withoutStart, withoutEnd)
    return dp[startIdx][endIdx]

def min_del_make_pal_btmup(s1):
    n = len(s1)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n)[::-1]:
        for j in range(i+1, n):
            if s1[i] == s1[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return len(s1) - dp[0][n-1]


if __name__ == '__main__':
    # Plain Recursion
    print (min_del_make_pal('abdbca')) # 1
    print (min_del_make_pal('cddpd')) # 2
    print (min_del_make_pal('pqr'))
    # Top Down DP
    print (min_del_make_pal_td('abdbca'))
    print (min_del_make_pal_td('cddpd'))
    print (min_del_make_pal_td('pqr'))
    # Bottom Up DP
    print (min_del_make_pal_btmup('abdbca'))
    print (min_del_make_pal_btmup('cddpd'))
    print (min_del_make_pal_btmup('pqr'))
