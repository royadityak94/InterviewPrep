# Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

def exists_subset(nums, s):
    return exists_subset_recursive(nums, s, 0)

def exists_subset_recursive(nums, s, currentIdx):
    if not s:
        return True
    if currentIdx == len(nums):
        return False
    if nums[currentIdx] <= s:
        if exists_subset_recursive(nums, s-nums[currentIdx], currentIdx+1):
            return True
    return  exists_subset_recursive(nums, s, currentIdx+1)


def exists_subset_td(nums, s):
    dp = [[-1 for _ in range(s+1)] for _ in range(len(nums))]
    return True if exists_subset_td_recursive(dp, nums, s, 0) == 1 else False

def exists_subset_td_recursive(dp, nums, s, currentIdx):
    if not s:
        return True
    if currentIdx == len(nums):
        return False
    if dp[currentIdx][s] == -1:
        if nums[currentIdx] <= s:
            if exists_subset_td_recursive(dp, nums, s-nums[currentIdx], currentIdx+1):
                dp[currentIdx][s] = 1
                return 1
        dp[currentIdx][s] = exists_subset_td_recursive(dp, nums, s, currentIdx+1)
    return dp[currentIdx][s]

def exists_subset_bottom_up(nums, s):
    n = len(nums)
    dp = [[False for _ in range(s+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    for j in range(s+1):
        if j == nums[0]:
            dp[0][j] = True

    for i in range(1, n):
        for j in range(1, s+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
    return dp[n-1][s]

def main():
    # plain-recursion
    print (exists_subset([1, 2, 3, 7], 6))
    print (exists_subset([1, 2, 7, 1, 5], 10))
    print (exists_subset([1, 3, 4, 8], 6))

    # top-down DP
    print (exists_subset_td([1, 2, 3, 7], 6))
    print (exists_subset_td([1, 2, 7, 1, 5], 10))
    print (exists_subset_td([1, 3, 4, 8], 6))

    for _ in range(50): print('-', end='')
    print()
    # Bottom-up DP
    print (exists_subset_bottom_up([1, 2, 3, 7], 6))
    print (exists_subset_bottom_up([1, 2, 7, 1, 5], 10))
    print (exists_subset_bottom_up([1, 3, 4, 8], 6))


main()
