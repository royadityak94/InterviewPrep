# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

def can_partition(arr):
    S = sum(arr)
    if S%2:
        return False
    return can_partition_recursive(arr, S//2, 0)

def can_partition_recursive(arr, desired_sum, currentIndex):
    if not desired_sum:
        return True
    if currentIndex > len(arr)-1:
        return False

    if arr[currentIndex] <= desired_sum:
        if can_partition_recursive(arr, desired_sum-arr[currentIndex], currentIndex+1):
            return True
    return can_partition_recursive(arr, desired_sum, currentIndex+1)

def can_partition_td(arr):
    S = sum(arr)
    if S%2:
        return False
    S //= 2
    dp = [[-1 for _ in range(S+1)] for _ in range(len(arr))]
    return can_partition_td_recursive(dp, arr, S, 0)

def can_partition_td_recursive(dp, arr, desired_sum, currentIndex):
    if not desired_sum:
        return True
    if currentIndex > len(arr)-1:
        return False

    if not (dp[currentIndex][desired_sum]+1):
        if arr[currentIndex] <= desired_sum:
            if can_partition_td_recursive(dp, arr, desired_sum-arr[currentIndex], currentIndex+1):
                dp[currentIndex][desired_sum] = True
        can_partition_td_recursive(dp, arr, desired_sum, currentIndex+1)
    return dp[currentIndex][desired_sum]

def can_partition_dp_bottomup(arr):
    S = sum(arr)
    if S%2:
        return False
    S //= 2
    dp = [[False for _ in range(S+1)] for _ in range(len(arr))]

    # Populating column=0, i.e. there is always an empty set which is equally divisible
    for row in range(len(arr)):
        dp[row][0] = True

    for col in range(1, S+1):
        dp[0][col] = col == arr[0]

    # Populating other subsets
    for row in range(1, len(arr)):
        for col in range(1, S+1):
            if dp[row-1][col]:
                dp[row][col] = True
            elif col >= arr[row]:
                dp[row][col] = dp[row-1][col - arr[row]]
    return dp[-1][-1]

def main():
    # Using simple recursion
    print (can_partition([1, 2, 3, 4]))
    print (can_partition([1, 1, 3, 4, 7]))
    print (can_partition([2, 3, 4, 6]))

    # Using top-down recursion
    print (can_partition_td([1, 2, 3, 4]))
    print (can_partition_td([1, 1, 3, 4, 7]))
    print (can_partition_td([2, 3, 4, 6]))

    # Using bottom-up recursion
    print (can_partition_dp_bottomup([1, 2, 3, 4]))
    print (can_partition_dp_bottomup([1, 1, 3, 4, 7]))
    print (can_partition_dp_bottomup([2, 3, 4, 6]))

main()
