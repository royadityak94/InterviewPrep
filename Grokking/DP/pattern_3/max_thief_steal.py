'''
There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses.
 The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert
 the security system. How should the thief maximize his stealing?
'''

def find_max_steal_btmup(wealth):
    # Time: O(N), Space: O(N)
    if not wealth:
        return 0
    N = len(wealth)
    dp = [0 for _ in range(N+1)]
    dp[:2] = [0, wealth[0]]

    for idx in range(1, N):
        dp[idx+1] = max(wealth[idx]+dp[idx-1], dp[idx])
    return dp[N]


if __name__ == '__main__':
    print(find_max_steal_btmup([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_btmup([2, 10, 14, 8, 1]))
