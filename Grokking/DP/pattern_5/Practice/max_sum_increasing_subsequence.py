# Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

# O(2^n) time | O(n) space
def msis(nums):
    return msis_recursive(nums, 0, -1)

def msis_recursive(nums, currentIdx, previousIdx):
    if currentIdx == len(nums):
        return 0

    with_current = 0
    if previousIdx == -1 or nums[currentIdx] > nums[previousIdx]:
        with_current = nums[currentIdx] + msis_recursive(nums, currentIdx+1, currentIdx)
    without_current = msis_recursive(nums, currentIdx+1, previousIdx)
    return max(with_current, without_current)

# O(n*n) time | O(n*n + n ~ n) space
def msis_td(nums):
    dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
    return msis_td_recursive(dp, nums, 0, -1)

def msis_td_recursive(dp, nums, currentIdx, previousIdx):
    if currentIdx == len(nums):
        return 0

    if dp[currentIdx][previousIdx] == -1:
        with_current = 0
        if previousIdx == -1 or nums[currentIdx] > nums[previousIdx]:
            with_current = nums[currentIdx] + msis_td_recursive(dp, nums, currentIdx+1, currentIdx)
        without_current = msis_td_recursive(dp, nums, currentIdx+1, previousIdx)
        dp[currentIdx][previousIdx] = max(with_current, without_current)
    return dp[currentIdx][previousIdx]

def msis_btmup(nums):
    dp = [0 for _ in range(len(nums))]
    maxSum = float('-inf')
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = nums[i] + dp[j]
            maxSum = max(maxSum, dp[i])
    return maxSum

if __name__ == '__main__':
    # using simple recursion
    print (msis([4,1,2,6,10,1,12]))
    print (msis([-4,10,3,7,15]))
    # using top-down DP
    print (msis_td([4,1,2,6,10,1,12]))
    print (msis_td([-4,10,3,7,15]))
    # using bottom-up DP
    print (msis_btmup([4,1,2,6,10,1,12]))
    print (msis_btmup([-4,10,3,7,15]))
