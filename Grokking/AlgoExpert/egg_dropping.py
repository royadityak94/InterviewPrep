'''
    Source: https://leetcode.com/problems/super-egg-drop/
    Given some number of floors and some number of eggs, what is the minimum number of attempts
    it will take to find out from which floor egg will break.
'''

def min_egg_attempts(floors, eggs):
    if eggs < 2 or floors < 2:
        return floors
    min_value = float('inf')
    for fl in range(2, floors):
        for j in range(1, eggs):
            max_ = 1 + max(min_egg_attempts(fl-1, eggs-1), min_egg_attempts(floors-fl, eggs))
            min_value = min(min_value, max_)
    return min_value

def min_egg_attempts_btmup(floors, eggs):
    if eggs == 1 or floors < 2:
        return floors

    dp = [[0 for _ in range(floors+1)] for _ in range(eggs)]

    for j in range(floors+1):
        dp[0][j] = j

    for i in range(1, eggs):
        for j in range(1, floors+1):
            dp[i][j] = 1 + min(max(dp[i-1][k-1], dp[i][j-k]) for k in range(1, j+1))
    return dp[eggs-1][floors]


if __name__ == '__main__':
    # Plain Recursion
    print (min_egg_attempts(10, 2)) # 4
    print (min_egg_attempts(6, 2)) # 3
    print (min_egg_attempts(4, 2)) # 3
    #
    # # Dynamic Prog
    print (min_egg_attempts_btmup(10, 2)) # 4
    print (min_egg_attempts_btmup(6, 2)) # 3
    print (min_egg_attempts_btmup(4, 2)) #3
