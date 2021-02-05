'''
    Given a string, find the length of its Longest Palindromic Substring (lps). In a palindromic string, elements read the same backward and forward.
    I/p('abdbca') -> 3, 'bdb'
    I/p('cddpd') -> 3, 'dpd'
    I/p('pqr') -> 1, 'p'|'q'|'r'
'''

def find_lps_length(st):
    return find_lps_length_recursive(st, 0, len(st)-1)

def find_lps_length_recursive(st, startIdx, endIdx):
    n = len(st)
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if st[startIdx] == st[endIdx]:
        remaining = endIdx - startIdx - 1
        if remaining == find_lps_length_recursive(st, startIdx+1, endIdx-1):
            return remaining + 2
    withoutStart = find_lps_length_recursive(st, startIdx+1, endIdx)
    withoutEnd = find_lps_length_recursive(st, startIdx, endIdx-1)
    return max(withoutStart, withoutEnd)

def find_lps_length_td(st):
    dp = [[-1 for _ in range(len(st))] for _ in range(len(st))]
    return find_lps_length_td_recursive(dp, st, 0, len(st)-1)

def find_lps_length_td_recursive(dp, st, startIdx, endIdx):
    n = len(st)
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if dp[startIdx][endIdx] == -1:
        if st[startIdx] == st[endIdx]:
            remaining = endIdx - startIdx - 1
            if remaining == find_lps_length_td_recursive(dp, st, startIdx+1, endIdx-1):
                return remaining + 2
        withoutStart = find_lps_length_td_recursive(dp, st, startIdx+1, endIdx)
        withoutEnd = find_lps_length_td_recursive(dp, st, startIdx, endIdx-1)
        dp[startIdx][endIdx] = max(withoutStart, withoutEnd)
    return dp[startIdx][endIdx]

def find_lps_length_btmup(st):
    n = len(st)
    dp = [[False for _ in range(n)] for _ in range(n)]
    maxLength = 1
    for i in range(n):
        dp[i][i] = True

    for i in range(n)[::-1]:
        for j in range(i+1, n):
            if st[i] == st[j]:
                if (j-i) == 1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    maxLength = max(maxLength, j-i+1)
    return maxLength

if __name__ == '__main__':
    #main()
    # Plain Recursion
    print (find_lps_length('abdbca'))
    print (find_lps_length('cddpd'))
    print (find_lps_length('pqr'))
    # TopDown DP
    print (find_lps_length_td('abdbca'))
    print (find_lps_length_td('cddpd'))
    print (find_lps_length_td('pqr'))
    # Bottomup DP
    print (find_lps_length_btmup('abdbca'))
    print (find_lps_length_btmup('cddpd'))
    print (find_lps_length_btmup('pqr'))
