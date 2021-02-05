# Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

def max_sum_incr_subseq(nums):
    return max_sum_incr_subseq_recursive(nums, 0, -1, 0)

def max_sum_incr_subseq_recursive(nums, currentIdx, previousIdx, sum):
    if currentIdx == len(nums):
        return sum
    with_current = sum
    if previousIdx == -1 or nums[currentIdx] > nums[previousIdx]:
        with_current = max_sum_incr_subseq_recursive(nums, currentIdx+1, currentIdx, sum+nums[currentIdx])
    without_current = max_sum_incr_subseq_recursive(nums, currentIdx+1, previousIdx, sum)
    return max(with_current, without_current)

def max_sum_incr_subseq_td(nums):
    n = len(nums)
    s = sum(nums)
    dp = [[[-1 for _ in range(s+1)] for _ in range(n)] for _ in range(n)]
    return max_sum_incr_subseq_td_recursive(dp, nums, 0, -1, 0)

def max_sum_incr_subseq_td_recursive(dp, nums, currentIdx, previousIdx, sum):
    if currentIdx == len(nums):
        return sum

    if dp[currentIdx][previousIdx][sum] == -1:
        with_current = sum
        if previousIdx == -1 or nums[currentIdx] > nums[previousIdx]:
            with_current = max_sum_incr_subseq_td_recursive(dp, nums, currentIdx+1, currentIdx, sum+nums[currentIdx])
        without_current = max_sum_incr_subseq_td_recursive(dp, nums, currentIdx+1, previousIdx, sum)
        dp[currentIdx][previousIdx][sum] = max(with_current, without_current)
    return dp[currentIdx][previousIdx][sum]

def max_sum_incr_subseq_btmup(nums):
    dp = [0 for _ in range(len(nums))]
    maxSum = float('-inf')
    for i in range(len(nums)):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < nums[i] + dp[j]:
                dp[i] = nums[i] + dp[j]
        maxSum = max(maxSum, dp[i])
    return maxSum

if __name__ == '__main__':
    # using simple recursion
    print (max_sum_incr_subseq([4,1,2,6,10,1,12]))
    print (max_sum_incr_subseq([-4,10,3,7,15]))
    # using top-down DP
    print (max_sum_incr_subseq_td([4,1,2,6,10,1,12]))
    print (max_sum_incr_subseq_td([-4,10,3,7,15]))
    # using bottom-up DP
    print (max_sum_incr_subseq_btmup([4,1,2,6,10,1,12]))
    print (max_sum_incr_subseq_btmup([-4,10,3,7,15]))
