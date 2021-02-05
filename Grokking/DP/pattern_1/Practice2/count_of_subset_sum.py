# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

def count_subsets(nums, S):
    return count_subsets_recursive(nums, S, 0)

def count_subsets_recursive(nums, desired_sum, currentIdx):
    if not desired_sum:
        return 1
    if currentIdx == len(nums):
        return 0

    with_current = 0
    if nums[currentIdx] <= desired_sum:
        with_current = count_subsets_recursive(nums, desired_sum-nums[currentIdx], currentIdx+1)
    without_current = count_subsets_recursive(nums, desired_sum, currentIdx+1)
    return with_current+without_current

def count_subsets_td(nums, S):
    dp = [[-1 for _ in range(S+1)] for _ in range(len(nums))]
    return count_subsets_td_recursive(dp, nums, S, 0)

def count_subsets_td_recursive(dp, nums, desired_sum, currentIdx):
    if not desired_sum:
        return 1
    if currentIdx == len(nums):
        return 0
    if dp[currentIdx][desired_sum] == -1:
        with_current = 0
        if nums[currentIdx] <= desired_sum:
            with_current = count_subsets_td_recursive(dp, nums, desired_sum-nums[currentIdx], currentIdx+1)
        without_current = count_subsets_td_recursive(dp, nums, desired_sum, currentIdx+1)
        dp[currentIdx][desired_sum] = with_current+without_current
    return dp[currentIdx][desired_sum]

def count_subsets_btmup(nums, S):
    dp = [[0 for _ in range(S+1)] for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][0] = 1
        
    for j in range(S+1):
        if j == nums[0]:
            dp[0][j] = 1

    for i in range(1, len(nums)):
        for j in range(1, S+1):
            dp[i][j] = dp[i-1][j]
            if j >= nums[i]:
                dp[i][j] += dp[i-1][j-nums[i]]
    return dp[len(nums)-1][S]


def main():
    # Using plain Recursion
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
    # Using top-down Recursion
    print("Total number of subsets (Top-Down): " + str(count_subsets_td([1, 1, 2, 3], 4)))
    print("Total number of subsets (Top-Down): " + str(count_subsets_td([1, 2, 7, 1, 5], 9)))
    # Using bottom-up Recursion
    print("Total number of subsets (Bottom-Up): " + str(count_subsets_btmup([1, 1, 2, 3], 4)))
    print("Total number of subsets (Bottom-Up): " + str(count_subsets_btmup([1, 2, 7, 1, 5], 9)))

main()
