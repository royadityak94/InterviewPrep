# Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the minimum number of coins needed to make up that amount.

def mctma(denominations, capacity):
    return mctma_recursive(denominations, capacity, 0)

def mctma_recursive(denominations, capacity, currentIdx):
    if capacity == 0:
        return 0
    if currentIdx == len(denominations):
        return float('inf')
    with_current = float('inf')
    if denominations[currentIdx] <= capacity:
        with_current = 1 + mctma_recursive(denominations, capacity-denominations[currentIdx], currentIdx)
    without_current = mctma_recursive(denominations, capacity, currentIdx+1)
    return min(with_current, without_current)

def mctma_td(denominations, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(denominations))]
    return mctma_td_recursive(dp, denominations, capacity, 0)

def mctma_td_recursive(dp, denominations, capacity, currentIdx):
    if capacity == 0:
        return 0
    if currentIdx == len(denominations):
        return float('inf')
    if dp[currentIdx][capacity] == -1:
        with_current = float('inf')
        if denominations[currentIdx] <= capacity:
            with_current = 1 + mctma_td_recursive(dp, denominations, capacity-denominations[currentIdx], currentIdx)
        without_current = mctma_td_recursive(dp, denominations, capacity, currentIdx+1)
        dp[currentIdx][capacity] = min(with_current, without_current)
    return dp[currentIdx][capacity]

def mctma_btmup(denominations, capacity):
    n = len(denominations)
    dp = [[float('inf') for _ in range(capacity+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 0
    for j in range(capacity+1):
        if j == denominations[0]:
            dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, capacity+1):
            p1 = dp[i-1][j]
            p2 = float('inf')
            if j >= denominations[i]:
                p2 = 1 + dp[i][j-denominations[i]]
            dp[i][j] = min(p1, p2)
    return dp[n-1][capacity]


def main():
    # using simple recursion
    print(mctma([1, 2, 3], 5)) #2 # mctma = mctma !!
    print(mctma([1, 2, 3], 11)) #4
    # using top-down DP
    print(mctma_td([1, 2, 3], 5))
    print(mctma_td([1, 2, 3], 11)) #4
    # using bottom-up DP
    print(mctma_btmup([1, 2, 3], 5))
    print(mctma_btmup([1, 2, 3], 11)) #4

main()
