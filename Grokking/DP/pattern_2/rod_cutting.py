# Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that will maximize the profit. We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.

def max_price_from_rod(lengths, price, capacity):
    if capacity <= 0 or len(lengths) == 0 or len(lengths) != len(price):
        return []
    return max_price_from_rod_recursive(lengths, price, capacity, 0)

def max_price_from_rod_recursive(lengths, price, capacity, currentIndex):
    # Time Complexity = Space Complexity: O(2^(N+C))
    if capacity == 0:
        return 0
    if currentIndex >= len(lengths):
        return 0

    with_current = without_current = 0
    if lengths[currentIndex] <= capacity:
        with_current = price[currentIndex] + max_price_from_rod_recursive(lengths, price, capacity-lengths[currentIndex], currentIndex)
    without_current = max_price_from_rod_recursive(lengths, price, capacity, currentIndex+1)
    return max(with_current, without_current)

def max_price_from_rod_td_dp(lengths, price, capacity):
    if capacity <= 0 or len(lengths) == 0 or len(lengths) != len(price):
        return []
    dp = [[-1 for _ in range(capacity+1)] for _ in lengths]
    return max_price_from_rod_td_dp_recursive(dp, lengths, price, capacity, 0)

def max_price_from_rod_td_dp_recursive(dp, lengths, price, capacity, currentIndex):
    if capacity == 0 or currentIndex >= len(lengths):
        return 0

    if dp[currentIndex][capacity] == -1:
        with_current = without_current = 0
        if lengths[currentIndex] <= capacity:
            with_current = price[currentIndex] + max_price_from_rod_td_dp_recursive(dp, lengths, price, capacity-lengths[currentIndex], currentIndex)
        without_current = max_price_from_rod_td_dp_recursive(dp, lengths, price, capacity, currentIndex+1)

        dp[currentIndex][capacity] = max(with_current, without_current)

    return dp[currentIndex][capacity]

def max_price_from_rod_btmup_dp(lengths, price, capacity):
    # Space Complexity = Time Complexity = O(NC), N: Total Items, C: Maximum Capacity
    if capacity <= 0 or len(lengths) == 0 or len(lengths) != len(price):
        return []

    dp = [[-1 for _ in range(capacity+1)] for _ in lengths]

    # Populating column = 0, profit = 0 when length = 0
    for r in range(len(lengths)):
        dp[r][0] = 0

    # Populating row = 0, i.e. profit = price[0] when lengths <= c ([0, capacity+1])
    for c in range(capacity+1):
        if lengths[0] <= c:
            dp[0][c] = price[0]

    # Populating other subsets, i.e. all rod lengths for all prices
    for r in range(1, len(lengths)):
        for c in range(1, capacity+1):
            with_current = without_current = 0
            if lengths[r] <= c:
                with_current = price[r] + dp[r][c-lengths[r]]
            without_current = dp[r-1][c]
            dp[r][c] = max(with_current, without_current)

    return dp[len(lengths)-1][capacity]

def main():
    # Using simple recursion
    print (max_price_from_rod([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
    print (max_price_from_rod([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 12))

    # Using top-down recursion
    print (max_price_from_rod_td_dp([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
    print (max_price_from_rod_td_dp([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 12))

    # Using bottom-up recursion
    print (max_price_from_rod_btmup_dp([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
    print (max_price_from_rod_btmup_dp([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 12))

main()
