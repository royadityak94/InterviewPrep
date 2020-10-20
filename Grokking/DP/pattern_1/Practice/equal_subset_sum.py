# Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

def exists_subset(arr, S):
    if (not arr) or (not S):
        return False
    return exists_subset_recursive(arr, S, 0)

def exists_subset_recursive(arr, desired_sum, currentIndex):
    if not desired_sum:
        return True
    if currentIndex > len(arr)-1:
        return False

    if arr[currentIndex] <= desired_sum:
        if exists_subset_recursive(arr, desired_sum-arr[currentIndex], currentIndex+1):
            return True
    return exists_subset_recursive(arr, desired_sum, currentIndex+1)

def exists_subset_dp(arr, S):
    if (not arr) or (not S):
        return False
    dp = [[False for _ in range(S+1)] for _ in range(len(arr))]
    return exists_subset_dp_recursive(dp, arr, S, 0)

def exists_subset_dp_recursive(dp, arr, desired_sum, currentIndex):
    if not desired_sum:
        return True
    if currentIndex > len(arr)-1:
        return False

    if not dp[currentIndex][desired_sum]:
        if arr[currentIndex] <= desired_sum:
            if exists_subset_dp_recursive(dp, arr, desired_sum-arr[currentIndex], currentIndex+1):
                dp[currentIndex][desired_sum] = True
        exists_subset_dp_recursive(dp, arr, desired_sum, currentIndex+1)
    return dp[currentIndex][desired_sum]

def exists_subset_bottom_up(arr, S):
    if (not arr) or (not S):
        return False
    dp = [[False for _ in range(S+1)] for _ in range(len(arr))]

    # Populating column=0
    for row in range(len(arr)):
        dp[row][0] = True

    # Populating row=0
    for col in range(1, S+1):
        dp[0][col] = col == arr[0]

    # Populating other subsets
    for row in range(1, len(arr)):
        for col in range(1, S+1):
            if dp[row-1][col]:
                dp[row][col] = True
            elif col >= arr[row]:
                dp[row][col] = dp[row-1][col-arr[row]]
    return dp[-1][-1]

def main():
    # plain-recursion
    print (exists_subset([1, 2, 3, 7], 6))
    print (exists_subset([1, 2, 7, 1, 5], 10))
    print (exists_subset([1, 3, 4, 8], 6))

    # top-down DP
    print (exists_subset_dp([1, 2, 3, 7], 6))
    print (exists_subset_dp([1, 2, 7, 1, 5], 10))
    print (exists_subset_dp([1, 3, 4, 8], 6))

    # Bottom-up DP
    print (exists_subset_bottom_up([1, 2, 3, 7], 6))
    print (exists_subset_bottom_up([1, 2, 7, 1, 5], 10))
    print (exists_subset_bottom_up([1, 3, 4, 8], 6))


main()
