'''
Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS). A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.
'''
# O(2^n) time | O(n) space
def lbs(nums):
    maxLength = 0
    for i in range(len(nums)):
        in_positive = lbs_recursive(nums, i, -1)
        in_negative = lbs_rev_recursive(nums, i, -1)
        maxLength = max(maxLength, (in_positive+in_negative-1))
    return maxLength

def lbs_recursive(nums, currentIdx, previousIdx):
    if currentIdx == len(nums):
        return 0
    with_current = 0
    if previousIdx == -1 or nums[currentIdx] < nums[previousIdx]:
        with_current = 1 + lbs_recursive(nums, currentIdx+1, currentIdx)
    without_current = lbs_recursive(nums, currentIdx+1, previousIdx)
    return max(with_current, without_current)

def lbs_rev_recursive(nums, currentIdx, previousIdx):
    if currentIdx < 0:
        return 0
    with_current = 0
    if previousIdx == -1 or nums[currentIdx] < nums[previousIdx]:
        with_current = 1 + lbs_rev_recursive(nums, currentIdx-1, currentIdx)
    without_current = lbs_rev_recursive(nums, currentIdx-1, previousIdx)
    return max(with_current, without_current)

# O(n^2) time | O(n^2) space
def lbs_td(nums):
    dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
    dp_rev = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
    maxLength = 0
    for i in range(len(nums)):
        in_positive = lbs_td_recursive(dp, nums, i, -1)
        in_negative = lbs_td_rev_recursive(dp_rev, nums, i, -1)
        maxLength = max(maxLength, (in_positive+in_negative-1))
    return maxLength

def lbs_td_recursive(dp, nums, currentIdx, previousIdx):
    if currentIdx == len(nums):
        return 0
    if dp[currentIdx][previousIdx] == -1:
        with_current = 0
        if previousIdx == -1 or nums[currentIdx] < nums[previousIdx]:
            with_current = 1 + lbs_td_recursive(dp, nums, currentIdx+1, currentIdx)
        without_current = lbs_td_recursive(dp, nums, currentIdx+1, previousIdx)
        dp[currentIdx][previousIdx] = max(with_current, without_current)
    return dp[currentIdx][previousIdx]

def lbs_td_rev_recursive(dp, nums, currentIdx, previousIdx):
    if currentIdx < 0:
        return 0
    if dp[currentIdx][previousIdx] == -1:
        with_current = 0
        if previousIdx == -1 or nums[currentIdx] < nums[previousIdx]:
            with_current = 1 + lbs_rev_recursive(nums, currentIdx-1, currentIdx)
        without_current = lbs_rev_recursive(nums, currentIdx-1, previousIdx)
        dp[currentIdx][previousIdx] = max(with_current, without_current)
    return dp[currentIdx][previousIdx]

# O(n^2) time | O(n) space
def lbs_btmup(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp_rev = [0 for _ in range(n)]

    for i in range(n):
        dp[i] = 1
        for j in range(i)[::-1]:
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1+dp[j])

    for i in range(n)[::-1]:
        dp_rev[i] = 1
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                dp_rev[i] = max(dp_rev[i], 1+dp_rev[j])

    maxLength = 0
    for i in range(n):
        maxLength = max(maxLength, (dp[i]+dp_rev[i]-1))
    return maxLength

if __name__ == '__main__':
    # Plain Recursion
    print (lbs([4,2,3,6,10,1,12])) #5
    print (lbs([4,2,5,9,7,6,10,3,1])) #7
    # Top-Down DP
    print (lbs_td([4,2,3,6,10,1,12])) #5
    print (lbs_td([4,2,5,9,7,6,10,3,1])) #7
    # Bottom-Up DP
    print (lbs_btmup([4,2,3,6,10,1,12])) #5
    print (lbs_btmup([4,2,5,9,7,6,10,3,1])) #7
