# Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.
# ("abdca", "cbda") -> "bda" (Ans: 3)
# ("passport", "ppsspt") -> "psspt" (Ans: 5)

def longest_common_subsequence(s1, s2):
    if not s1 or not s2:
        return 0
    return longest_common_subsequence_recursive(s1, s2, 0, 0)

def longest_common_subsequence_recursive(s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if s1[i1] == s2[i2]:
        return 1 + longest_common_subsequence_recursive(s1, s2, i1+1, i2+1)

    c1 = longest_common_subsequence_recursive(s1, s2, i1+1, i2)
    c2 = longest_common_subsequence_recursive(s1, s2, i1, i2+1)
    return max(c1, c2)

def longest_common_subsequence_td(s1, s2):
    if not s1 or not s2:
        return 0
    dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    return longest_common_subsequence_td_recursive(dp, s1, s2, 0, 0)

def longest_common_subsequence_td_recursive(dp, s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if not dp[i1][i2]:
        if s1[i1] == s2[i2]:
            dp[i1][i2] = 1 + longest_common_subsequence_recursive(s1, s2, i1+1, i2+1)

        c1 = longest_common_subsequence_recursive(s1, s2, i1+1, i2)
        c2 = longest_common_subsequence_recursive(s1, s2, i1, i2+1)
        dp[i1][i2] = max(c1, c2)
    return dp[i1][i2]

def longest_common_subsequence_btmup(s1, s2):
    if not s1 or not s2:
        return 0
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

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
