# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’
# {1, 2, 3, 7}, S=6

def can_partition(arr, sum):
    if len(arr) == 0:
        return False
    dp = [[-1 for _ in range(sum+1)] for _ in arr]
    #return can_partition_recursive(arr, sum, 0)
    #return True if can_partition_recursive_dp(dp, arr, sum, 0) == 1 else False
    return can_partition_dp_bottom_up(arr, sum)

def can_partition_recursive(arr, sum, currentIndex):
    if sum == 0:
        return True
    n = len(arr)
    if currentIndex >= n:
        return False

    if arr[currentIndex] <= sum:
        if can_partition_recursive(arr, sum-arr[currentIndex], currentIndex+1):
            return True
    return can_partition_recursive(arr, sum, currentIndex+1)

def can_partition_recursive_dp(dp, arr, sum, currentIndex):
    if sum == 0:
        print ("I returned .....: flag1")
        return True
    if len(arr) == 0 or currentIndex >= len(arr):
        return False

    if dp[currentIndex][sum] == -1:
        if arr[currentIndex] <= sum:
            if can_partition_recursive_dp(dp, arr, sum-arr[currentIndex], currentIndex+1):
                dp[currentIndex][sum] = 1
                print ("I returned - flag 2..... : ",sum-arr[currentIndex])
                return 1
        dp[currentIndex][sum] = can_partition_recursive_dp(dp, arr, sum, currentIndex+1)

    return dp[currentIndex][sum]

def can_partition_dp_bottom_up(num, sum):
    # Time Complexity: O(NS), Space Complexity: O(S)
    n = len(num)
    dp = [[False for x in range(sum+1)] for y in range(n)]

    # populate the sum = 0 columns, as we can always form '0' sum with an empty set
    for i in range(0, n):
    dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for s in range(1, sum+1):
    dp[0][s] = True if num[0] == s else False

    # process all subsets for all sums
    for i in range(1, n):
    for s in range(1, sum+1):
      # if we can get the sum 's' without the number at index 'i'
      if dp[i - 1][s]:
        dp[i][s] = dp[i - 1][s]
      elif s >= num[i]:
        # else include the number and see if we can find a subset to get the remaining sum
        dp[i][s] = dp[i - 1][s - num[i]]

    # the bottom-right corner will have our answer.
    return dp[n - 1][sum]


def main():
    arr = [1, 2, 3, 7]
    sum = 13
    print (can_partition(arr, sum))

main()
