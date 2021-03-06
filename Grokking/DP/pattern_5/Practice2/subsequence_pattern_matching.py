'''
Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.
Example 1: Input: string: “baxmx”, pattern: “ax”, Output: 2, Explanation: {baxmx, baxmx}.
Example 2: Input: string: “tomorrow”, pattern: “tor”, Output: 4, Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.
'''

def sspm(s1, s2):
    return sspm_recursive(s1, s2, 0, 0)

def sspm_recursive(s1, s2, i, j):
    if j == len(s2):
        return 1
    if i == len(s1):
        return 0
    with_current = 0
    if s1[i] == s2[j]:
        with_current = sspm_recursive(s1, s2, i+1, j+1)
    withoutI = sspm_recursive(s1, s2, i+1, j)
    return with_current + withoutI

def sspm_td(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return sspm_td_recursive(dp, s1, s2, 0, 0)

def sspm_td_recursive(dp, s1, s2, i, j):
    if j == len(s2):
        return 1
    if i == len(s1):
        return 0
    if dp[i][j] == -1:
        with_current = 0
        if s1[i] == s2[j]:
            with_current = sspm_td_recursive(dp, s1, s2, i+1, j+1)
        withoutI = sspm_td_recursive(dp, s1, s2, i+1, j)
        dp[i][j] = with_current + withoutI
    return dp[i][j]

def sspm_btmup(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(n1+1):
        dp[i][0] = 1

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            dp[i][j] = dp[i-1][j]
            if s1[i-1] == s2[j-1]:
                dp[i][j] += dp[i-1][j-1]
    return dp[n1][n2]

if __name__ == '__main__':
    # Plain Recursion
    print (sspm('baxmx', 'ax'))
    print (sspm('tomorrow', 'tor'))
    # Top-Down Recursion
    print (sspm_td('baxmx', 'ax'))
    print (sspm_td('tomorrow', 'tor'))
    # Bottom-Up Recursion
    print (sspm_btmup('baxmx', 'ax'))
    print (sspm_btmup('tomorrow', 'tor'))
