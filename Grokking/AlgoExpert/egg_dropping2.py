'''
    Source: https://leetcode.com/problems/super-egg-drop/
    Given some number of floors and some number of eggs, what is the minimum number of attempts
    it will take to find out from which floor egg will break.
'''


def min_egg_attempts_btmup(floors, eggs):
    if eggs == 1 or floors < 2:
        return floors

    dp = [[0 for _ in range(floors+1)] for _ in range(eggs)]
    for j in range(floors+1):
        dp[0][j] = j

    for i in range(1, eggs):

        for j in range(1, floors+1):
            considered_idxes = []
            considered_maxes = []


            for k in range(1, j+1):
                considered_maxes += max(dp[i-1][k-1], dp[i][j-k]),
                considered_idxes += (i-1, k-1), '->', dp[i-1][k-1], (i, j-k), '->', dp[i][j-k],

            dp[i][j] = 1 + min(considered_maxes)

            #print (considered_maxes)
            #considered_idxes.sort(key=lambda x: (x[0], x[1]))
            print ("\t ", j, considered_idxes, considered_maxes)
            #dp[i][j] = 1 + min(max(dp[i-1][k-1], dp[i][j-k]) for k in range(1, j+1))

    for i in range(len(dp)):
        print (dp[i])
    return dp[eggs-1][floors]

if __name__ == '__main__':
    print (min_egg_attempts_btmup(4, 2))
