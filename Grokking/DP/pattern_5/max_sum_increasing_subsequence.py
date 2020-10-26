# Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

def max_sum_incr_subseq(arr):
    # Time Complexity: O(2^N), Space Complexity: O(N)
    if not arr:
        return 0
    return max_sum_incr_subseq_recursive(arr, 0, -1)

def max_sum_incr_subseq_recursive(arr, currIndex, prevIndex):
    if currIndex == len(arr):
        return 0

    sum1 = 0
    if prevIndex == -1 or arr[currIndex] > arr[prevIndex]:
        sum1 = arr[currIndex] + max_sum_incr_subseq_recursive(arr, currIndex+1, currIndex)
    sum2 = max_sum_incr_subseq_recursive(arr, currIndex+1, prevIndex)
    return max(sum1, sum2)

def max_sum_incr_subseq_td(arr):
    # Time Complexity: O(N*N), Space Complexity: O(N*N)
    if not arr:
        return 0
    dp = [[0 for _ in arr] for _ in arr]
    return max_sum_incr_subseq_td_recursive(dp, arr, 0, -1)

def max_sum_incr_subseq_td_recursive(dp, arr, currIndex, prevIndex):
    if currIndex == len(arr):
        return 0

    if not dp[currIndex][prevIndex]:
        sum1 = 0
        if prevIndex == -1 or arr[currIndex] > arr[prevIndex]:
            sum1 = arr[currIndex] + max_sum_incr_subseq_td_recursive(dp, arr, currIndex+1, currIndex)
        sum2 = max_sum_incr_subseq_td_recursive(dp, arr, currIndex+1, prevIndex)
        dp[currIndex][prevIndex] = max(sum1, sum2)
    return dp[currIndex][prevIndex]

def max_sum_incr_subseq_btmup(arr):
    # Time Complexity: O(N*N), Space Complexity: O(N)
    if not arr:
        return 0
    dp = [0 for _ in arr]
    dp[0] = arr[0]
    maxSum = float('-inf')

    for i in range(1, len(arr)):
        dp[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j]+arr[i]:
                dp[i] = dp[j] + arr[i]
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
