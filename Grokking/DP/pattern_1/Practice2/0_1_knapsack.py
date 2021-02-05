# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’.

def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_recursive(profits, weights, capacity, 0)

def solve_knapsack_recursive(profits, weights, capacity, currentIdx):
    if currentIdx == len(profits) or (not capacity):
        return 0
    with_current = 0
    if weights[currentIdx] <= capacity:
        with_current = profits[currentIdx] + \
        solve_knapsack_recursive(profits, weights, capacity-weights[currentIdx], currentIdx+1)
    without_current = solve_knapsack_recursive(profits, weights, capacity, currentIdx+1)
    return max(with_current, without_current)

def solve_knapsack_td(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
    return solve_knapsack_td_recursive(dp, profits, weights, capacity, 0)

def solve_knapsack_td_recursive(dp, profits, weights, capacity, currentIdx):
    if currentIdx == len(profits) or (not capacity):
        return 0
    if dp[currentIdx][capacity] == -1:
        with_current = 0
        if weights[currentIdx] <= capacity:
            with_current = profits[currentIdx] + \
            solve_knapsack_td_recursive(dp, profits, weights, capacity-weights[currentIdx], currentIdx+1)
        without_current = solve_knapsack_td_recursive(dp, profits, weights, capacity, currentIdx+1)
        dp[currentIdx][capacity] = max(with_current, without_current)
    return dp[currentIdx][capacity]

def solve_knapsack_btup_dp(profits, weights, capacity):
    n = len(profits)
    dp =  [[0 for _ in range(capacity+1)] for _ in range(n)]
    for j in range(1, capacity+1):
        if j >= weights[0]:
            dp[0][j] = profits[0]

    for i in range(1, n):
        for j in range(1, capacity+1):
            profit1 = 0
            if weights[i] <= j:
                profit1 = profits[i] + dp[i-1][j-weights[i]]
            dp[i][j] = max(dp[i-1][j], profit1)
    return dp[n-1][capacity]

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # Using top-down dynamic programming
    print(solve_knapsack_td([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_td([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # # Using bottom-up dynamic programming
    print(solve_knapsack_btup_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_btup_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()
