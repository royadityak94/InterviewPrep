'''
Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you
take the step. Implement a method to calculate the minimum fee required to reach the top of the staircase
(beyond the top-most step). At every step, you have an option to take either 1 step, 2 steps, or 3 steps.
You should assume that you are standing at the first step.
'''

def find_min_fee_btmup(fee):
    # Time: O(N), Space: O(N)
    N = len(fee)
    dp = [0 for _ in range(N+1)]
    dp[:3] = [0, fee[0], fee[0]]

    for idx in range(2, N):
        dp[idx+1] = min(dp[idx]+fee[idx],
                        dp[idx-1]+fee[idx-1],
                        dp[idx-2]+fee[idx-2])
    return dp[N]

if __name__ == '__main__':
    print(find_min_fee_btmup([1, 2, 5, 2, 1, 2]))
    print(find_min_fee_btmup([2, 3, 4, 5]))
