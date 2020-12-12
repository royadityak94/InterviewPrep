'''
Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach
the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.
'''

def count_ways_btmup(n):
    # Time: O(N), Space: O(N)
    dp = [0 for _ in range(n+1)]
    dp[:3] = [1, 1, 2]

    for idx in range(3, n+1):
        dp[idx] = dp[idx-1] + dp[idx-2] + dp[idx-3]

    return dp[-1]

def main():
    print(count_ways_btmup(3)) #4
    print(count_ways_btmup(4)) #7
    print(count_ways_btmup(5)) #13


main()
