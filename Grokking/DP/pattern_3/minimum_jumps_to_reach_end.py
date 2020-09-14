# Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

def count_min_jumps(arr):
    if len(arr) == 0:
        return 0
    return count_min_jumps_recursive(arr, 0)

def count_min_jumps_recursive(arr, currentIndex):
    if currentIndex == len(arr)-1:
        return 0

    if arr[currentIndex] == 0:
        return float('inf')

    total_jumps = float('inf')
    start, end = currentIndex+1, currentIndex + arr[currentIndex]
    while start < len(arr) and start <= end:
        min_jump = count_min_jumps_recursive(arr, start)
        start += 1
        if min_jump < float('inf'):
            total_jumps = min(total_jumps, min_jump+1)
    return total_jumps

def count_max_jumps(arr):
    if len(arr) == 0:
        return 0
    return count_max_jumps_recursive(arr, 0)

def count_max_jumps_recursive(arr, currentIndex):
    if currentIndex == len(arr)-1:
        return 0
    if arr[currentIndex] == 0:
        return float('-inf')

    total_jumps = float('-inf')
    start, end = currentIndex+1, currentIndex + arr[currentIndex]

    while start < len(arr) and start <= end:
        max_jumps =  count_max_jumps_recursive(arr, start)
        start += 1
        if max_jumps > float('-inf'):
            total_jumps = max(total_jumps, max_jumps+1)
    return total_jumps

def count_min_jumps_td(arr):
    if len(arr) == 0:
        return 0
    dp = [float('inf') for _ in arr]
    return count_min_jumps_td_recursive(dp, arr, 0)

def count_min_jumps_td_recursive(dp, arr, currentIndex):
    if currentIndex == len(arr)-1:
        return 0

    if arr[currentIndex] == 0:
        return float('inf')

    if dp[currentIndex] == float('inf'):
        total_jumps = float('inf')
        start, end = currentIndex+1, currentIndex + arr[currentIndex]
        while start < len(arr) and start <= end:
            min_jump = count_min_jumps_recursive(arr, start)
            start += 1
            if min_jump < float('inf'):
                total_jumps = min(total_jumps, min_jump+1)
        dp[currentIndex] = total_jumps

    return dp[currentIndex]

def count_min_jumps_bottomup(arr):
    if len(arr) == 0:
        return 0

    n = len(arr)
    dp = [float('inf') for _ in arr]
    dp[0] = 0

    for start in range(n-1):
        end = start + 1
        while end <= start + arr[start] and end < n:
            dp[end] = min(dp[end], dp[start]+1)
            end += 1

    return dp[n-1]



def main():
    # Using simple recursion
    print (count_min_jumps([2, 1, 1, 1, 4]))

    # Using simple recursion
    print (count_max_jumps([2, 1, 1, 1, 4]))

    # using top-down recursion - min jumps
    print (count_min_jumps_td([2, 1, 1, 1, 4]))

    # using bottom-up recursion - min jumps
    print (count_min_jumps_bottomup([2, 1, 1, 1, 4]))



main()
