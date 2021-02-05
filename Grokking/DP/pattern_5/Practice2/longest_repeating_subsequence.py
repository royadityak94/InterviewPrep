'''
Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).
'''
# O(2^n) time | O(n) space
def lrss(s1):
    return lrss_recursive(s1, 0, 0)

def lrss_recursive(s1, i, j):
    if i == len(s1) or j == len(s1):
        return 0
    if i != j and s1[i] == s1[j]:
        return 1 + lrss_recursive(s1, i+1, j+1)
    withoutI = lrss_recursive(s1, i+1, j)
    withoutJ = lrss_recursive(s1, i, j+1)
    return max(withoutI, withoutJ)

# O(n^2) time | O(n^2) space
def lrss_td(s1):
    dp = [[-1 for _ in range(len(s1))] for _ in range(len(s1))]
    return lrss_td_recursive(dp, s1, 0, 0)

def lrss_td_recursive(dp, s1, i, j):
    if i == len(s1) or j == len(s1):
        return 0
    if dp[i][j] == -1:
        if i != j and s1[i] == s1[j]:
            return 1 + lrss_td_recursive(dp, s1, i+1, j+1)
        withoutI = lrss_td_recursive(dp, s1, i+1, j)
        withoutJ = lrss_td_recursive(dp, s1, i, j+1)
        dp[i][j] = max(withoutI, withoutJ)
    return dp[i][j]

# O(n^2) time | O(n^2) space
def lrss_btmup(s1):
    n = len(s1)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and s1[i-1] == s1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]

if __name__ == '__main__':
    # Plain Recursion
    print (lrss('tomorrow')) # 2 ('or')
    print (lrss('aabdbcec')) # 3 ('abc')
    print (lrss('fmff')) # 2 ('ff')
    # Top-Down Recursion
    print (lrss_td('tomorrow')) # 2 ('or')
    print (lrss_td('aabdbcec')) # 3 ('abc')
    print (lrss_td('fmff')) # 2 ('ff')
    # Bottom-Up Recursion
    print (lrss_btmup('tomorrow')) # 2 ('or')
    print (lrss_btmup('aabdbcec')) # 3 ('abc')
    print (lrss_btmup('fmff')) # 2 ('ff')
