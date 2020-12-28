# Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

def find_target_subsets(arr, S):
    if (not arr) or (not S):
        return 0
    desired_sum = (sum(arr)+S)//2
    return find_target_subsets_recursive(arr, desired_sum, 0)

def find_target_subsets_recursive(arr, S, currentIndex):
    if not S:
        return 1
    if currentIndex > len(arr)-1:
        return 0
    ways1 = 0
    if arr[currentIndex] <= S:
        ways1 = find_target_subsets_recursive(arr, S-arr[currentIndex], currentIndex+1)
    ways2 = find_target_subsets_recursive(arr, S, currentIndex+1)
    return ways1+ways2

def find_target_subsets_td(arr, S):
    if (not arr) or (not S):
        return 0
    desired_sum = (sum(arr)+S)//2
    dp = [[-1 for _ in range(desired_sum+1)] for _ in range(len(arr))]
    return find_target_subsets_td_recursive(dp, arr, desired_sum, 0)

def find_target_subsets_td_recursive(dp, arr, desired_sum, currentIndex):
    if not desired_sum:
        return 1
    if currentIndex > len(arr)-1:
        return 0

    if not (dp[currentIndex][desired_sum]+1):
        ways1 = 0
        if arr[currentIndex] <= desired_sum:
            ways1 = find_target_subsets_recursive(arr, desired_sum-arr[currentIndex], currentIndex+1)
        ways2 = find_target_subsets_recursive(arr, desired_sum, currentIndex+1)
        dp[currentIndex][desired_sum] = ways1+ways2
    return dp[currentIndex][desired_sum]

def find_target_subsets_btmup(arr, S):
    if (not arr) or (not S):
        return 0
    desired_sum = (sum(arr)+S)//2
    dp = [[-1 for _ in range(desired_sum+1)] for _ in range(len(arr))]

    # Populating column=0, ways=0 for empty set
    for row in range(len(arr)):
        dp[row][0] = 1

    # Populating row=0, ways = 1 when col = arr[0]
    for col in range(1, desired_sum+1):
        dp[0][col] = 1 if col == arr[0] else 0

    # Populating other subsets
    for row in range(1, len(arr)):
        for col in range(1, desired_sum+1):
            dp[row][col] = dp[row-1][col]
            if col >= arr[row]:
                dp[row][col] += dp[row-1][col-arr[row]]

    return dp[-1][-1]

def main():
    # Using plain recursion
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))
    # Using top-down recursion
    print("Total ways (Top-Down): " + str(find_target_subsets_td([1, 1, 2, 3], 1)))
    print("Total ways (Top-Down): " + str(find_target_subsets_td([1, 2, 7, 1], 9)))
    # Using bottom-up recursion
    print("Total ways (Bottom-Up): " + str(find_target_subsets_btmup([1, 1, 2, 3], 1)))
    print("Total ways (Bottom-Up): " + str(find_target_subsets_btmup([1, 2, 7, 1], 9)))

main()
