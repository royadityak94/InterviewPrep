# Source: https://www.algoexpert.io/product
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if not prices or not k:
        return 0
    profits = [[0 for _ in prices] for _ in range(k+1)]
    # Populating row = 0
    for col in range(1, len(prices)):
        if col >= 0:
            profits[0][col] = prices[0]

    for t in range(1, k+1):
        maxThusFar = float('-inf')
        for d in range(1, len(prices)):
            maxThusFar = max(maxThusFar, profits[t-1][d-1]-prices[d-1])
            profits[t][d] = max(profits[t][d-1], maxThusFar+prices[d])

    print (profits)
    return profits[-1][-1]

if __name__ == '__main__':
    prices = [5, 11, 3, 50, 60, 90]
    k = 2
    print (maxProfitWithKTransactions(prices, k))
