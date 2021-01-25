# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).
# [4,2,3,6,10,1,12] -> len({2,3,6,10,12}) = 5
# [-4,10,3,7,15] -> len([-4, 3, 7, 15]) = 4
# O(2^n) time | O(n) space

# O(2^n) time | O(n) space
def lcs(nums):
    return lcs_recursive(nums, 0, -1)

def lcs_recursive(nums, currentIdx, previousIdx):
    if currentIdx == len(nums):
        return 0

    with_current = 0
    if previousIdx == -1 or nums[currentIdx] > nums[previousIdx]:
        with_current = 1 + lcs_recursive(nums, currentIdx+1, currentIdx)
    without_current = lcs_recursive(nums, currentIdx+1, previousIdx)
    return max(with_current, without_current)

# O(n^2) time | O(n^2 + n ~ n^2) space
def lcs_td(nums):
    dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
    return lcs_td_recursive(dp, nums, 0, -1)

def lcs_td_recursive(dp, nums, currentIdx, previousIdx):
    if currentIdx == len(nums):
        return 0

    if dp[currentIdx][previousIdx] == -1:
        with_current = 0
        if previousIdx == -1 or nums[currentIdx] > nums[previousIdx]:
            with_current = 1 + lcs_td_recursive(dp, nums, currentIdx+1, currentIdx)
        without_current = lcs_td_recursive(dp, nums, currentIdx+1, previousIdx)
        dp[currentIdx][previousIdx] = max(with_current, without_current)
    return dp[currentIdx][previousIdx]

# O(n^2) time | O(n) space
def lcs_btmup(nums):
    dp = [1 for _ in range(len(nums))]
    dp[0] = 1
    maxLength = float('-inf')
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = 1 + dp[j]
            maxLength = max(maxLength, dp[i])
    return maxLength


if __name__ == '__main__':
    # Using recursion
    print (lcs([4,2,3,6,10,1,12]))
    print (lcs([-4,10,3,7,15]))
    print ('---------------')
    # Using top-down DP
    print (lcs_td([4,2,3,6,10,1,12]))
    print (lcs_td([-4,10,3,7,15]))
    print ('---------------')
    # Using bottom-up DP
    print (lcs_btmup([4,2,3,6,10,1,12]))
    print (lcs_btmup([-4,10,3,7,15]))
