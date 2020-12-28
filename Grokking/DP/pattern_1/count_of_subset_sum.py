# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

def count_subsets(arr, S):
    if (not arr) or (not S):
        return 0
    return count_subsets_recursive(arr, S, 0)

def count_subsets_recursive(arr, S, currentIndex):
    if not S:
        return 1
    if currentIndex > len(arr) - 1:
        return 0

    count1 = 0
    if arr[currentIndex] <= S:
        count1 = count_subsets_recursive(arr, S-arr[currentIndex], currentIndex+1)
    count2 = count_subsets_recursive(arr, S, currentIndex+1)
    return count1+count2

def count_subsets_td(arr, S):
    if (not arr) or (not S):
        return 0
    dp = [[-1 for _ in range(S+1)] for _ in range(len(arr))]
    return count_subsets_td_recursive(dp, arr, S, 0)

def count_subsets_td_recursive(dp, arr, S, currentIndex):
    if not S:
        return 1
    if currentIndex > len(arr) - 1:
        return 0

    if not (dp[currentIndex][S]+1):
        count1 = 0
        if arr[currentIndex] <= S:
            count1 = count_subsets_td_recursive(dp, arr, S-arr[currentIndex], currentIndex+1)
        count2 = count_subsets_td_recursive(dp, arr, S, currentIndex+1)
        dp[currentIndex][S] =  count1+count2
    return dp[currentIndex][S]

def count_subsets_btmup(arr, S):
    if (not arr) or (not S):
        return 0
    dp = [[-1 for _ in range(S+1)] for _ in range(len(arr))]

    # Populating column=0, there is always an empty set for zero sum
    for row in range(len(arr)):
        dp[row][0] = 1

    # Populating row=0, i.e. subset=1 where col=arr[0]
    for col in range(1, S+1):
        dp[0][col] = 1 if col == arr[0] else 0

    # Populating other subsets
    for row in range(1, len(arr)):
        for col in range(1, S+1):
            dp[row][col] = dp[row-1][col]
            if col >= arr[row]:
                dp[row][col] += dp[row-1][col-arr[row]]
    return dp[-1][-1]

def main():
    # Using plain Recursion
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
    # Using top-down Recursion
    print("Total number of subsets (Top-Down): " + str(count_subsets_td([1, 1, 2, 3], 4)))
    print("Total number of subsets (Top-Down): " + str(count_subsets_td([1, 2, 7, 1, 5], 9)))
    # Using bottom-up Recursion
    print("Total number of subsets (Bottom-Up): " + str(count_subsets_btmup([1, 1, 2, 3], 4)))
    print("Total number of subsets (Bottom-Up): " + str(count_subsets_btmup([1, 2, 7, 1, 5], 9)))

main()
