# O(2^(m+n)) time | O(m+n) space
def min_del_ins(s1, s2):
    c = min_del_ins_recursive(s1, s2, 0, 0)
    return len(s1)-c, len(s2)-c

def min_del_ins_recursive(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0

    if s1[i] == s2[j]:
        return 1 + min_del_ins_recursive(s1, s2, i+1, j+1)

    withoutI = min_del_ins_recursive(s1, s2, i+1, j)
    withoutJ = min_del_ins_recursive(s1, s2, i, j+1)
    return max(withoutI, withoutJ)

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

# O(m*n) time | O(m*n) space
def min_del_ins_btmup(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    maxLength = float('-inf')

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            maxLength = max(maxLength, dp[i][j])
    return len(s1)-maxLength, len(s2)-maxLength

if __name__ == '__main__':
    # Using simple recursion
    print (min_del_ins("abc", "fbc"))
    print (min_del_ins("abdca", "cbda"))
    print (min_del_ins("passport", "ppsspt"))
    print ('-----------------------')
    # # Using top-down DP
    print (min_del_ins_td("abc", "fbc"))
    print (min_del_ins_td("abdca", "cbda"))
    print (min_del_ins_td("passport", "ppsspt"))
    print ('-----------------------')
    # Using bottom-up DP
    print (min_del_ins_btmup("abc", "fbc"))
    print (min_del_ins_btmup("abdca", "cbda"))
    print (min_del_ins_btmup("passport", "ppsspt"))
