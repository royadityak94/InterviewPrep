# Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters. Write a function to calculate the count of the minimum number of deletion and insertion operations.

# O(2^(m+n)) time | O(m+n) space
def min_del_ins(s1, s2):
    c = min_del_ins_recursive(s1, s2, 0, 0)
    return len(s1)-c, len(s2)-c

def min_del_ins_recursive(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1+min_del_ins_recursive(s1, s2, i+1, j+1)
    withoutI = min_del_ins_recursive(s1, s2, i+1, j)
    withoutJ = min_del_ins_recursive(s1, s2, i, j+1)
    return max(withoutI, withoutJ)

# O(mn) time | O(mn) space
def min_del_ins_td(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    c = min_del_ins_td_recursive(dp, s1, s2, 0, 0)
    return len(s1)-c, len(s2)-c

def min_del_ins_td_recursive(dp, s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if dp[i][j] == -1:
        if s1[i] == s2[j]:
            dp[i][j] = 1 + min_del_ins_td_recursive(dp, s1, s2, i+1, j+1)
        else:
            withoutI = min_del_ins_td_recursive(dp, s1, s2, i+1, j)
            withoutJ = min_del_ins_td_recursive(dp, s1, s2, i, j+1)
            dp[i][j] = max(withoutI, withoutJ)
    return dp[i][j]

# O(mn) time | O(mn) space
def min_del_ins_btmup(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return len(s1) - dp[n1][n2], len(s2) - dp[n1][n2]

if __name__ == '__main__':
    # Using simple recursion
    print (min_del_ins("abc", "fbc"))
    print (min_del_ins("abdca", "cbda"))
    print (min_del_ins("passport", "ppsspt"))
    # Using top-down DP
    print (min_del_ins_td("abc", "fbc"))
    print (min_del_ins_td("abdca", "cbda"))
    print (min_del_ins_td("passport", "ppsspt"))
    # Using bottom-up DP
    print (min_del_ins_btmup("abc", "fbc"))
    print (min_del_ins_btmup("abdca", "cbda"))
    print (min_del_ins_btmup("passport", "ppsspt"))
