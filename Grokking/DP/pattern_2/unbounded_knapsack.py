# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Assume: infinite supply of item quantities.

def maximum_capacity(profits, weights, capacity):
    if len(profits) != len(weights) or capacity == 0:
        return []
    return maximum_capacity_recursive(profits, weights, capacity, 0)

def maximum_capacity_recursive(profits, weights, capacity, currentIndex):
    # Time Complexity: O(2^(N+C)); Space Complexity: O(2^(N+C))
    if capacity == 0:
        return 0

    if currentIndex >= len(profits):
        return 0

    with_current = without_current = 0
    if weights[currentIndex] <= capacity:
        with_current = profits[currentIndex] + maximum_capacity_recursive(profits, weights, capacity-weights[currentIndex], currentIndex)
    without_current = maximum_capacity_recursive(profits, weights, capacity, currentIndex+1)
    return max(with_current, without_current)

def maximum_capacity_dp(profits, weights, capacity):
    # Time Complexity = Space Complexity = O(N*C)
    if len(profits) != len(weights) or capacity == 0:
        return []
    # Setting up top-down DP
    dp = [[-1 for _ in range(capacity+1)] for _ in profits]
    return maximum_capacity_dp_recursive(dp, profits, weights, capacity, 0)

def maximum_capacity_dp_recursive(dp, profits, weights, capacity, currentIndex):
    if currentIndex >= len(profits):
        return 0

    if dp[currentIndex][capacity] == -1:
        with_current = without_current = 0
        if weights[currentIndex] <= capacity:
            with_current = profits[currentIndex] + maximum_capacity_dp_recursive(dp, profits, weights, capacity-weights[currentIndex], currentIndex)
        without_current = maximum_capacity_dp_recursive(dp, profits, weights, capacity, currentIndex+1)

        dp[currentIndex][capacity] = max(without_current, with_current)

    return dp[currentIndex][capacity]

def maximum_capacity_bottom_up(profits, weights, capacity):
    # Time Complexity = Space Complexity = O(N*C)
    if len(weights) == 0 or len(weights) != len(profits) or capacity <= 0:
        return 0

    dp = [[-1 for _ in range(capacity+1)] for _ in profits]

    # Populating 0th column, profit = 0 when capacity = 0
    for r in range(len(profits)):
        dp[r][0] = 0

    # Populating the first row, i.e. profit = profit[0] if weight[0] <= C
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # Populating the entire table
    for r in range(1, len(profits)):
        for c in range(1, capacity+1):
            with_current = without_current = 0
            if weights[r] <= c:
                with_current = profits[r] + dp[r][c-weights[r]]
            without_current = dp[r-1][c]
            dp[r][c] = max(with_current, without_current)

    return dp[r][capacity]

def solve_knapsack(profits, weights, capacity):
  n = len(profits)
  # base checks
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]

  # populate the capacity=0 columns
  for i in range(n):
    dp[i][0] = 0

  # process all sub-arrays for all capacities
  for i in range(n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      if weights[i] <= c:
        profit1 = profits[i] + dp[i][c - weights[i]]
      if i > 0:
        profit2 = dp[i - 1][c]
      dp[i][c] = profit1 if profit1 > profit2 else profit2

  # maximum profit will be in the bottom-right corner.
  return dp[n - 1][capacity]


def main():

    # Using simple recursion
    print(maximum_capacity([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(maximum_capacity([15, 50, 60, 90], [1, 3, 4, 5], 6))

    # Using top-down DP with memoization
    print(maximum_capacity_dp([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(maximum_capacity_dp([15, 50, 60, 90], [1, 3, 4, 5], 6))

    # Using bottom-up DP
    print(maximum_capacity_bottom_up([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(maximum_capacity_bottom_up([15, 50, 60, 90], [1, 3, 4, 5], 6))



main()
