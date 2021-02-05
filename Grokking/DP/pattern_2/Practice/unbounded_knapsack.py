# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Assume: infinite supply of item quantities.

# O(2^(n+c)) time | O(n+c) space
def maximum_capacity(profits, weights, capacity):
    return maximum_capacity_recursive(profits, weights, capacity, 0)

def maximum_capacity_recursive(profits, weights, capacity, currentIndex):
    if currentIndex == len(profits):
        return 0
    with_current = 0
    if weights[currentIndex] <= capacity:
        with_current = profits[currentIndex] + maximum_capacity_recursive(profits, weights, capacity-weights[currentIndex], currentIndex)
    without_current = maximum_capacity_recursive(profits, weights, capacity, currentIndex+1)
    return max(with_current, without_current)

# O(n*c + n) time | O(n^2) space
def maximum_capacity_dp(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
    return maximum_capacity_dp_recursive(dp, profits, weights, capacity, 0)

def maximum_capacity_dp_recursive(dp, profits, weights, capacity, currentIndex):
    if currentIndex == len(profits):
        return 0
    if dp[currentIndex][capacity] == -1:
        with_current = 0
        if weights[currentIndex] <= capacity:
            with_current = profits[currentIndex] + maximum_capacity_dp_recursive(dp, profits, weights, capacity-weights[currentIndex], currentIndex)
        without_current = maximum_capacity_dp_recursive(dp,profits, weights, capacity, currentIndex+1)
        dp[currentIndex][capacity] = max(with_current, without_current)
    return dp[currentIndex][capacity]

# O(nc) time | O(nc) space
def maximum_capacity_bottom_up(profits, weights, capacity):
    n = len(profits)
    dp = [[-1 for _ in range(capacity+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0
    for j in range(1+capacity):
        if j == weights[0]:
            dp[0][j] = profits[0]

    for i in range(1, n):
        for j in range(1, capacity+1):
            p1 = dp[i-1][j]
            p2 = 0
            if j >= weights[i]:
                p2 = profits[i] + dp[i][j-weights[i]]
            dp[i][j] = max(p1, p2)
    return dp[n-1][capacity]



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
