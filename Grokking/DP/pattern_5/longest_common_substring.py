# Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.
# ("abdca", "cbda") -> "bd"
# ("passport", "ppsspt") -> "ssp"

def find_LCS_length(s1, s2):
    # Time Complexity: O(3^(m+n)), Space Complexity: O(m+n); m=len(s1), n=len(s2)
    if not s1 or not s2:
        return 0
    return find_LCS_length_recursive(s1, s2, 0, 0, 0)

def find_LCS_length_recursive(s1, s2, i1, i2, count):
    if i1 == len(s1) or i2 == len(s2):
        return count

    if s1[i1] == s2[i2]:
        count = find_LCS_length_recursive(s1, s2, i1+1, i2+1, count+1)

    c1 = find_LCS_length_recursive(s1, s2, i1+1, i2, 0)
    c2 = find_LCS_length_recursive(s1, s2, i1, i2+1, 0)
    return max(count, max(c1, c2))

def find_LCS_length_td(s1, s2):
    # Time Complexity: O(m*n), Space Complexity: O(m*n); m=len(s1), n=len(s2)
    if not s1 or not s2:
        return 0
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    return find_LCS_length_td_recursive(dp, s1, s2, 0, 0, 0)

def find_LCS_length_td_recursive(dp, s1, s2, i1, i2, count):
    if i1 == len(s1) or i2 == len(s2):
        return count

    if not dp[i1][i2]:
        if s1[i1] == s2[i2]:
            count = find_LCS_length_recursive(s1, s2, i1+1, i2+1, count+1)

        c1 = find_LCS_length_recursive(s1, s2, i1+1, i2, 0)
        c2 = find_LCS_length_recursive(s1, s2, i1, i2+1, 0)
        dp[i1][i2] = max(count, max(c1, c2))
    return dp[i1][i2]

def find_LCS_length_btmup(s1, s2):
    if not s1 or not s2:
        return 0
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    maxLength = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
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
    # Using bottom-up DP
    print (find_LCS_length_btmup("abdca", "cbda"))
    print (find_LCS_length_btmup("passport", "ppsspt"))
    print (find_LCS_length_btmup("makauttdes", "auttdes"))
