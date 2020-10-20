# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’.

def solve_knapsack(profits, weights, capacity):
    if (not profits) or (not weights) or (not len(profits) == len(weights)) or (not capacity):
        return 0
    return solve_knapsack_recursive(profits, weights, capacity, 0)

def solve_knapsack_recursive(profits, weights, capacity, currentIndex):
    if capacity == 0:
        return 0
    if currentIndex > len(weights)-1:
        return 0

    with_current = 0
    if weights[currentIndex] <= capacity:
        with_current = profits[currentIndex] + \
            solve_knapsack_recursive(profits, weights, capacity-weights[currentIndex], currentIndex+1)
    without_current = solve_knapsack_recursive(profits, weights, capacity, currentIndex+1)
    return max(with_current, without_current)

def solve_knapsack_dp(profits, weights, capacity):
    if (not profits) or (not weights) or (not len(profits) == len(weights)) or (not capacity):
        return 0
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(weights))]
    return solve_knapsack_dp_recursive(dp, profits, weights, capacity, 0)

def solve_knapsack_dp_recursive(dp, profits, weights, capacity, currentIndex):
    if capacity == 0:
        return 0
    if currentIndex > len(weights)-1:
        return 0

    if not (dp[currentIndex][capacity]+1):
        with_current = 0
        if weights[currentIndex] <= capacity:
            with_current = profits[currentIndex] + \
                solve_knapsack_dp_recursive(dp, profits, weights, capacity-weights[currentIndex], currentIndex+1)
        without_current = solve_knapsack_dp_recursive(dp, profits, weights, capacity, currentIndex+1)
        dp[currentIndex][capacity] = max(with_current, without_current)
    return dp[currentIndex][capacity]

def solve_knapsack_btup_dp(profits, weights, capacity):
    if (not profits) or (not weights) or (not len(profits) == len(weights)) or (not capacity):
        return 0
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(weights))]

    # Populating column=0
    for row in range(len(profits)):
        dp[row][0] = 0

    # Populating row=0, i.e. col>= weights[0] gets profits[0]
    for col in range(1, capacity+1):
        dp[0][col] = profits[0] if col >= weights[0] else 0

    # Populating other subsets
    for row in range(1, len(profits)):
        for col in range(1, capacity+1):
            with_current, without_current = 0, 0
            if col >= weights[row]:
                with_current = profits[row] + dp[row-1][col - weights[row]]
            without_current = dp[row-1][col]
            dp[row][col] = max(with_current, without_current)
    return dp[-1][-1]

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # Using top-down dynamic programming
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # # # Using bottom-up dynamic programming
    print(solve_knapsack_btup_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_btup_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()
