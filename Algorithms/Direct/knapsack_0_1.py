
def knapsack(W, wt, val, n):
    # Base case
    if n == 0 or W == 0:
        return 0
    # current weight greater than max allowed weight
    elif wt[n-1] > W:
        return knapsack(W, wt, val, n-1)
    else: 
        return max(
            knapsack(W, wt, val, n-1), 
            val[n-1] + knapsack(W-wt[n-1], wt, val, n-1)
        )


if __name__ == '__main__':
    val = [60, 100, 120] 
    wt = [10, 20, 30] 
    W = 50
    n = len(val) 
    print (knapsack(W , wt , val , n) )
