# Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

def find_target_subsets(nums, s):
    S = sum(nums)
    if S < s or (S + s) % 2 != 0:
        return 0
    return find_target_subsets_recursive(nums, (S+s)//2, 0)

def find_target_subsets_recursive(nums, s, currentIdx):
    if not s:
        return 1
    if currentIdx == len(nums):
        return 0
    with_current = 0
    if nums[currentIdx] <= s:
        with_current = find_target_subsets_recursive(nums, s-nums[currentIdx], currentIdx+1)
    without_current = find_target_subsets_recursive(nums, s, currentIdx+1)
    return with_current + without_current

def find_target_subsets_td(nums, s):
    S = sum(nums)
    if S < s or (S + s) % 2 != 0:
        return 0
    desired_sum = (S + s)//2
    dp = [[-1 for _ in range(desired_sum+1)] for _ in range(len(nums))]
    return find_target_subsets_td_recursive(dp, nums, (S+s)//2, 0)

def find_target_subsets_td_recursive(dp, nums, s, currentIdx):
    if not s:
        return 1
    if currentIdx == len(nums):
        return 0
    if dp[currentIdx][s] == -1:
        with_current = 0
        if nums[currentIdx] <= s:
            with_current = find_target_subsets_td_recursive(dp, nums, s-nums[currentIdx], currentIdx+1)
        without_current = find_target_subsets_td_recursive(dp, nums, s, currentIdx+1)
        dp[currentIdx][s] = with_current + without_current
    return dp[currentIdx][s]

def find_target_subsets_btmup(nums, s):
    S = sum(nums)
    if S < s or (S + s) % 2 != 0:
        return 0
    desired_sum = (S + s)//2
    dp = [[0 for _ in range(desired_sum+1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = 1
    for j in range(1, desired_sum+1):
        if j == nums[0]:
            dp[0][j] = 1

    for i in range(1, len(nums)):
        for j in range(1, desired_sum+1):
            dp[i][j] = dp[i-1][j]
            if j >= nums[i]:
                dp[i][j] += dp[i-1][j-nums[i]]

    return dp[len(nums)-1][desired_sum]

def main():
    # Using plain recursion
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))
    # Using top-down recursion
    print("Total ways (Top-Down): " + str(find_target_subsets_td([1, 1, 2, 3], 1)))
    print("Total ways (Top-Down): " + str(find_target_subsets_td([1, 2, 7, 1], 9)))
    # Using bottom-up recursion
    print("Total ways (Bottom-Up): " + str(find_target_subsets_btmup([1, 1, 2, 3], 1)))
    print("Total ways (Bottom-Up): " + str(find_target_subsets_btmup([1, 2, 7, 1], 9)))

main()
