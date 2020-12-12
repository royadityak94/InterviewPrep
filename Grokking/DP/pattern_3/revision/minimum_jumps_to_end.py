'''
Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.
'''

def count_min_jumps_btmup(jumps):
    # Time: O(N), Space: O(N)
    N = len(jumps)
    dp = [float('inf') for _ in range(N)]
    dp[0] = 0

    for start in range(N):
        end = start+1
        while end <= start + jumps[start] and end < N:
            dp[end] = min(dp[end], dp[start]+1)
            end += 1
    return dp[N-1]


def main():
    print(count_min_jumps_btmup([2, 1, 1, 1, 4]))
    print(count_min_jumps_btmup([1, 1, 3, 6, 9, 3, 0, 1, 3]))

main()
