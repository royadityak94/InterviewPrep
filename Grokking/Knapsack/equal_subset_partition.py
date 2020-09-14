# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal
# I/p: {1, 2, 3, 4}; O/p: {1, 4} & {2, 3}
# I/p: {1, 1, 3, 4, 7}; O/p: {1, 3, 4} & {1, 7}
# I/p: {2, 3, 4, 6}; O/p: None

def can_partition(num):
    s = sum(num)
    if s % 2 != 0:
        return False
    return can_partition_recursive(num, s/2, 0)

def can_partition_recursive(num, sum, currentIndex):
    # Time Complexity: O(2^N), Space Complexity: O(N)
    if sum == 0:
        return True
    n = len(num)
    if n == 0 or currentIndex >= n:
        return False

    # recursive call after choosing the number at the `currentIndex`
    if num[currentIndex] <= sum:
        if can_partition_recursive(num, sum-num[currentIndex], currentIndex+1):
            return True
    # recursive call after excluding the number at the 'currentIndex'
    return can_partition_recursive(num, sum, currentIndex+1)

def can_partition_dp(num):
    # Time Complexity = Space Complexity = O(N∗S), N=len(num), S = sum(num)
    s = sum(num)
    if s%2 != 0:
        return False
    dp = [[-1 for _ in range(s+1)] for _ in num]
    return True if can_partition_dp_recursive(dp, num, int(s/2), 0) == 1 else False

def can_partition_dp_recursive(dp, num, sum, currentIndex):
    if sum == 0:
        return True
    n = len(num)
    if n == 0 or currentIndex >= n:
        return False

    if dp[currentIndex][sum] == -1:
        if num[currentIndex] <= sum:
            # recursive call after choosing the number at the `currentIndex`
            if can_partition_dp_recursive(dp, num, sum-num[currentIndex], currentIndex+1):
                dp[currentIndex][sum] = 1
                return 1

        # recursive call after excluding the number at the 'currentIndex'
        dp[currentIndex][sum] = can_partition_dp_recursive(dp, num, sum, currentIndex+1)
    return dp[currentIndex][sum]

def can_partition_dp_bottomup(num):
    # Time Complexity = Space Complexity = O(N*S)
    n, s = len(num), sum(num)
    if s % 2 != 0:
        return False
    s = int(s/2)
    dp = [[False for _ in range(s+1)] for _ in num]

    # Populate s=0 with 'true'
    for i in range(n):
        dp[i][0] = True

    # with only one number, it's true only when that number is equal to sum
    for i in range(n):
        dp[0][i] = num[0] == i

    # Process subset for all sums
    for i in range(1, n):
        for j in range(1, s+1):
            if dp[i-1][j]:
                dp[i][j] = True
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]

    return dp[-1][-1]

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))

    print("Can partition (using top-down dp): " + str(can_partition_dp([1, 2, 3, 4])))
    print("Can partition (using top-down dp): " + str(can_partition_dp([1, 1, 3, 4, 7])))
    print("Can partition (using top-down dp): " + str(can_partition_dp([2, 3, 4, 6])))

    print("Can partition (using bottom-up dp): " + str(can_partition_dp_bottomup([1, 2, 3, 4])))
    print("Can partition (using bottom-up dp): " + str(can_partition_dp_bottomup([1, 1, 3, 4, 7])))
    print("Can partition (using bottom-up dp): " + str(can_partition_dp_bottomup([2, 3, 4, 6])))

main()
