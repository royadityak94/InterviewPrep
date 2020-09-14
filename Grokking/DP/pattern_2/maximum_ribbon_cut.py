# We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. Now we need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

def maximum_ribbon_cuts(arr, max_size):
    # Time Complexity = Space Complexity = O(2^(len(arr)+max_size)
    if len(arr) == 0 or max_size == 0:
        return 0
    return maximum_ribbon_cuts_recursive(arr, max_size, 0)

def maximum_ribbon_cuts_recursive(arr, max_size, currentIndex):
    if max_size == 0:
        return 0
    if currentIndex >= len(arr):
        return float('-inf')

    with_current = without_current = float('-inf')
    if arr[currentIndex] <= max_size:
        resultant = maximum_ribbon_cuts_recursive(arr, max_size-arr[currentIndex], currentIndex)
        if resultant > float('-inf'):
            with_current = 1 + resultant
    without_current = maximum_ribbon_cuts_recursive(arr, max_size, currentIndex+1)
    return max(with_current, without_current)

def maximum_ribbon_cuts_dp(arr, max_size):
    # Time Complexity = Space Complexity = O(len(arr)*max_size)
    if len(arr) == 0 or max_size == 0:
        return 0
    dp = [[float('-inf') for _ in range(max_size+1)] for _ in arr]
    return maximum_ribbon_cuts_dp_recursion(dp, arr, max_size, 0)

def maximum_ribbon_cuts_dp_recursion(dp, arr, max_size, currentIndex):
    if max_size == 0:
        return 0
    if currentIndex >= len(arr):
        return float('-inf')

    if dp[currentIndex][max_size] == float('-inf'):
        with_current = without_current = float('-inf')
        if arr[currentIndex] <= max_size:
            from_current = maximum_ribbon_cuts_dp_recursion(dp, arr, max_size - arr[currentIndex], currentIndex)
            if from_current > float('-inf'):
                with_current = 1 + from_current
        without_current = maximum_ribbon_cuts_dp_recursion(dp, arr, max_size, currentIndex+1)
        dp[currentIndex][max_size] = max(with_current, without_current)
    return dp[currentIndex][max_size]

def maximum_ribbon_cuts_bottomup_dp(arr, max_size):
    # Time Complexity = Space Complexity = O(len(arr)*max_size)
    if len(arr) == 0 or max_size == 0:
        return 0
    dp = [[float('-inf') for _ in range(max_size+1)] for _ in arr]

    # Populating column = 0, i.e. maximum cuts = 0 when max_size = 0
    for row in range(len(arr)):
        dp[row][0] = 0

    # Populating other subsets, for all cuts, sizes
    for i in range(len(arr)):
        for c in range(1, max_size+1):
            if i > 0:
                dp[i][c] = dp[i-1][c]
            if arr[i] <= c:
                if dp[i][c - arr[i]] > float('-inf'):
                    dp[i][c] = max(dp[i][c], dp[i][c-arr[i]]+1)

    return dp[len(arr)-1][max_size]


def main():
    # using plain recursion
    print (maximum_ribbon_cuts([5, 2, 3], 5))
    print (maximum_ribbon_cuts([5, 2, 3], 15))
    # using top-down DP
    print (maximum_ribbon_cuts_dp([5, 2, 3], 5))
    print (maximum_ribbon_cuts_dp([5, 2, 3], 15))
    # using bottom-up DP
    print (maximum_ribbon_cuts_bottomup_dp([5, 2, 3], 5))
    print (maximum_ribbon_cuts_bottomup_dp([5, 2, 3], 15))

main()
