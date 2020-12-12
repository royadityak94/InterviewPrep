
def find_min_fee_btmup(fees):
    N = len(fees)
    dp = [0 for _ in range(N+1)]
    dp[:3] = [0, fees[0], fees[0]]
    for idx in range(2, N):
        dp[idx+1] = min(dp[idx]+fees[idx],
                        dp[idx-1]+fees[idx-1],
                        dp[idx-2]+fees[idx-2])
    return dp[-1]

def main():
    print(find_min_fee_btmup([1, 2, 5, 2, 1, 2]))
    print(find_min_fee_btmup([2, 3, 4, 5]))

main()
