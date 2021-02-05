# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).
# [4,2,3,6,10,1,12] -> len({2,3,6,10,12}) = 5
# [-4,10,3,7,15] -> len([-4, 3, 7, 15]) = 4

# O(2^n) time | O(n) space
def longest_increasing_subsequence(nums):
    return longest_increasing_subsequence_recursive(nums, 0, -1)

def longest_increasing_subsequence_recursive(nums, currentIdx, parentIdx):
    if currentIdx == len(nums):
        return 0
    with_current = 0
    if parentIdx == -1 or nums[currentIdx] > nums[parentIdx]:
        with_current = 1 + longest_increasing_subsequence_recursive(nums, currentIdx+1, currentIdx)

    without_current = longest_increasing_subsequence_recursive(nums, currentIdx+1, parentIdx)
    return max(with_current, without_current)

# O(n^2) time | O(n^2) space
def longest_increasing_subsequence_td(nums):
    dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
    return longest_increasing_subsequence_td_recursive(dp, nums, 0, -1)

def longest_increasing_subsequence_td_recursive(dp, nums, currentIdx, parentIdx):
    if currentIdx == len(nums):
        return 0
    if dp[currentIdx][parentIdx] == -1:
        with_current = 0
        if parentIdx == -1 or nums[currentIdx] > nums[parentIdx]:
            with_current = 1 + longest_increasing_subsequence_td_recursive(dp, nums, currentIdx+1, currentIdx)

        without_current = longest_increasing_subsequence_td_recursive(dp, nums, currentIdx+1, parentIdx)
        dp[currentIdx][parentIdx] = max(with_current, without_current)
    return dp[currentIdx][parentIdx]

# O(n^2) time | O(n) space
def longest_increasing_subsequence_btmup(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    maxLength = float('-inf')

    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = 1 + dp[j]
                maxLength = max(maxLength, dp[i])
    return maxLength

if __name__ == '__main__':
    # Using recursion
    print (longest_increasing_subsequence([4,2,3,6,10,1,12]))
    print (longest_increasing_subsequence([-4,10,3,7,15]))
    # Using top-down DP
    print (longest_increasing_subsequence_td([4,2,3,6,10,1,12]))
    print (longest_increasing_subsequence_td([-4,10,3,7,15]))
    # Using bottom-up DP
    print (longest_increasing_subsequence_btmup([4,2,3,6,10,1,12]))
    print (longest_increasing_subsequence_btmup([-4,10,3,7,15]))
