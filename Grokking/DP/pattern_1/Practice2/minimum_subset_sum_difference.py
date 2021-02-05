# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

def can_partition(nums):
    return can_partition_recursive(nums, 0, 0, 0)

def can_partition_recursive(nums, s1, s2, currentIdx):
    if currentIdx == len(nums):
        return abs(s1-s2)

    c1 = can_partition_recursive(nums, s1-nums[currentIdx], s2, currentIdx+1)
    c2 = can_partition_recursive(nums, s1, s2-nums[currentIdx], currentIdx+1)
    return min(c1, c2)

def can_partition_td(nums):
    n, s = len(nums), sum(nums)
    dp = [[-1 for _ in range(s+1)] for _ in range(n)]
    return can_partition_td_recursive(dp, nums, 0, 0, 0)

def can_partition_td_recursive(dp, nums, s1, s2, currentIdx):
    if currentIdx == len(nums):
        return abs(s1-s2)

    if dp[currentIdx][s1] == -1:
        c1 = can_partition_td_recursive(dp, nums, s1-nums[currentIdx], s2, currentIdx+1)
        c2 = can_partition_td_recursive(dp, nums, s1, s2-nums[currentIdx], currentIdx+1)
        dp[currentIdx][s1] = min(c1, c2)
    return dp[currentIdx][s1]

def can_partition_btmup(nums):
    n, s = len(nums), sum(nums)
    S = s//2
    dp = [[False for _ in range(S+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    for j in range(S+1):
        dp[0][j] = (nums[0] == j)

    for i in range(1, n):
        for j in range(1, S+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]

    val1, val2 = None, None
    for j in range(S+1)[::-1]:
        if dp[n-1][j]:
            val1 = j
            break
    val2 = s-val1
    return abs(val1 - val2)

def main():
    # Using plain recursion
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))

    # Using top-down recursion
    print("Can partition: " + str(can_partition_td([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition_td([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition_td([1, 3, 100, 4])))

    # Using bottom-up recursion
    print("Can partition: " + str(can_partition_btmup([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition_btmup([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition_btmup([1, 3, 100, 4])))

main()
