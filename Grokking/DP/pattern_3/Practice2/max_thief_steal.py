'''
There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses.
 The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert
 the security system. How should the thief maximize his stealing?
'''

def find_max_steal(wealth):
    return find_max_steal_recursive(wealth, 0)

def find_max_steal_recursive(wealth, currentIdx):
    if currentIdx >= len(wealth):
        return 0
    with_current = wealth[currentIdx] + find_max_steal_recursive(wealth, currentIdx+2)
    without_current = find_max_steal_recursive(wealth, currentIdx+1)
    return max(with_current, without_current)

def find_max_steal_td(wealth):
    dp = [-1 for _ in range(len(wealth))]
    return find_max_steal_td_recursive(dp, wealth, 0)

def find_max_steal_td_recursive(dp, wealth, currentIdx):
    if currentIdx >= len(wealth):
        return 0
    if dp[currentIdx] == -1:
        with_current = wealth[currentIdx] + find_max_steal_td_recursive(dp, wealth, currentIdx+2)
        without_current = find_max_steal_td_recursive(dp, wealth, currentIdx+1)
        dp[currentIdx] = max(with_current, without_current)
    return dp[currentIdx]

def find_max_steal_btmup(wealth):
    n = len(wealth)
    dp = [0 for _ in range(n+1)]
    dp[:2] = [0, wealth[0]]

    for i in range(1, n):
        dp[i+1] = max(wealth[i]+dp[i-1], dp[i])
    return dp[n]

if __name__ == '__main__':
    # Plain recursion
    print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal([2, 10, 14, 8, 1]))
    # TopDown DP
    print(find_max_steal_td([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_td([2, 10, 14, 8, 1]))
    # Bottomup DP
    print(find_max_steal_btmup([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_btmup([2, 10, 14, 8, 1]))
