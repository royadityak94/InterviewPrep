# Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.
# ("abdca", "cbda") -> "bda" (Ans: 3)
# ("passport", "ppsspt") -> "psspt" (Ans: 5)

# O(2^(m+n)) time | O(m+n) space; m=len(s1), n=len(s2)
def lcs(s1, s2):
    return lcs_recursive(s1, s2, 0, 0)

def lcs_recursive(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + lcs_recursive(s1, s2, i+1, j+1)

    withoutI = lcs_recursive(s1, s2, i+1, j)
    withoutJ = lcs_recursive(s1, s2, i, j+1)
    return max(withoutI, withoutJ)

# O(m*n) time | O(m*n) space
def lcs_td(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return lcs_td_recursive(dp, s1, s2, 0, 0)

def lcs_td_recursive(dp, s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if dp[i][j] == -1:
        if s1[i] == s2[j]:
            dp[i][j] = 1 + lcs_td_recursive(dp, s1, s2, i+1, j+1)
        else:
            withoutI = lcs_td_recursive(dp, s1, s2, i+1, j)
            withoutJ = lcs_td_recursive(dp, s1, s2, i, j+1)
            dp[i][j] = max(withoutI, withoutJ)
    return dp[i][j]

# O(m*n) time | O(m*n) space
def lcs_btmup(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]




if __name__ == '__main__':
    # Using simple recursion
    print (lcs("abdca", "cbda"))
    print (lcs("passport", "ppsspt"))
    # Using top-down DP
    print (lcs_td("abdca", "cbda"))
    print (lcs_td("passport", "ppsspt"))
    # Using bottom-up DP
    print (lcs_btmup("abdca", "cbda"))
    print (lcs_btmup("passport", "ppsspt"))
