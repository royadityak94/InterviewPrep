'''
Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you
take the step. Implement a method to calculate the minimum fee required to reach the top of the staircase
(beyond the top-most step). At every step, you have an option to take either 1 step, 2 steps, or 3 steps.
You should assume that you are standing at the first step.
'''
maxValue = float('inf')

def find_min_fee(fees):
    return find_min_fee_recursive(fees, 0)

def find_min_fee_recursive(fees, currentIdx):
    if currentIdx >= len(fees):
        return 0
    if not fees[currentIdx]:
        return maxValue

    take1step = find_min_fee_recursive(fees, currentIdx+1)
    take2step = find_min_fee_recursive(fees, currentIdx+2)
    take3step = find_min_fee_recursive(fees, currentIdx+3)
    return fees[currentIdx] + min(take1step, take2step, take3step)

def find_min_fee_td(fees):
    dp = [-1 for _ in range(len(fees))]
    return find_min_fee_td_recursive(dp, fees, 0)

def find_min_fee_td_recursive(dp, fees, currentIdx):
    if currentIdx >= len(fees):
        return 0
    if not fees[currentIdx]:
        return maxValue

    if dp[currentIdx] == -1:
        take1step = find_min_fee_td_recursive(dp, fees, currentIdx+1)
        take2step = find_min_fee_td_recursive(dp, fees, currentIdx+2)
        take3step = find_min_fee_td_recursive(dp, fees, currentIdx+3)
        dp[currentIdx] = fees[currentIdx] + min(take1step, take2step, take3step)
    return dp[currentIdx]

def find_min_fee_btmup(fees):
    n = len(fees)
    dp = [-1 for _ in range(n+1)]
    dp[:3] = [0, fees[0], fees[0]]

    for i in range(2, n):
        dp[i+1] = min(fees[i]+dp[i], fees[i-1]+dp[i-1], fees[i-2]+dp[i-2])
    return dp[n]

if __name__ == '__main__':
    # Plain Recursion
    print(find_min_fee([1, 2, 5, 2, 1, 2]))
    print(find_min_fee([2, 3, 4, 5]))
    # TopDown DP
    print(find_min_fee_td([1, 2, 5, 2, 1, 2]))
    print(find_min_fee_td([2, 3, 4, 5]))
    # BottomUp DP
    print(find_min_fee_btmup([1, 2, 5, 2, 1, 2]))
    print(find_min_fee_btmup([2, 3, 4, 5]))
