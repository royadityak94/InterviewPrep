'''
    Source: https://leetcode.com/problems/wildcard-matching/ + AlgoExpert
    Wildcard matching using DP
'''


def match_wildcards(string, pattern):
    dp = [[False for _ in range(len(pattern)+1)] for _ in range(len(string)+1)]
    dp[0][0] = True

    for j in range(1, len(pattern)+1):
        if pattern[j-1] == '*':
            break
        dp[0][j] = True

    for i in range(1, len(string)+1):
        for j in range(1, len(pattern)+1):
            if pattern[j-1] in {'?', string[i-1]}:
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]

    return dp[len(string)][len(pattern)]

if __name__ == '__main__':
    print (match_wildcards('xbyz', 'x?y*z'))
    print (match_wildcards('a', '*'))
    print (match_wildcards('cb', '?a'))
    print (match_wildcards('adceb', '*a*b'))
    print (match_wildcards('aab', 'c*a*b'))
