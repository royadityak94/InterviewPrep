# Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.

def solve_staircase(steps):
    # Time Complexity: O(3^N), Space Complexity: O(N)
    if steps == 0:
        return 1
    elif steps == 1:
        return 1
    elif steps == 2:
        return 2

    return solve_staircase(steps-1) + solve_staircase(steps-2) + solve_staircase(steps-3)

def solve_staircase_dp (steps):
    # Time Complexity: O(N), Space Complexity: O(N)
    if steps == 0:
        return 1
    elif steps == 1:
        return 1
    elif steps == 2:
        return 2

    dp = [0 for _ in range(steps+1)]
    dp[0] = dp[1] = 1
    dp[2] = 2

    if not dp[steps]:
        dp[steps] = solve_staircase_dp(steps-1) + solve_staircase_dp(steps-2) + solve_staircase_dp(steps-3)
    return dp[steps]

def solve_staircase_bottomup_dp(steps):
    # Time Complexity: O(N), Space Complexity: O(N)

    dp = [0 for _ in range(steps+1)]
    dp[0] = dp[1] = 1
    dp[2] = 2

    for i in range(3, steps+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[steps]

def solve_staircase_simple(steps):
    # Time Complexity: O(N), Space Complexity: O(1)
    a = b = 1
    c = 2
    for i in range(3, steps+1):
        c, b, a  = a + b + c, c, b
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
