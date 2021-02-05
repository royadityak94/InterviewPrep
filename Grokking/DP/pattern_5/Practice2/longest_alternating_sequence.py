'''
Given a number sequence, find the length of its Longest Alternating Subsequence (LAS).
A subsequence is considered alternating if its elements are in alternating order.
A three element sequence (a1, a2, a3) will be an alternating sequence if its elements hold one of the following conditions:
{a1 > a2 < a3 } or { a1 < a2 > a3}.
'''

def lass(nums):
    return max(lass_recursive(nums, 0, -1, True), lass_recursive(nums, 0, -1, False))

def lass_recursive(nums, currentIdx, previousIdx, isAscending):
    if currentIdx == len(nums):
        return 0
    b1, b2 = 0, 0
    if isAscending:
        if previousIdx == -1 or nums[currentIdx] > nums[previousIdx]:
            b1 = 1 + lass_recursive(nums, currentIdx+1, currentIdx, (not isAscending))
    else:
        if previousIdx == -1 or nums[currentIdx] < nums[previousIdx]:
            b1 = 1 + lass_recursive(nums, currentIdx+1, currentIdx, (not isAscending))
    b2 = lass_recursive(nums, currentIdx+1, previousIdx, isAscending)
    return max(b1, b2)

def lass_td(nums):
    dp = [[[-1 for _ in range(2)] for _ in range(len(nums))] for _ in range(len(nums))]
    return max(lass_td_recursive(dp, nums, 0, -1, True), lass_td_recursive(dp, nums, 0, -1, False))

def lass_td_recursive(dp, nums, currentIdx, previousIdx, isAscending):
    if currentIdx == len(nums):
        return 0
    if dp[currentIdx][previousIdx][int(isAscending)] == -1:
        b1, b2 = 0, 0
        if isAscending:
            if previousIdx == -1 or nums[currentIdx] > nums[previousIdx]:
                b1 = 1 + lass_td_recursive(dp, nums, currentIdx+1, currentIdx, (not isAscending))
        else:
            if previousIdx == -1 or nums[currentIdx] < nums[previousIdx]:
                b1 = 1 + lass_td_recursive(dp, nums, currentIdx+1, currentIdx, (not isAscending))
        b2 = lass_td_recursive(dp, nums, currentIdx+1, previousIdx, isAscending)
        dp[currentIdx][previousIdx][int(isAscending)] = max(b1, b2)
    return dp[currentIdx][previousIdx][int(isAscending)]

def lass_btmup(nums):
    n = len(nums)
    dp = [[0 for _ in range(2)] for _ in range(n)] # 0:Descending, 1:Ascending
    maxLength = 1
    for i in range(n):
        dp[i][0] = dp[i][1] = 1
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i][1] = max(dp[i][1], 1+dp[j][0])
                maxLength = max(maxLength, dp[i][1])
            elif nums[i] < nums[j]:
                dp[i][0] = max(dp[i][0], 1+dp[j][1])
                maxLength = max(maxLength, dp[i][0])
    return maxLength



if __name__ == '__main__':
    # Plain Recursion
    print (lass([1, 2, 3, 4])) # 2 [{1,2}, {3,4}, {1,3}, {1,4}]
    print (lass([3, 2, 1, 4])) # 3 [{3, 2, 4}, {2, 1, 4}]
    print (lass([1, 3, 2, 4])) # 4 [{1, 3, 2, 4}]
    # Top-Down DP
    print (lass_td([1, 2, 3, 4])) # 2
    print (lass_td([3, 2, 1, 4])) # 3
    print (lass_td([1, 3, 2, 4])) # 4
    # Bottom-Up DP
    print (lass_btmup([1, 2, 3, 4])) # 2
    print (lass_btmup([3, 2, 1, 4])) # 3
    print (lass_btmup([1, 3, 2, 4])) # 4
