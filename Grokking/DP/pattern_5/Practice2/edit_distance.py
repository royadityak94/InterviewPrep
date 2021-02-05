'''
Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or replacing characters. Write a function to calculate the count of the minimum number of edit operations.
'''

# O(3^(m+n)) time | O(m+n) space
def edit_distance(s1, s2):
    return edit_distance_recursive(s1, s2, 0, 0)

def edit_distance_recursive(s1, s2, i, j):
    if i == len(s1):
        return len(s2)-j
    if j == len(s2):
        return len(s1)-i

    if s1[i] == s2[j]:
        return edit_distance_recursive(s1, s2, i+1, j+1)

    withoutI = 1 + edit_distance_recursive(s1, s2, i+1, j)
    withoutJ = 1 + edit_distance_recursive(s1, s2, i, j+1)
    withoutBoth = 1 + edit_distance_recursive(s1, s2, i+1, j+1)
    return min(withoutI, withoutJ, withoutBoth)

# O(mn) time | O(mn) space
def edit_distance_td(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return edit_distance_td_recursive(dp, s1, s2, 0, 0)

def edit_distance_td_recursive(dp, s1, s2, i, j):
    if i == len(s1):
        return len(s2)-j
    if j == len(s2):
        return len(s1)-i

    if dp[i][j] == -1:
        if s1[i] == s2[j]:
            return edit_distance_td_recursive(dp, s1, s2, i+1, j+1)

        withoutI = 1 + edit_distance_td_recursive(dp, s1, s2, i+1, j)
        withoutJ = 1 + edit_distance_td_recursive(dp, s1, s2, i, j+1)
        withoutBoth = 1 + edit_distance_td_recursive(dp, s1, s2, i+1, j+1)
        dp[i][j] = min(withoutI, withoutJ, withoutBoth)
    return dp[i][j]

# O(mn) time | O(mn) space
def edit_distance_btmup(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(n1+1):
        dp[i][0] = i

    for j in range(n2+1):
        dp[0][j] = j

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
    return dp[n1][n2]


if __name__ == '__main__':
    # Plain Recursion
    print (edit_distance('bat', 'but')) # 1
    print (edit_distance('abdca', 'cbda')) # 2
    print (edit_distance('passpot', 'ppsspqrt')) # 3
    # Top-Down DP
    print (edit_distance_td('bat', 'but')) # 1
    print (edit_distance_td('abdca', 'cbda')) # 2
    print (edit_distance_td('passpot', 'ppsspqrt')) # 3
    # Bottom-Up DP
    print (edit_distance_btmup('bat', 'but')) # 1
    print (edit_distance_btmup('abdca', 'cbda')) # 2
    print (edit_distance_btmup('passpot', 'ppsspqrt')) # 3
