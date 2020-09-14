# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit and that their cumulative weight is not more than a given number ‘C’.

def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weights, capacity, currentIndex):
    # Time Complexity: O(2^N), Space Complexity: O(N)
    if capacity <= 0 or not currentIndex < len(profits):
        return 0
    with_current = without_current = 0
    if weights[currentIndex] <= capacity:
        with_current = profits[currentIndex] + knapsack_recursive(profits,
            weights, capacity - weights[currentIndex], currentIndex + 1)

    without_current = knapsack_recursive(profits, weights, capacity, currentIndex+1)
    return max(with_current, without_current)

def solve_knapsack_dp(profits, weights, capacity):
    # Time Complexity: O(NC), N: Subproblems, C: knapsack capacity; O(N)
    # Space Complexity: O(NC) + O(N); O(N): recursion call-stack
    dp = [[None for _ in range(capacity+1)] for _ in profits]
    return solve_knapsack_dp_topdown(dp, profits, weights, capacity, 0)

def solve_knapsack_dp_topdown(dp, profits, weights, capacity, currentIndex):
    if capacity <= 0 or not currentIndex < len(profits):
        return 0

    if dp[currentIndex][capacity]:
        return dp[currentIndex][capacity]

    without_current = with_current = 0

    if weights[currentIndex] <= capacity:
        with_current = profits[currentIndex] + solve_knapsack_dp_topdown(dp, profits, weights, capacity - weights[currentIndex], currentIndex+1)

    without_current = solve_knapsack_dp_topdown(dp, profits, weights, capacity, currentIndex+1)
    dp[currentIndex][capacity] = max(with_current, without_current)
    return dp[currentIndex][capacity]

def solve_knapsack_btup_dp(profits, weights, capacity):
    # Time Complexity = Space Complexity: O(NC)
    if capacity <= 0:
        return 0
    dp = [[0 for _ in range(capacity+1)] for _ in profits]

    # Populating '0' capacity with '0' profit (Column - 0)
    for r in range(len(profits)):
        dp[r][0] = 0

    # If we have only 1 weight we will take it if it's not more than the capacity
    for c in range(1, capacity+1):
        if weights[0] <= capacity:
            dp[0][c] = profits[0]

    for r in range(1, len(profits)):
        for c in range(1, capacity+1):
            with_current = without_current = 0
            if weights[r] <= c:
                with_current = profits[r] + dp[r-1][c-weights[r]]
            without_current = dp[r-1][c]
            dp[r][c] = max(without_current, with_current)

    print (">>>>>>>>>>>>>>>>>>>>>>>")
    print_selected_elements(dp, weights, profits, capacity)
    print (">>>>>>>>>>>>>>>>>>>>>>>")
    return dp[-1][-1]

def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[n-1][capacity]
    for i in range(n-1, 0, -1):
        if totalProfit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # Using top-down dynamic programming
    # print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))
    # print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # # Using bottom-up dynamic programming
    # print(solve_knapsack_btup_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))
    # print(solve_knapsack_btup_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()
