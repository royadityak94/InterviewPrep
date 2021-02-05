# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

# O(2^n) time | O(n) space
def can_partition(nums):
    sum_ = sum(nums)
    if sum_ % 2 != 0:
        return False
    return can_partition_recursive(nums, sum_//2, 0)

def can_partition_recursive(nums, desired_sum, currentIdx):
    if not desired_sum:
        return True
    if currentIdx == len(nums):
        return False

    if nums[currentIdx] <= desired_sum:
        if can_partition_recursive(nums, desired_sum-nums[currentIdx], currentIdx+1):
            return True
    return can_partition_recursive(nums, desired_sum, currentIdx+1)

# O(ns) time | O(ns) space
def can_partition_td(nums):
    sum_ = sum(nums)
    if sum_ % 2 != 0:
        return False
    dp = [[-1 for _ in range(sum_+1)] for _ in range(len(nums))]
    return True if can_partition_td_recursive(dp, nums, sum_//2, 0)== 1 else False

def can_partition_td_recursive(dp, nums, desired_sum, currentIdx):
    if not desired_sum:
        return True
    if currentIdx == len(nums):
        return False

    if dp[currentIdx][desired_sum] == -1:
        if nums[currentIdx] <= desired_sum:
            if can_partition_td_recursive(dp, nums, desired_sum-nums[currentIdx], currentIdx+1):
                dp[currentIdx][desired_sum] = 1
                return 1
        dp[currentIdx][desired_sum] = can_partition_td_recursive(dp, nums, desired_sum, currentIdx+1)
    return dp[currentIdx][desired_sum]

# O(ns) time | O(ns) space
def can_partition_dp_bottomup(nums):
    s = sum(nums)
    n = len(nums)
    if s % 2 != 0:
        return False
    s = s//2
    dp = [[False for _ in range(s+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    for j in range(s+1):
        dp[0][j] = (j == nums[0])

    for i in range(1, n):
        for j in range(1, s+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
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
