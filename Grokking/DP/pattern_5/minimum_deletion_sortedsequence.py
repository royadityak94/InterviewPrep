'''
Given a number sequence, find the minimum number of elements that should be deleted to make the remaining sequence sorted.
'''
# O(2^n) time | O(n) space
def min_deletions(nums):
    c = min_deletions_recursive(nums, 0, -1)
    return len(nums)-c

def min_deletions_recursive(nums, currentIdx, previousIdx):
    if currentIdx == len(nums):
        return 0

    withCurrent = 0
    if previousIdx == -1 or nums[currentIdx] >= nums[previousIdx]:
        withCurrent = 1 + min_deletions_recursive(nums, currentIdx+1, currentIdx)
    withoutCurrent = min_deletions_recursive(nums, currentIdx+1, previousIdx)
    return max(withCurrent, withoutCurrent)

# O(n^2) time | O(n) space
def min_deletions_td(nums):
    dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
    c = min_deletions_td_recursive(dp, nums, 0, -1)
    return len(nums)-c

def min_deletions_td_recursive(dp, nums, currentIdx, previousIdx):
    if currentIdx == len(nums):
        return 0

    if dp[currentIdx][previousIdx]:
        withCurrent = 0
        if previousIdx == -1 or nums[currentIdx] >= nums[previousIdx]:
            withCurrent = 1 + min_deletions_td_recursive(dp, nums, currentIdx+1, currentIdx)
        withoutCurrent = min_deletions_td_recursive(dp, nums, currentIdx+1, previousIdx)
        dp[currentIdx][previousIdx] = max(withCurrent, withoutCurrent)
    return dp[currentIdx][previousIdx]

# # O(n^2) time | O(n) space
def min_deletions_btmup(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = 1
    for i in range(1, len(nums)):
        dp[i] = 1
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = 1 + dp[j]
    return len(nums) - dp[-1]


if __name__ == '__main__':
    # Plain Recursion
    print (min_deletions([4,2,3,6,10,1,12]))
    print (min_deletions([-4,10,3,7,15]))
    print (min_deletions([3,2,1,0]))
    # TopDown TD
    print (min_deletions_td([4,2,3,6,10,1,12]))
    print (min_deletions_td([-4,10,3,7,15]))
    print (min_deletions_td([3,2,1,0]))
    # BottomUp TD
    print (min_deletions_btmup([4,2,3,6,10,1,12]))
    print (min_deletions_btmup([-4,10,3,7,15]))
    print (min_deletions_btmup([3,2,1,0]))
