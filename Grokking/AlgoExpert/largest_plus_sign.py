'''
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0. An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s.
'''
from typing import List

# O(N^3) time | O(N) space
def orderOfLargestPlusSign_naive(N:int, mines: List[List[int]]) -> int:
    mines = {tuple(mine) for mine in mines}
    maxOrder = float('-inf')

    for r in range(N):
        for c in range(N):
            k = 0
            while (k <= r < N-k) and (k <= c < N-k) \
                and (r-k, c) not in mines \
                and (r+k, c) not in mines \
                and (r, c-k) not in mines \
                and (r, c+k) not in mines:
                k += 1
            maxOrder = max(maxOrder, k)
    return maxOrder

# O(N^2) time | O(N) space
def orderOfLargestPlusSign(N:int, mines: List[List[int]]) -> int:
    mines = {tuple(mine) for mine in mines}
    maxOrder = float('-inf')
    dp = [[0]*N for _ in range(N)]

    for r in range(N):
        count = 0
        for c in range(N):
            count = count+1 if (r, c) not in mines else 0
            dp[r][c] = count
        count = 0
        for c in range(N-1, -1, -1):
            count = count+1 if (r, c) not in mines else 0
            dp[r][c] = min(dp[r][c], count)

    for c in range(N):
        count = 0
        for r in range(N):
            count = count+1 if (r, c) not in mines else 0
            dp[r][c] = min(dp[r][c], count)

        for r in range(N-1, -1, -1):
            count = count+1 if (r, c) not in mines else 0
            dp[r][c] = min(dp[r][c], count)
            maxOrder = max(maxOrder, dp[r][c])
    return maxOrder





if __name__ == '__main__':
    # Naive Implementations
    assert orderOfLargestPlusSign_naive(5, [[4, 2]]) == 2
    assert orderOfLargestPlusSign_naive(2, []) == 1
    assert orderOfLargestPlusSign_naive(1, [[0, 0]]) == 0

    # Optimized Implementations = DP
    assert orderOfLargestPlusSign(5, [[4, 2]]) == 2
    assert orderOfLargestPlusSign(2, []) == 1
    assert orderOfLargestPlusSign(1, [[0, 0]]) == 0
