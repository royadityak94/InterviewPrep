# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

def can_partition(num):
    s = sum(num)
    if s % 2 != 0:
        return False
    return can_partition_recursive(num, s//2, 0)

def can_partition_recursive(num, sum, currentIndex):
    if sum == 0:
        return True
    if len(num) == 0 or currentIndex >= len(num):
        return False

    if num[currentIndex] <= sum:
        if can_partition_recursive(num, sum-num[currentIndex], currentIndex+1):
            return True
    return can_partition_recursive(num, sum, currentIndex+1)

def can_partition_td(num):
    # Time Complexity: O(N*S), Space Complexity: O(N*S); N-> Total Numbers, S-> Sum of all numbers
    s = sum(num)
    if s % 2 != 0:
        return False
    s = s//2
    dp = [[-1 for _ in range(s+1)] for _ in num]
    return True if can_partition_td_recursive(dp, num, s, 0) == 1 else False

def can_partition_td_recursive(dp, num, sum, currentIndex):
    if sum == 0:
        return 1
    if len(num) == 0 and currentIndex >= len(num):
        return 0

    if num[currentIndex] <= sum:
        if can_partition_td_recursive(dp, num, sum-num[currentIndex], currentIndex+1):
            dp[currentIndex][sum] = 1
            return 1
        dp[currentIndex][sum] = can_partition_td_recursive(dp, num, sum, currentIndex+1)
    return dp[currentIndex][sum]

def can_partition_dp_bottomup(num):
    # Time Complexity: O(N*S), Space Complexity: O(N*S); N-> Total Numbers, S-> Sum of all numbers
    if len(num) == 0:
        return False
    n, s = len(num), sum(num)
    if s % 2 != 0:
        return False
    s = s//2
    dp = [[False for _ in range(s+1)] for _ in num]

    # Populating column - 0, i.e, we can always partition when capacity = 0
    for r in range(n):
        dp[r][0] = True

    # Partitioning row - 0, i.e, we can always partition depending on whether weight[0] < capacity column
    for c in range(s+1):
        dp[0][c] = num[0] == c

    # Creating all other subsets
    for r in range(1, n):
        for c in range(1, s+1):
            if dp[r-1][c]:
                dp[r][c] = dp[r-1][c]
            elif c >= num[r]:
                dp[r][c] = dp[r-1][c-num[r]]

    return dp[n-1][s]

def main():
    # Using simple recursion
    print (can_partition([1, 2, 3, 4]))
    print (can_partition([1, 1, 3, 4, 7]))
    print (can_partition([2, 3, 4, 6]))

    # Using top-down recursion
    print (can_partition_td([1, 2, 3, 4]))
    print (can_partition_td([1, 1, 3, 4, 7]))
    print (can_partition_td([2, 3, 4, 6]))

    # Using bottom-up recursion
    print (can_partition_dp_bottomup([1, 2, 3, 4]))
    print (can_partition_dp_bottomup([1, 1, 3, 4, 7]))
    print (can_partition_dp_bottomup([2, 3, 4, 6]))

main()
