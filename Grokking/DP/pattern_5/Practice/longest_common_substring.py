# Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.
# ("abdca", "cbda") -> "bd"
# ("passport", "ppsspt") -> "ssp"

def find_LCS_length(s1, s2):
    return find_LCS_length_recursive(s1, s2, 0, 0, 0)

def find_LCS_length_recursive(s1, s2, i, j, count):
    if i == len(s1) or j == len(s2):
        return count

    if s1[i] == s2[j]:
        count = find_LCS_length_recursive(s1, s2, i+1, j+1, count+1)

    withoutI = find_LCS_length_recursive(s1, s2, i+1, j, 0)
    withoutJ = find_LCS_length_recursive(s1, s2, i, j+1, 0)
    return max(count, max(withoutI, withoutJ))

def find_LCS_length_td(s1, s2):
    maxLength = min(len(s1), len(s2))
    dp = [[[-1 for _ in range(maxLength)] for _ in range(len(s2))] for _ in range(len(s1))]
    return find_LCS_length_td_recursive(dp, s1, s2, 0, 0, 0)

def find_LCS_length_td_recursive(dp, s1, s2, i, j, count):
    if i == len(s1) or j == len(s2):
        return count

    if dp[i][j][count] == -1:
        c = count
        if s1[i] == s2[j]:
            c = find_LCS_length_td_recursive(dp, s1, s2, i+1, j+1, c+1)

        withoutI = find_LCS_length_td_recursive(dp, s1, s2, i+1, j, 0)
        withoutJ = find_LCS_length_td_recursive(dp, s1, s2, i, j+1, 0)
        dp[i][j][count] = max(c, max(withoutI, withoutJ))
    return dp[i][j][count]

def find_LCS_length_btmup(s1, s2):
    n1, n2 = len(s1), len(s2)
    maxLength = float('-inf')
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxLength = max(maxLength, dp[i][j])
    return maxLength

if __name__ == '__main__':
    # Using simple recursion
    print (find_LCS_length("abdca", "cbda"))
    print (find_LCS_length("passport", "ppsspt"))
    print (find_LCS_length("makauttdes", "auttdes"))
    # Using top-down DP
    print (find_LCS_length_td("abdca", "cbda"))
    print (find_LCS_length_td("passport", "ppsspt"))
    print (find_LCS_length_td("makauttdes", "auttdes"))
    # # Using bottom-up DP
    print (find_LCS_length_btmup("abdca", "cbda"))
    print (find_LCS_length_btmup("passport", "ppsspt"))
    print (find_LCS_length_btmup("makauttdes", "auttdes"))
