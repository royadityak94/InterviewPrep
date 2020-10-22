# Source: https://www.hackerrank.com/challenges/greedy-florist/problem

def getMinimumCost(k, c):
    c.sort(reverse=True)
    minimum_cost = 0
    mult = 1
    original_k = k

    for price in c:
        minimum_cost += mult*price
        k -= 1
        if not k:
            mult += 1
            k = original_k
    return minimum_cost


if __name__ == '__main__':
    print(getMinimumCost(3, [2, 5, 6]))
    print(getMinimumCost(2, [2, 5, 6]))
    print(getMinimumCost(3, [1, 3, 5, 7, 9]))
    print (getMinimumCost(3, [ 390225,426456,688267,800389,990107,439248,240638,15991,874479,568754,729927,980985,132244,488186,5037,721765,251885,28458,23710,281490,30935,897665,768945,337228,533277,959855,927447,941485,24242,684459,312855,716170,512600,608266,779912,950103,211756,665028,642996,262173,789020,932421,390745,433434,350262,463568,668809,305781,815771,550800]))
