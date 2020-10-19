# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit out of the items in the knapsack

def solve_knapsack(profits, weights, capacity):
    # Time Complexity: (O(2^N) + O(2^N) - 1), Space Complexity: O(N)
    return solve_knapsack_recursive(profits, weights, capacity, 0)

def solve_knapsack_recursive(profits, weights, capacity, currentIndex):
    if capacity <= 0 or currentIndex > len(profits) - 1:
        return 0

    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + \
            solve_knapsack_recursive(profits, weights, capacity-weights[currentIndex], currentIndex+1)
    profit2 = solve_knapsack_recursive(profits, weights, capacity, currentIndex+1)
    return max(profit1, profit2)

def solve_knapsack_td(profits, weights, capacity):
    # Time Complexity: O(NC), Space Complexity: O(N + NC)
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
    return solve_knapsack_td_recursive(dp, profits, weights, capacity, 0)

def solve_knapsack_td_recursive(dp, profits, weights, capacity, currentIndex):
    if capacity <= 0 or currentIndex > (len(profits) - 1):
        return 0

    if not (dp[currentIndex][capacity]+1):
        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + \
                solve_knapsack_recursive(profits, weights, capacity-weights[currentIndex], currentIndex+1)
        profit2 = solve_knapsack_recursive(profits, weights, capacity, currentIndex+1)
        dp[currentIndex][capacity] = max(profit1, profit2)

    return dp[currentIndex][capacity]

def solve_knapsack_btmup(profits, weights, capacity):
    # Time Complexity = Space Complexity = O(N*C), N=len(profits), C=max(capacity)
    if (not len(profits)) or (not capacity):
        return 0

    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]

    # Populating profit=0
    for row in range(len(profits)):
        dp[row][0] = 0
    # Populating 0th column, with profit[0] provided col <= weights[0]
    for col in range(capacity+1):
        if weights[0] <= col:
            dp[0][col] = profits[0]

    # Populating other subsets of weights, capacity
    for row in range(1, len(profits)):
        for col in range(1, capacity+1):
            profit1 = 0
            if weights[row] <= col:
                profit1 = profits[row] + dp[row-1][col-weights[row]]
            profit2 = dp[row-1][col]
            dp[row][col] = max(profit1, profit2)
    return dp[-1][-1]

def main():
    # Using Recursion
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # Using top-down DP
    print(solve_knapsack_td([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_td([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # # Using bottom-up DP
    print(solve_knapsack_btmup([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_btmup([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()
