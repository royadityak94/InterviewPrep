# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

def can_partition(arr):
    # Time Complexity: O(2^N), Space Complexity: O(N)
    if not arr:
        return False
    S = sum(arr)
    if S%2:
        return False
    return can_partition_recursive(arr, S//2, 0)

def can_partition_recursive(arr, desired_sum, currentIndex):
    if desired_sum == 0:
        return True
    if currentIndex > len(arr)-1:
        return False

    if arr[currentIndex] <= desired_sum:
        if can_partition_recursive(arr, desired_sum-arr[currentIndex], currentIndex+1):
            return True
    return can_partition_recursive(arr, desired_sum, currentIndex+1)

def can_partition_td(arr):
    # Time Complexity = Space Complexity = O(NS), N=len(arr), S=Sum(arr)
    if not arr:
        return False
    S = sum(arr)
    if S%2:
        return False
    dp = [[False for _ in range(S+1)] for _ in range(len(arr))]
    return can_partition_td_recursive(dp, arr, S//2, 0)

def can_partition_td_recursive(dp, arr, desired_sum, currentIndex):
    if desired_sum == 0:
        return True
    if currentIndex > len(arr)-1:
        return False

    if not dp[currentIndex][desired_sum]:
        if arr[currentIndex] <= desired_sum:
            if can_partition_recursive(arr, desired_sum-arr[currentIndex], currentIndex+1):
                dp[currentIndex][desired_sum] = True
        return can_partition_recursive(arr, desired_sum, currentIndex+1)
    return dp[currentIndex][desired_sum]

def can_partition_btmup(arr):
    # Time Complexity = Space Complexity = O(NS), N=len(arr), S=Sum(arr)
    if not arr:
        return False
    S = sum(arr)
    if S%2:
        return False
    S = S//2
    dp = [[False for _ in range(S+1)] for _ in range(len(arr))]

    # Populating column=0, i.e. we can always have an empty set
    for row in range(len(arr)):
        dp[row][0] = True

    # Populating row=0, i.e. when col == arr[0]
    for col in range(1, S+1):
        dp[0][col] = col==arr[0]

    # Populating other subsets
    for row in range(1, len(arr)):
        for col in range(1, S+1):
            if dp[row-1][col]:
                dp[row][col] = True
            elif col >= arr[row]:
                dp[row][col] = dp[row-1][col-arr[row]]
    return dp[-1][-1]

def main():
    # Using simple recursion
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))
    # Using top-down recursion
    print("Can partition: " + str(can_partition_td([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition_td([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_td([2, 3, 4, 6])))
    # # Using bottom-up recursion
    print("Can partition: " + str(can_partition_btmup([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition_btmup([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_btmup([2, 3, 4, 6])))

main()
