'''
Write a function to calculate the nth Fibonacci number
'''

def calculateFibonacci(n):
    # Time: O(N), Space: O(N)
    if n < 2:
        return n
    dp = [0 for _ in range(n+1)]
    dp[:2] = [0, 1]
    for idx in range(2, n+1):
        dp[idx] = dp[idx-1] + dp[idx-2]
    return dp[-1]

if __name__ == '__main__':
    print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
    print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
    print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))
