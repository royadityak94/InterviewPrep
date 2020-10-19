# You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’. (Super-hard, don't worry if you can't do it in first go, or just till recursion!!!)
# Soln : https://www.educative.io/courses/grokking-the-coding-interview/JE0BWB8DgAJ

# Logic: Sum(S1) = (S + Sum(num))/2; S is supplied.

def find_target_subsets(num, s):
    # Time Complexity = O(2^N), Space Complexity: O(N)
    if (not num) or (not s):
        return 0
    sum_ = sum(num)
    desired_sum = (s + sum_)//2
    return find_target_subsets_recursive(num, desired_sum, 0)

def find_target_subsets_recursive(num, s, currentIndex):
    if s == 0:
        return 1
    if currentIndex > len(num) - 1:
        return 0
    count1 = 0
    if num[currentIndex] <= s:
        count1 = find_target_subsets_recursive(num, s-num[currentIndex], currentIndex+1)
    count2 = find_target_subsets_recursive(num, s, currentIndex+1)
    return count1+count2

def find_target_subsets_td(num, s):
    # Time Complexity = Space Complexity = O(N*s)
    if (not num) or (not s):
        return 0
    sum_ = sum(num)
    desired_sum = (s + sum_)//2
    dp = [[-1 for _ in range(desired_sum+1)] for _ in range(len(num))]
    return find_target_subsets_td_recursive(dp, num, desired_sum, 0)

def find_target_subsets_td_recursive(dp, num, desired_sum, currentIndex):
    if desired_sum == 0:
        return 1
    if currentIndex > len(num) - 1:
        return 0

    if not (dp[currentIndex][desired_sum]+1):
        count1 = 0
        if num[currentIndex] <= desired_sum:
            count1 = find_target_subsets_recursive(num, desired_sum-num[currentIndex], currentIndex+1)
        count2 = find_target_subsets_recursive(num, desired_sum, currentIndex+1)
        dp[currentIndex][desired_sum] = count1+count2

    return dp[currentIndex][desired_sum]

def find_target_subsets_btmup(arr, s):
    # Time Complexity = Space Complexity = O(N*s)
    if (not arr) or (not s):
        return 0
    sum_ = sum(arr)
    desired_sum = (s + sum_)//2
    dp = [[-1 for _ in range(desired_sum+1)] for _ in range(len(arr))]

    # For column=0, there is always a possibility of an empty set
    for row in range(len(arr)):
        dp[row][0] = 1
    # For row=0, count=1 where col == arr[0]
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
    # Recursive
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))
    # Top-Down DP
    print("Total ways: " + str(find_target_subsets_td([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets_td([1, 2, 7, 1], 9)))
    # Bottom-Up DP
    print("Total ways: " + str(find_target_subsets_btmup([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets_btmup([1, 2, 7, 1], 9)))

main()


# def count_subsets_recursive(num, sum, currentIndex):
#     if sum <= 0:
#         return 1
#     if currentIndex > len(num) - 1:
#         return 0
#     count1 = 0
#     if num[currentIndex] <= sum:
#         count1 = count_subsets_recursive(num, sum-num[currentIndex], currentIndex+1)
#     count2 = count_subsets_recursive(num, sum, currentIndex+1)
#     return count1+count2
