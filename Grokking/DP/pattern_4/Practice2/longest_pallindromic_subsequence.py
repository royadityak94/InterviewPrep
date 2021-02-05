'''Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence,
elements read the same backward and forward. A subsequence is a sequence that can be derived from another
sequence by deleting some or no elements without changing the order of the remaining elements.
Ex: Inp('abdbca'), O/p: 5 ('abdba')
Ex: Inp('cddpd'), O/p: 3 ('ddd')
Ex: Inp('pqr'), O/p: 1 ('p'/'q'/'r')
'''

def find_lpss(st):
    return find_lpss_recursive(st, 0, len(st)-1)

def find_lpss_recursive(st, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    if startIdx == endIdx:
        return 1

    if st[startIdx] == st[endIdx]:
        return 2 + find_lpss_recursive(st, startIdx+1, endIdx-1)

    withoutStart = find_lpss_recursive(st, startIdx+1, endIdx)
    withoutEnd = find_lpss_recursive(st, startIdx, endIdx-1)
    return max(withoutStart, withoutEnd)

def find_lpss_td(st):
    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_lpss_td_recursive(dp, st, 0, len(st)-1)

def find_lpss_td_recursive(dp, st, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    if startIdx == endIdx:
        return 1
    if dp[startIdx][endIdx] == -1:
        if st[startIdx] == st[endIdx]:
            return 2 + find_lpss_td_recursive(dp, st, startIdx+1, endIdx-1)

        withoutStart = find_lpss_td_recursive(dp, st, startIdx+1, endIdx)
        withoutEnd = find_lpss_td_recursive(dp, st, startIdx, endIdx-1)
        dp[startIdx][endIdx] = max(withoutStart, withoutEnd)
    return dp[startIdx][endIdx]

def find_lpss_btmup(st):
    n = len(st)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n)[::-1]:
        for j in range(i+1, n):
            if st[i] == st[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

if __name__ == '__main__':
    #main()
    # Plain Recursion
    print(find_lpss('abdbca'))
    print(find_lpss('cddpd'))
    print(find_lpss('pqr'))
    # TopDown DP
    print(find_lpss_td('abdbca'))
    print(find_lpss_td('cddpd'))
    print(find_lpss_td('pqr'))
    # Bottomup DP
    print(find_lpss_btmup('abdbca'))
    print(find_lpss_btmup('cddpd'))
    print(find_lpss_btmup('pqr'))
