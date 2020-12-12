
def find_max_steal_btmup(wealth):
    N = len(wealth)
    dp = [0 for _ in range(N+1)]
    dp[:2] = [0, wealth[0]]

    for idx in range(1, N):
        dp[idx+1] = max(dp[idx-1]+wealth[idx], dp[idx])
    return dp[-1]


def main():
    print(find_max_steal_btmup([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_btmup([2, 10, 14, 8, 1]))

main()
