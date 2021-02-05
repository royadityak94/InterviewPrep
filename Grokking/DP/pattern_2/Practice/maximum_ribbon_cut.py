# We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. Now we need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

def mrc(lengths, capacity):
    return mrc_recursive(lengths, capacity, 0)

def mrc_recursive(lengths, capacity, currentIdx):
    if capacity == 0:
        return 0
    if currentIdx == len(lengths):
        return float('-inf')

    with_current = float('-inf')
    if lengths[currentIdx] <= capacity:
        with_current = 1 + mrc_recursive(lengths, capacity-lengths[currentIdx], currentIdx)
    without_current = mrc_recursive(lengths, capacity, currentIdx+1)
    return max(with_current, without_current)

def mrc_dp(lengths, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(lengths))]
    return mrc_td_recursive(dp, lengths, capacity, 0)

def mrc_td_recursive(dp, lengths, capacity, currentIdx):
    if capacity == 0:
        return 0
    if currentIdx == len(lengths):
        return float('-inf')

    if dp[currentIdx][capacity] == -1:
        with_current = float('-inf')
        if lengths[currentIdx] <= capacity:
            with_current = 1 + mrc_td_recursive(dp, lengths, capacity-lengths[currentIdx], currentIdx)
        without_current = mrc_td_recursive(dp, lengths, capacity, currentIdx+1)
        dp[currentIdx][capacity] = max(with_current, without_current)
    return dp[currentIdx][capacity]

def mrc_btmup(lengths, capacity):
    n = len(lengths)
    dp = [[float('-inf') for _ in range(capacity+1)] for _ in range(len(lengths))]
    for i in range(len(lengths)):
        dp[i][0] = 0
    for j in range(capacity+1):
        if j == lengths[0]:
            dp[0][j] = 1

    for i in range(n):
        for j in range(1, capacity+1):
            p1 = dp[i-1][j]
            p2 = float('-inf')
            if j >= lengths[i]:
                p2 = 1 + dp[i][j-lengths[i]]
            dp[i][j] = max(p1, p2)
    return dp[n-1][capacity]

def main():
    # mrc = mrc
    # using plain recursion
    print (mrc([2, 3, 5], 5)) #2
    print (mrc([2, 3], 7)) #3
    print (mrc([3, 5, 7], 13)) #3
    # using top-down DP
    print (mrc_dp([2, 3, 5], 5)) #2
    print (mrc_dp([2, 3], 7)) #3
    print (mrc_dp([3, 5, 7], 13)) #3
    # using bottom-up DP
    print (mrc_btmup([2, 3, 5], 5)) #2
    print (mrc_btmup([2, 3], 7)) #3
    print (mrc_btmup([3, 5, 7], 13)) #3

main()
