'''
Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.
'''

def count_ways_btmup(n):
    # Time: O(N), Space: O(N)
    dp = [0 for _ in range(n+1)]
    dp[:4] = [1, 1, 1, 2]

    for idx in range(4, n+1):
        dp[idx] = dp[idx-1] + dp[idx-3] + dp[idx-4]
    return dp[-1]

def main():
    print(count_ways_btmup(4))
    print(count_ways_btmup(5))
    print(count_ways_btmup(6))

main()
