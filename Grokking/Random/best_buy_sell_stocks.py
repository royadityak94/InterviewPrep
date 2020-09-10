# Best time to buy, sell stocks: Given an array of integers where the ith integer represents the price of the stock on day i, return the largest possible profit from completing one transaction
# prices = [1, 2, 3, 4, 5], return 4. Buy on day 1 and sell on day 5 for a profit of 5 - 1 = 4.
# prices = [4, 5, 2, 1, 6, 10, 4, 9, 11], return 10. Buy on day 4 and sell on day 9 for a profit of 11 - 1 = 10.
# prices = [33, 18, 8, 2], return 0

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def return_max_profit(prices):
    # Time Complexity: O(N), Space Complexity: O(1)
    minimum_price = min(prices)
    minimum_price_idx = prices.index(minimum_price)+1
    max_profit = 0
    for idx in range(minimum_price_idx, len(prices)):
        max_profit = max(max_profit, prices[idx]-minimum_price)
    return max_profit

def main():
    test(5, return_max_profit([1, 1, 2, 3, 4, 5, 5, 6]), "Test - 1")
    test(10, return_max_profit([4, 5, 2, 1, 6, 10, 4, 9, 11]), "Test - 2")
    test(0, return_max_profit([33, 18, 8, 2]), "Test - 2")

main()
