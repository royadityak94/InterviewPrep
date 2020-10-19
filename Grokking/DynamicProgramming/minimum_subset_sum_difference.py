# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.


def can_partition(arr):
    return can_partition_recursive(arr, 0, 0, 0)

def can_partition_recursive(arr, sum1, sum2, currentIndex):
    if currentIndex == len(arr):
        return abs(sum1-sum2)
    diff1 = can_partition_recursive(arr, sum1+arr[currentIndex], sum2, currentIndex+1)
    diff2 = can_partition_recursive(arr, sum1, sum2+arr[currentIndex], currentIndex+1)
    return min(diff1, diff2)

def can_partition_td(arr):
    if not len(arr):
        return 0
    S = sum(arr)
    dp = [[-1 for _ in range(S+1)] for _ in range(len(arr))]
    return can_partition_td_recursive(dp, arr, 0, 0, 0)

def can_partition_td_recursive(dp, arr, sum1, sum2, currentIndex):
    if currentIndex == len(arr):
        return abs(sum1 - sum2)

    if not (dp[currentIndex][sum1]+1):
        diff1 = can_partition_td_recursive(dp, arr, sum1+arr[currentIndex], sum2, currentIndex+1)
        diff2 = can_partition_td_recursive(dp, arr, sum1, sum2+arr[currentIndex], currentIndex+1)
        dp[currentIndex][sum1] = min(diff1, diff2)
    return dp[currentIndex][sum1]

def can_partition_btmup(arr):
    if not len(arr):
        return 0
    S = sum(arr) // 2
    dp = [[False for _ in range(S+1)] for _ in range(len(arr))]

    # Populating column=0, always possible to get a set with 0 sum
    for row in range(len(arr)):
        dp[row][0] = True

    # Populating row=0, always possible to get a sum when (arr[0] == j)
    for col in range(1, S+1):
        dp[0][col] = (col == arr[0])

    # Populating other subsets
    for row in range(1, len(arr)):
        for col in range(1, S+1):
            if dp[row-1][col]:
                dp[row][col] = True
            elif col >= arr[row]:
                dp[row][col] = dp[row-1][col-arr[row]]

    sum1 = 0
    for i in range(S, -1, -1):
        if dp[len(arr)-1][i]:
            sum1 = i
            break
    sum2 = sum(arr) - sum1
    return abs(sum1-sum2)

def main():
    # Using simple recursion
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))
    # Using top-down DP
    print("Can partition: " + str(can_partition_td([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition_td([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition_td([1, 3, 100, 4])))
    # Using bottom-up DP
    print("Can partition: " + str(can_partition_btmup([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition_btmup([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition_btmup([1, 3, 100, 4])))

main()
