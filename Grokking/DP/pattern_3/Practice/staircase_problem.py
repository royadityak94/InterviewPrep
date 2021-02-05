# Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.

# O(3^n) time | O(n) space
def solve_staircase(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    take1step = solve_staircase(n-1)
    take2step = solve_staircase(n-2)
    take3step = solve_staircase(n-3)
    return take1step + take2step + take3step

def solve_staircase_dp(n):
    dp = [-1 for _ in range(n+1)]
    dp[:3] = [1, 1, 2]
    return solve_staircase_dp_recursive(dp, n)

# O(n) time | O(n) space
def solve_staircase_dp_recursive(dp, n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if dp[n] == -1:
        take1step = solve_staircase(n-1)
        take2step = solve_staircase(n-2)
        take3step = solve_staircase(n-3)
        dp[n] = take1step + take2step + take3step
    return dp[n]

# O(n) time | O(n) space
def solve_staircase_bottomup_dp(n):
    dp = [0 for _ in range(n+1)]
    dp[:3] = [1, 1, 2]

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

# O(n) time | O(1) space
def solve_staircase_simple(n):
    a, b, c = 1, 1, 2
    while n > 2:
        a, b, c = b, c, a + b + c
        n -= 1
    return c


def main():
    # using simple recursion
    print (solve_staircase(13))
    print (solve_staircase(24))

    # using top-down DP
    print (solve_staircase_dp(13))
    print (solve_staircase_dp(24))

    # using bottom-up DP
    print (solve_staircase_bottomup_dp(13))
    print (solve_staircase_bottomup_dp(24))

    # simple
    print (solve_staircase_simple(13))
    print (solve_staircase_simple(24))

main()
