'''
Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.
'''

# O(2^(m+n)) time | O(m+n) space
def scss(s1, s2):
    return scss_recursive(s1, s2, 0, 0)

def scss_recursive(s1, s2, i, j):
    if i == len(s1):
        return len(s2)-j
    if j == len(s2):
        return len(s1)-i

    if s1[i]==s2[j]:
        return 1 + scss_recursive(s1, s2, i+1, j+1)
    withoutI = 1 + scss_recursive(s1, s2, i+1, j)
    withoutJ = 1 + scss_recursive(s1, s2, i, j+1)
    return min(withoutI, withoutJ)

# O(mn) time | O(mn) space
def scss_td(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return scss_td_recursive(dp, s1, s2, 0, 0)

def scss_td_recursive(dp, s1, s2, i, j):
    if i == len(s1):
        return len(s2)-j
    if j == len(s2):
        return len(s1)-i

    if dp[i][j] == -1:
        if s1[i]==s2[j]:
            dp[i][j] = 1 + scss_td_recursive(dp, s1, s2, i+1, j+1)
        else:
            withoutI = 1 + scss_td_recursive(dp, s1, s2, i+1, j)
            withoutJ = 1 + scss_td_recursive(dp, s1, s2, i, j+1)
            dp[i][j] = min(withoutI, withoutJ)
    return dp[i][j]

# O(mn) time | O(mn) space
def scss_btmup(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(n1+1):
        dp[i][0] = i
    for j in range(n2+1):
        dp[0][j] = j

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] ==  s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[n1][n2]

if __name__ == '__main__':
    # Plain Recursion
    print (scss('abcf', 'bdcf'))
    print (scss('dynamic', 'programming'))
    # Top-down DP
    print (scss_td('abcf', 'bdcf'))
    print (scss_td('dynamic', 'programming'))
    # Bottom-up DP
    print (scss_btmup('abcf', 'bdcf'))
    print (scss_btmup('dynamic', 'programming'))
