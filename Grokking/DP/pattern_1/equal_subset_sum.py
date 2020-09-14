# Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

def exists_subset(arr, sum):
    return exists_subset_recursive(arr, sum, 0)

def exists_subset_recursive(arr, sum, currentIndex):
    if sum == 0:
        return True
    if not len(arr) or currentIndex >= len(arr):
        return False

    if arr[currentIndex] <= sum:
        if exists_subset_recursive(arr, sum-arr[currentIndex], currentIndex+1) == 1:
            return True
    return exists_subset_recursive(arr, sum, currentIndex+1)

def exists_subset_dp(arr, sum):
    dp = [[-1 for _ in range(sum+1)] for _ in arr]
    recv = exists_subset_dp_recursive(dp, arr, sum, 0)
    return True if exists_subset_dp_recursive(dp, arr, sum, 0) == 1 else False

def exists_subset_dp_recursive(dp, arr, sum, currentIndex):
    if sum == 0:
        #print ("Got it ....", arr)
        return 1

    if currentIndex >= len(arr):
        return -1

    if dp[currentIndex][sum] == -1:
        if arr[currentIndex] <= sum:
            if exists_subset_dp_recursive(dp, arr, sum-arr[currentIndex], currentIndex+1) == 1:
                dp[currentIndex][sum] = 1
                return 1

        dp[currentIndex][sum] = exists_subset_dp_recursive(dp, arr, sum, currentIndex+1)

    return dp[currentIndex][sum]

def exists_subset_bottom_up(arr, sum_):
    # Time Complexity: O(N*S), Space Complexity: O(S)
    if len(arr) == 0:
        print (">> I said")
        return False

    n = len(arr)

    dp = [[False for _ in range(sum_+1)] for _ in arr]

    # Filling sum = 0 column, i.e. for first row, such partitions do exists
    for r in range(n):
        dp[r][0] = True

    for c in range(sum_+1):
        if arr[0] == sum_:
            dp[0][c] = True

    for i in range(1, n):
        for j in range(1, sum_+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= arr[i]:
                dp[i][j] = dp[i-1][j-arr[i]]

    return dp[n-1][sum_-1]

def main():
    # plain-recursion
    print (exists_subset([1, 2, 3, 7], 6))
    print (exists_subset([1, 2, 7, 1, 5], 10))
    print (exists_subset([1, 3, 4, 8], 6))

    # top-down DP
    print (exists_subset_dp([1, 2, 3, 7], 6))
    print (exists_subset_dp([1, 2, 7, 1, 5], 10))
    print (exists_subset_dp([1, 3, 4, 8], 6))

    for _ in range(50): print('-', end='')
    print()
    # Bottom-up DP
    print (exists_subset_bottom_up([1, 2, 3, 7], 6))
    print (exists_subset_bottom_up([1, 2, 7, 1, 5], 10))
    print (exists_subset_bottom_up([1, 3, 4, 8], 6))


main()
