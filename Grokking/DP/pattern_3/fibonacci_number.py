# Write a function to calculate the nth Fibonacci number.

def calculate_nth_fibonacci(n):
    # Time Complexity: O(2^N), Space Complexity: O(N)
    if n < 2:
        return n
    return calculate_nth_fibonacci(n-1) + calculate_nth_fibonacci(n-2)

def calculate_nth_fibonacci_dp(n):
    dp = [0 for _ in range(n+1)]
    return recursive_dp(dp, n)

def recursive_dp(dp, n):
    # Time Complexity: O(2^N), Space Complexity: O(N)
    if n < 2:
        return n
    if not dp[n]:
        dp[n] = recursive_dp(dp, n-1) + recursive_dp(dp, n-2)
    return dp[n]

def calculate_nth_fibonacci_bottom_up_dp(n):
    # Time Complexity = O(n), Space Complexity: O(n)
    if n < 2:
        return n

    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def calculate_nth_fibonacci_space_optimized(n):
    # Time Complexity = O(n), Space Complexity: O(1)
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        b, a = a + b, b
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
