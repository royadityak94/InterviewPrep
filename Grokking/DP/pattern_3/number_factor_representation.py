# Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.
# Simple recursion
def count_ways(n):
    # Time Complexity: O(3^N), Space Complexity: O(N)
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2

    return count_ways(n-1) + count_ways(n-3) + count_ways(n-4)

def count_ways_td(n):
    # Time Complexity: O(N), Space Complexity: O(N)
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    dp = [0 for _ in range(n+1)]
    if not dp[n]:
        dp[n] = count_ways_td(n-1) + count_ways_td(n-3) + count_ways_td(n-4)
    return dp[n]

def count_ways_bottom_up(n):
    # Time Complexity = Space Complexity = O(N)
    dp = [0 for _ in range(n+1)]
    dp [0:4] = [1, 1, 1, 2]
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
    return dp[n]

def main():
    # Simple Recursion
    print (count_ways(4))
    print (count_ways(5))
    # Top-down Recursion
    print (count_ways_td(4))
    print (count_ways_td(5))
    # Bottom-up Recursion
    print (count_ways_bottom_up(4))
    print (count_ways_bottom_up(5))

main()
