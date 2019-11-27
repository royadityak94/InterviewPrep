def return_lists(mapped):
    key, value = [], []
    for k in mapped.keys():
        key.append(k)
        value.append(mapped.get(k))
    return key, value

def knapsack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0
    # Current Weight > W
    elif wt[n-1] > W:
        return knapsack(W, wt, val, n-1)
    else:
        return max(
            knapsack(W, wt, val, n-1), 
            val[n-1] + knapsack(W-wt[n-1], wt, val, n-1)
        )

if __name__ == '__main__':
    maxWeight = 5
    items = {1:6, 2:10, 3:12}
    wt, vals = return_lists (items)
    print (knapsack(maxWeight, wt, vals, len(wt)))

# 
# 
# knapsack(items, maxWeight) = 22