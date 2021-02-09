'''
    Source: https://www.geeksforgeeks.org/cost-balance-parantheses/ + Failed Interview
     The task here is to correct the sequence of parenthesis in such a way that it is done in minimum cost. And shifting of parenthesis by over one parentheses costs 1. If the parenthesis can’t be balanced then print -1.

     Input : ()
     Output : 0
     Explanation : Already balanced

     Input : ))((
     Output : 4
     Explanation : Firstly, ) at position 1st goes to the last position, costing 3, so we get )((). Then, ) at position 1st goes to the 2nd position costing 1. So, finally we get ()(). Therefore, the total cost is 4.
'''

def min_cost_balance_parantheses(string):
    openingCount = 0
    closingCount = 0
    for ch in string:
        if ch == '(':
            openingCount += 1
        else:
            closingCount += 1
    if openingCount != closingCount:
        return -1

    dp = [0 for i in range(len(string))]
    minimum_cost = 0
    dp[0] = 1 if string[0] == '(' else -1
    if dp[0] < 0:
        minimum_cost += 1

    for i in range(1, len(string)):
        if string[i] == '(':
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1] - 1
        if dp[i] < 0:
            minimum_cost += abs(dp[i])
    return minimum_cost


if __name__ == '__main__':
    print (min_cost_balance_parantheses('))(('))
