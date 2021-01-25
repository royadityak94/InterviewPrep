# Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters. Write a function to calculate the count of the minimum number of deletion and insertion operations.

# O(m*n) time | O(m*n) space
def min_del_ins_btmup(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    maxLength = 0
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
    # print (min_del_ins("abc", "fbc"))
    # print (min_del_ins("passport", "ppsspt"))
    # # Using top-down DP
    # print (min_del_ins_td("abdca", "cbda"))
    # print (min_del_ins_td("passport", "ppsspt"))
    # Using bottom-up DP
    print (min_del_ins_btmup("abc", "fbc"))
    print (min_del_ins_btmup("abdca", "cbda"))
    print (min_del_ins_btmup("passport", "ppsspt"))
