'''
'''

def is_regex_match(string, pattern):
    n1, n2 = len(string), len(pattern)
    dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
    dp[0][0] = True
    for j in range(1, n2+1):
        if pattern[j-1] == '*':
            dp[0][j] = True
        else:
            break

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if pattern[j-1] == string[i-1] or pattern[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
    return dp[n1][n2]


if __name__ == '__main__':
    assert(is_regex_match('klacmbyd', '*a?mb*d')) == True
    assert(is_regex_match('azmbyk', '*a?mb*d')) == False
    assert(is_regex_match('abmx', '*')) == True
