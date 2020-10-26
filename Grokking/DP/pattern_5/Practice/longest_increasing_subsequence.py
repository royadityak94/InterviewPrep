# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).
# [4,2,3,6,10,1,12] -> len({2,3,6,10,12}) = 5
# [-4,10,3,7,15] -> len([-4, 3, 7, 15]) = 4

def longest_increasing_subsequence(arr):
    # Time Complexity: O(2^N), Space Complexity: O(N)
    if not arr:
        return 0
    return longest_increasing_subsequence_recursive(arr, 0, -1)

def longest_increasing_subsequence_recursive(arr, currIndex, prevIndex):
    if currIndex == len(arr):
        return 0
    count1 = 0
    if prevIndex == -1 or arr[currIndex] > arr[prevIndex]:
        count1 = 1 + longest_increasing_subsequence_recursive(arr, currIndex+1, currIndex)
    count2 = longest_increasing_subsequence_recursive(arr, currIndex+1, prevIndex)
    return max(count1, count2)

def longest_increasing_subsequence_td(arr):
    # Time Complexity: O(N^N), Space Complexity: O(N^N)
    if not arr:
        return 0
    dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    return longest_increasing_subsequence_td_recursive(dp, arr, 0, -1)

def longest_increasing_subsequence_td_recursive(dp, arr, currIndex, prevIndex):
    if currIndex == len(arr):
        return 0
    if not dp[currIndex][prevIndex]:
        count1 = 0
        if prevIndex == -1 or arr[currIndex] > arr[prevIndex]:
            count1 = 1 + longest_increasing_subsequence_recursive(arr, currIndex+1, currIndex)
        count2 = longest_increasing_subsequence_recursive(arr, currIndex+1, prevIndex)
        dp[currIndex][prevIndex] = max(count1, count2)
    return dp[currIndex][prevIndex]

def longest_increasing_subsequence_btmup(arr):
    # Time Complexity: O(N^N), Space Complexity: O(N)
    if not arr:
        return 0
    dp = [0 for _ in arr]
    dp[0] = 1
    maxLength = 1
    for i in range(1, len(arr)):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j] and dp[i] <= dp[j]:
                dp[i] = dp[j]+1
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
