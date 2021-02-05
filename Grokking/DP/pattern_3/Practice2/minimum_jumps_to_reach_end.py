# Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

maxValue = float('inf')

def count_min_jumps(jumps):
    return count_min_jumps_recursive(jumps, 0)

def count_min_jumps_recursive(jumps, currentIdx):
    if currentIdx >= len(jumps) - 1:
        return 0
    elif not jumps[currentIdx]:
        return maxValue

    totalJumps = maxValue
    start, end = currentIdx + 1, currentIdx + jumps[currentIdx]
    while start < len(jumps) and start <= end:
        minJumps = count_min_jumps_recursive(jumps, start)
        if minJumps < maxValue:
            totalJumps = min(totalJumps, minJumps+1)
        start += 1
    return totalJumps

def count_min_jumps_td(jumps):
    dp = [-1 for _ in range(len(jumps)+1)]
    return count_min_jumps_td_recursive(dp, jumps, 0)

def count_min_jumps_td_recursive(dp, jumps, currentIdx):
    if currentIdx >= len(jumps) - 1:
        return 0
    elif not jumps[currentIdx]:
        return maxValue

    if dp[currentIdx] == -1:
        totalJumps = maxValue
        start, end = currentIdx + 1, currentIdx + jumps[currentIdx]
        while start < len(jumps) and start <= end:
            minJumps = count_min_jumps_td_recursive(dp, jumps, start)
            if minJumps < maxValue:
                totalJumps = min(totalJumps, minJumps+1)
            start += 1
        dp[currentIdx] = totalJumps
    return dp[currentIdx]

def count_min_jumps_bottomup(jumps):
    n = len(jumps)
    dp = [maxValue for _ in range(n)]
    dp[0] = 0
    for start in range(n-1):
        end = start + 1
        while end < n and end <= start + jumps[start]:
            dp[end] = min(dp[end], 1+dp[start])
            end += 1
    return dp[n-1]


def main():
    # Using simple recursion
    print (count_min_jumps([2, 1, 1, 1, 4]))
    # using top-down recursion - min jumps
    print (count_min_jumps_td([2, 1, 1, 1, 4]))
    # using bottom-up recursion - min jumps
    print (count_min_jumps_bottomup([2, 1, 1, 1, 4]))

main()
