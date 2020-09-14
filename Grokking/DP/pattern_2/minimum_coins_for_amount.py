# Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the minimum number of coins needed to make up that amount.

def minimum_coins_to_make_amount(arr, amount):
    if amount == 0 or len(arr) == 0:
        return 0
    return minimum_coins_to_make_amount_recursive(arr, amount, 0)

def minimum_coins_to_make_amount_recursive(arr, amount, currentIndex):
    # Space Complexity = Time Complexity = O(2^(len(arr)+amount))
    if amount == 0:
        return 0

    if currentIndex >= len(arr):
        return float('inf')

    with_current = without_current = float('inf')
    if arr[currentIndex] <= amount:
        resultant = minimum_coins_to_make_amount_recursive(arr, amount-arr[currentIndex], currentIndex)
        if resultant != float('inf'):
            with_current = resultant + 1
    without_current = minimum_coins_to_make_amount_recursive(arr, amount, currentIndex+1)
    return min(with_current, without_current)

def minimum_coins_to_make_amount_td(arr, amount):
    if amount == 0 or len(arr) == 0:
        return 0
    td = [[0 for _ in range(amount+1)] for _ in arr]
    return minimum_coins_to_make_amount_td_recursive(td, arr, amount, 0)

def minimum_coins_to_make_amount_td_recursive(td, arr, amount, currentIndex):
    if amount == 0:
        return 0
    if currentIndex >= len(arr):
        return float('inf')

    if td[currentIndex][amount] == 0:
        with_current = without_current = float('inf')
        if arr[currentIndex] <= amount:
            resultant = minimum_coins_to_make_amount_td_recursive(td, arr, amount-arr[currentIndex], currentIndex)
            if resultant < float('inf'):
                with_current = resultant + 1
        without_current = minimum_coins_to_make_amount_td_recursive(td, arr, amount, currentIndex+1)
        td[currentIndex][amount] = min(with_current, without_current)
    return td[currentIndex][amount]

def minimum_coins_to_make_amount_dp(arr, amount):
    if amount == 0 or len(arr) == 0:
        return 0

    dp = [[float('inf') for _ in range(amount+1)] for _ in arr]

    # Populating 0th row, i.e. when amount = 0, possible combinations = 0
    for i in range(len(arr)):
        dp[i][0] = 0

    # Populating 0th column, i.e. possible combination when respective column
    # value [0, amount+1] is less than the amount
    for c in range(1, amount+1):
        if arr[0] <= c:
            if dp[0][c-arr[0]] < float('inf'):
                dp[0][c] = min(dp[0][c], dp[0][c-arr[0]]+1)

    # Populating all combinations of amount and coin denominations
    for i in range(1, len(arr)):
        for c in range(1, amount+1):
            dp[i][c] = dp[i-1][c]
            if arr[i] <= c:
                if dp[i][c-arr[i]] < float('inf'):
                    dp[i][c] = min(dp[i][c], dp[i][c-arr[i]]+1)


    if dp[len(arr)-1][amount] < float('inf'):
        return dp[len(arr)-1][amount]
    else:
        return -1

def main():
    # using simple recursion
    print(minimum_coins_to_make_amount([1, 2, 3], 5))
    # using top-down DP
    print(minimum_coins_to_make_amount_td([1, 2, 3], 5))
    # using bottom-up DP
    print(minimum_coins_to_make_amount_dp([1, 2, 3], 5))

main()
