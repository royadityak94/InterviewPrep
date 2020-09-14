# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’.

def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_recursive(profits, weights, capacity, 0)

def solve_knapsack_recursive(profits, weights, capacity, currentIndex):
    # Time Complexity: (2^N) + (2^N) - 1 ~ O(2^N), Space Complexity: O(N)
    if not len(profits) or currentIndex >= len(profits):
        return 0

    with_current = without_current = 0
    if weights[currentIndex] <= capacity:
        with_current = profits[currentIndex] + solve_knapsack_recursive(profits, weights, capacity-weights[currentIndex], currentIndex + 1)
    without_current = solve_knapsack_recursive(profits, weights, capacity, currentIndex + 1)

    return max(with_current, without_current)

def solve_knapsack_dp(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in weights]
    return solve_knapsack_dp_recursive(dp, profits, weights, capacity, 0)

def solve_knapsack_dp_recursive(dp, profits, weights, capacity, currentIndex):
    # Time Complexity: O(NC), Space Complexity: O(NC)
    if currentIndex >= len(profits):
        return 0

    if dp[currentIndex][capacity] == -1:
        with_current = without_current = 0
        if weights[currentIndex] <= capacity:
            with_current = profits[currentIndex] + solve_knapsack_dp_recursive(dp, profits, weights, capacity-weights[currentIndex], currentIndex + 1)
        without_current = solve_knapsack_dp_recursive(dp, profits, weights, capacity, currentIndex + 1)

        dp[currentIndex][capacity] = max(with_current, without_current)

    return dp[currentIndex][capacity]

def solve_knapsack_btup_dp(profits, weights, capacity):
    # Time Complexity: O(NC), Space Complexity: O(NC)
    if capacity <= 0 or len(profits) <= 0 or len(profits) != len(weights):
        return 0
    dp = [[-1 for _ in range(capacity+1)] for _ in profits]

    # Populating column - 0, i.e. when capacity = 0, then profit = 0
    for r in range(len(profits)):
        dp[r][0] = 0

    # Populating row - 0 with profit [0] provided weight[0] <= capacity
    for c in range(capacity+1):
        if weights[0] <= c   :
            dp[0][c] = profits[0]

    # Building up the entire table
    for r in range(1, len(profits)):
        for c in range(1, capacity+1):
            with_current = without_current = 0
            if weights[r] <= c:
                with_current = profits[r] + dp[r-1][c-weights[r]]
            without_current = dp[r-1][c]
            dp[r][c] = max(with_current, without_current)

    return dp[len(weights)-1][capacity]

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # Using top-down dynamic programming
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # # Using bottom-up dynamic programming
    print(solve_knapsack_btup_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_btup_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()
