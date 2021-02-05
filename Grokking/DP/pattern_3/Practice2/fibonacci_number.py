# Write a function to calculate the nth Fibonacci number.

# O(2^n) time | O(n) space
def calculate_nth_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_nth_fibonacci(n-1) + calculate_nth_fibonacci(n-2)

def calculate_nth_fibonacci_dp(n):
    dp = [-1 for _ in range(n+1)]
    return calculate_nth_fibonacci_dp_recursive(dp, n)

# O(n) time | O(n) space
def calculate_nth_fibonacci_dp_recursive(dp, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if dp[n] == -1:
        dp[n] = calculate_nth_fibonacci(n-1) + calculate_nth_fibonacci(n-2)
    return dp[n]

# O(n) time | O(n) space
def calculate_nth_fibonacci_bottom_up_dp(n):
    dp = [-1 for _ in range(n+1)]
    dp[:2] = [0, 1]

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# O(n) time | O(1) space
def calculate_nth_fibonacci_space_optimized(n):
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b

def main():
    # Using simple recursion
    print (calculate_nth_fibonacci(7))
    print (calculate_nth_fibonacci(12))

    # Using memoization - top-down dp
    print (calculate_nth_fibonacci_dp(7))
    print (calculate_nth_fibonacci_dp(12))

    # Using bottom-up dp
    print (calculate_nth_fibonacci_bottom_up_dp(7))
    print (calculate_nth_fibonacci_bottom_up_dp(12))

    # back to school - O(1) approach
    print (calculate_nth_fibonacci_space_optimized(7))
    print (calculate_nth_fibonacci_space_optimized(12))

main()
