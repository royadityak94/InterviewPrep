# Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.
# ("abdca", "cbda") -> "bda" (Ans: 3)
# ("passport", "ppsspt") -> "psspt" (Ans: 5)

# O(2^(m+n)) time | O(m+n) space
def longest_common_subsequence(s1, s2):
    return longest_common_subsequence_recursive(s1, s2, 0, 0)

def longest_common_subsequence_recursive(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    with_current = 0
    if s1[i] == s2[j]:
        return 1 + longest_common_subsequence_recursive(s1, s2, i+1, j+1)
    withoutI = longest_common_subsequence_recursive(s1, s2, i+1, j)
    withoutJ = longest_common_subsequence_recursive(s1, s2, i, j+1)
    return max(withoutI, withoutJ)

# O(m*n) time | O(m*n) space
def longest_common_subsequence_td(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return longest_common_subsequence_td_recursive(dp, s1, s2, 0, 0)

def longest_common_subsequence_td_recursive(dp, s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0

    if dp[i][j] == -1:
        with_current = 0
        if s1[i] == s2[j]:
            dp[i][j] = 1 + longest_common_subsequence_td_recursive(dp, s1, s2, i+1, j+1)
        else:
            withoutI = longest_common_subsequence_td_recursive(dp, s1, s2, i+1, j)
            withoutJ = longest_common_subsequence_td_recursive(dp, s1, s2, i, j+1)
            dp[i][j] = max(withoutI, withoutJ)
    return dp[i][j]

# O(m*n) time | O(m*n) space
def longest_common_subsequence_btmup(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n1][n2]

if __name__ == '__main__':
    # Using simple recursion
    print (longest_common_subsequence("abdca", "cbda"))
    print (longest_common_subsequence("passport", "ppsspt"))
    # Using top-down DP
    print (longest_common_subsequence_td("abdca", "cbda"))
    print (longest_common_subsequence_td("passport", "ppsspt"))
    # Using bottom-up DP
    print (longest_common_subsequence_btmup("abdca", "cbda"))
    print (longest_common_subsequence_btmup("passport", "ppsspt"))
