# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

def count_subsets(num, sum):
    # Time Complexity; O(2^N), Space Complexity: O(N)
    if (not len(num)) or (not sum):
        return 0
    return count_subsets_recursive(num, sum, 0)

def count_subsets_recursive(num, sum, currentIndex):
    if sum <= 0:
        return 1
    if currentIndex > len(num) - 1:
        return 0
    count1 = 0
    if num[currentIndex] <= sum:
        count1 = count_subsets_recursive(num, sum-num[currentIndex], currentIndex+1)
    count2 = count_subsets_recursive(num, sum, currentIndex+1)
    return count1+count2

def count_subsets_td(num, sum):
    # Time Complexity = Space Complexity = O(NS)
    if (not len(num)) or (not sum):
        return 0
    dp = [[-1 for _ in range(sum+1)] for _ in range(len(num))]
    return count_subsets_td_recursive(dp, num, sum, 0)

def count_subsets_td_recursive(dp, num, sum, currentIndex):
    if sum <= 0:
        return 1
    if currentIndex > len(num) - 1:
        return 0

    if not (dp[currentIndex][sum]+1):
        count1 = 0
        if num[currentIndex] <= sum:
            count1 = count_subsets_recursive(num, sum-num[currentIndex], currentIndex+1)
        count2 = count_subsets_recursive(num, sum, currentIndex+1)
        dp[currentIndex][sum] = count1+count2

    return dp[currentIndex][sum]

def count_subsets_btmup(num, sum):
    # Time Complexity = Space Complexity = O(NS)
    if (not len(num)) or (not sum):
        return 0
    dp = [[-1 for _ in range(sum+1)] for _ in range(len(num))]

    # For column=0, count=1
    for row in range(len(num)):
        dp[row][0] = 1

    # For row=0, count = 1, only when col=num[0]
    for col in range(1, sum+1):
        dp[0][col] = 1 if col==num[0] else 0

    # Populating other subsets
    for row in range(1, len(num)):
        for col in range(1, sum+1):
            dp[row][col] = dp[row-1][col]
            if col >= num[row]:
                dp[row][col] += dp[row-1][col-num[row]]
    return dp[-1][-1]

def main():
    # Using simple recursion
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
    # Using top-down recursion
    print("Total number of subsets " + str(count_subsets_td([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_td([1, 2, 7, 1, 5], 9)))
    # Using bottom-up recursion
    print("Total number of subsets " + str(count_subsets_btmup([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets_btmup([1, 2, 7, 1, 5], 9)))

main()
