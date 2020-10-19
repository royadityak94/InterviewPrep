#Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

def can_partition(arr, S):
    # Time Complexity = O(2^N), Space Complexity: O(N)
    if (not len(arr)) or (not S):
        return False
    return can_partition_recursive(arr, S, 0)

def can_partition_recursive(arr, S, currentIndex):
    if (not S):
        return True
    if currentIndex > len(arr)-1:
        return False

    if arr[currentIndex] <= S:
        if can_partition_recursive(arr, S-arr[currentIndex], currentIndex+1):
            return True
    return can_partition_recursive(arr, S, currentIndex+1)

def can_partition_btmup(arr, S):
    # Time Complexity = Space Complexity: O(NS), N=len(arr)
    if (not len(arr)) or (not S):
        return False
    dp = [[False for _ in range(S+1)] for _ in range(len(arr))]

    # Populating column=0
    for row in range(len(arr)):
        dp[row][0] = True
    # Populating row=0
    for col in range(1, S+1):
        dp[0][col] = (col==arr[0])

    # Populating other subsets
    for row in range(1, len(arr)):
        for col in range(1, S+1):
            if dp[row-1][col]:
                dp[row][col] = True
            elif col >= arr[row]:
                dp[row][col] = dp[row-1][col-arr[row]]
    return dp[-1][-1]

def main():
    # Using recursion
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))
    # Using top-down DP
    print("Can partition: " + str(can_partition_btmup([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition_btmup([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition_btmup([1, 3, 4, 8], 6)))

main()
