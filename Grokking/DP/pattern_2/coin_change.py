# Coin Change problem : Similar to Count of Subset Sum
# Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.

def count_subset_coins(coins, amount):
    # Space Complexity = Time Complexity = O(2^(N+C)); N: Total Coins, C: Amount
    return count_subset_coins_recursive(coins, amount, 0)

def count_subset_coins_recursive(coins, amount, currentIndex):
    if amount == 0:
        return 1

    if len(coins) == 0 or currentIndex >= len(coins):
        return 0

    with_current = without_current = 0
    if coins[currentIndex] <= amount:
        with_current = count_subset_coins_recursive(coins, amount-coins[currentIndex], currentIndex)

    without_current = count_subset_coins_recursive(coins, amount, currentIndex+1)
    return (with_current+without_current)

def count_subset_coins_td(coins, amount):
    if len(coins) == 0:
        return 0
    td = [[-1 for _ in range(amount+1)] for _ in coins]
    return count_subset_coins_td_recursive(td, coins, amount, 0)

def count_subset_coins_td_recursive(td, coins, amount, currentIndex):
    if amount <= 0:
        return 1
    if currentIndex >= len(coins):
        return 0

    if td[currentIndex][amount] == -1:
        with_current = without_current = 0
        if coins[currentIndex] <= amount:
            with_current = count_subset_coins_td_recursive(td, coins, amount-coins[currentIndex], currentIndex)

        without_current = count_subset_coins_td_recursive(td, coins, amount, currentIndex+1)
        td[currentIndex][amount] = with_current + without_current
    return td[currentIndex][amount]

def count_subset_coins_bottom_up(coins, amount):
    # Space Complexity = Time Complexity = O(len(Coins)*Amount)
    if len(coins) == 0 or amount <= 0:
        return 0

    td = [[0 for _ in range(amount+1)] for _ in coins]

    # Populating column = 0, i.e., number of ways = 0 when amount = 0
    for r in range(len(coins)):
        td[r][0] = 1

    for c in range(1, amount+1):
        td[0][c] = td[0][c-coins[0]]

    # Populating other subsets, i.e. for all coin and amount combinations
    for r in range(1, len(coins)):
        for c in range(1, amount+1):
            td[r][c] = td[r-1][c]
            if coins[r] <= c:
                td[r][c] += td[r][c - coins[r]]

    return td[len(coins)-1][amount]

def main():
    # usign simple recursion
    print (count_subset_coins([1, 2, 3], 5))
    # using top-down recursion
    print (count_subset_coins_td([1, 2, 3], 5))
    # using bottom-up recursion
    print(count_subset_coins_bottom_up([1, 2, 3], 5))

main()
