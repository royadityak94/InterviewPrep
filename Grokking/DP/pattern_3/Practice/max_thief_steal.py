'''
There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses.
 The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert
 the security system. How should the thief maximize his stealing?
'''

def find_max_steal(wealths):
    return find_max_steal_recursive(wealths, 0)

def find_max_steal_recursive(wealths, currentIdx):
    if currentIdx >= len(wealths):
        return 0
    takeCurrent = wealths[currentIdx] + find_max_steal_recursive(wealths, currentIdx+2)
    skipCurrent = find_max_steal_recursive(wealths, currentIdx+1)
    return max(takeCurrent, skipCurrent)

def find_max_steal_td(wealths):
    dp = [-1 for _ in range(len(wealths))]
    return find_max_steal_td_recursive(dp, wealths, 0)

def find_max_steal_td_recursive(dp, wealths, currentIdx):
    if currentIdx >= len(wealths):
        return 0
    if dp[currentIdx] == -1:
        takeCurrent = wealths[currentIdx] + find_max_steal_td_recursive(dp, wealths, currentIdx+2)
        skipCurrent = find_max_steal_td_recursive(dp, wealths, currentIdx+1)
        dp[currentIdx] = max(takeCurrent, skipCurrent)
    return dp[currentIdx]

def find_max_steal_btmup(wealths):
    n = len(wealths)
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = wealths[0]

    for i in range(1, n):
        dp[i+1] = max(wealths[i]+dp[i-1], dp[i])
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
