# Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that will maximize the profit. We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.

# O(2^(n+c)) time | O(n+c) space
def max_price_from_rod(lengths, prices, capacity):
    return max_price_from_rod_recursive(lengths, prices, capacity, 0)

def max_price_from_rod_recursive(lengths, prices, capacity, currentIdx):
    if currentIdx == len(lengths):
        return 0
    with_current = 0
    if lengths[currentIdx] <= capacity:
        with_current = prices[currentIdx] + \
        max_price_from_rod_recursive(lengths, prices, capacity-lengths[currentIdx], currentIdx)
    without_current = max_price_from_rod_recursive(lengths, prices, capacity, currentIdx+1)
    return max(with_current, without_current)

# O(nc) time | O(nc) space
def max_price_from_rod_td(lengths, prices, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(lengths))]
    return max_price_from_rod_td_recursive(dp, lengths, prices, capacity, 0)

def max_price_from_rod_td_recursive(dp, lengths, prices, capacity, currentIdx):
    if currentIdx == len(lengths):
        return 0
    if dp[currentIdx][capacity] == -1:
        with_current = 0
        if lengths[currentIdx] <= capacity:
            with_current = prices[currentIdx] + \
            max_price_from_rod_td_recursive(dp, lengths, prices, capacity-lengths[currentIdx], currentIdx)
        without_current = max_price_from_rod_td_recursive(dp, lengths, prices, capacity, currentIdx+1)
        dp[currentIdx][capacity] = max(with_current, without_current)
    return dp[currentIdx][capacity]

# O(nc) time | O(nc) space
def max_price_from_rod_btmup(lengths, prices, capacity):
    n = len(lengths)
    dp = [[-1 for _ in range(capacity+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for j in range(capacity+1):
        if j == lengths[0]:
            dp[0][j] = prices[0]

    for i in range(1, n):
        for j in range(1, capacity+1):
            p1 = 0
            if j >= lengths[i]:
                p1 = dp[i][j-lengths[i]] + prices[i]
            p2 = dp[i-1][j]
            dp[i][j] = max(p1, p2)
    return dp[n-1][capacity]


def main():
    # Using simple recursion
    print (max_price_from_rod([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
    print (max_price_from_rod([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 12))

    # Using top-down recursion
    print (max_price_from_rod_td([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
    print (max_price_from_rod_td([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 12))

    # Using bottom-up recursion
    print (max_price_from_rod_btmup([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
    print (max_price_from_rod_btmup([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 12))

main()
