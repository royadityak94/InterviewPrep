# Coin Change problem : Similar to Count of Subset Sum
# Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.

def count_subset_coins(denominations, capacity):
    return count_subset_coins_recursive(denominations, capacity, 0)

def count_subset_coins_recursive(denominations, capacity, currentIdx):
    if currentIdx == len(denominations):
        return 0
    with_current = 0
    if denominations[currentIdx] <= capacity:
        with_current = denominations[currentIdx] + \
        count_subset_coins_recursive(denominations, capacity-denominations[currentIdx], currentIdx)
    without_current = count_subset_coins_recursive(denominations, capacity, currentIdx+1)
    return max(with_current, without_current)

def count_subset_coins_td(denominations, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(denominations))]
    return count_subset_coins_td_recursive(dp, denominations, capacity, 0)

def count_subset_coins_td_recursive(dp, denominations, capacity, currentIdx):
    if currentIdx == len(denominations):
        return 0
    if dp[currentIdx][capacity] == -1:
        with_current = 0
        if denominations[currentIdx] <= capacity:
            with_current = denominations[currentIdx] + \
            count_subset_coins_td_recursive(dp, denominations, capacity-denominations[currentIdx], currentIdx)
        without_current = count_subset_coins_td_recursive(dp, denominations, capacity, currentIdx+1)
        dp[currentIdx][capacity] = max(with_current, without_current)
    return dp[currentIdx][capacity]

def count_subset_coins_btm_up(denominations, capacity):
    n = len(denominations)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for j in range(1, capacity+1):
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j >= denominations[i]:
                dp[i][j] += dp[i][j-denominations[i]]
    return dp[n-1][capacity]

def main():
    # usign simple recursion
    print (count_subset_coins([1, 2, 3], 5))
    # using top-down recursion
    print (count_subset_coins_td([1, 2, 3], 5))
    # using bottom-up recursion
    print(count_subset_coins_btm_up([1, 2, 3], 5))
    print(count_subset_coins_btm_up([2, 4], 7))

main()
