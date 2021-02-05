'''Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence,
elements read the same backward and forward. A subsequence is a sequence that can be derived from another
sequence by deleting some or no elements without changing the order of the remaining elements.
Ex: Inp('abdbca'), O/p: 5 ('abdba')
Ex: Inp('cddpd'), O/p: 3 ('ddd')
Ex: Inp('pqr'), O/p: 1 ('p'/'q'/'r')
'''

def find_lpss(s1):
    return find_lpss_recursive(s1, 0, len(s1)-1)

def find_lpss_recursive(s1, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if s1[startIdx] == s1[endIdx]:
        return 2 + find_lpss_recursive(s1, startIdx+1, endIdx-1)

    withoutStart = find_lpss_recursive(s1, startIdx+1, endIdx)
    withoutEnd = find_lpss_recursive(s1, startIdx, endIdx-1)
    return max(withoutStart, withoutEnd)

def find_lpss_td(s1):
    n = len(s1)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_lpss_td_recursive(dp, s1, 0, len(s1)-1)

def find_lpss_td_recursive(dp, s1, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if dp[startIdx][endIdx] == -1:
        if s1[startIdx] == s1[endIdx]:
            return 2 + find_lpss_td_recursive(dp, s1, startIdx+1, endIdx-1)

        withoutStart = find_lpss_td_recursive(dp, s1, startIdx+1, endIdx)
        withoutEnd = find_lpss_td_recursive(dp, s1, startIdx, endIdx-1)
        dp[startIdx][endIdx] = max(withoutStart, withoutEnd)
    return dp[startIdx][endIdx]

def find_lpss_btmup(s1):
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
