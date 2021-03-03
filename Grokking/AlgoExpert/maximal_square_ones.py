'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
'''
from typing import List

# O((mn)^2) time | O(1) space
def maximalSquare_naive(matrix: List[int]) -> int:
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    maxSquareLength = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                currentSquareLength = 1
                zeroNotFound = True
                while (i + currentSquareLength) < m and (j + currentSquareLength) < n and zeroNotFound:
                    for k in range(j, j+currentSquareLength):
                        if matrix[i+currentSquareLength][k] == '0':
                            zeroNotFound = False
                            break
                    for k in range(i, i+currentSquareLength):
                        if matrix[k][j+currentSquareLength] == '0':
                            zeroNotFound = False
                            break
                    if zeroNotFound:
                        currentSquareLength += 1
                maxSquareLength = max(maxSquareLength, currentSquareLength)
    return maxSquareLength * maxSquareLength

# O(mn) time | O(mn) space
def maximalSquare(matrix: List[int]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    maxSquareLength = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                maxSquareLength = max(maxSquareLength, dp[i][j])
    return maxSquareLength * maxSquareLength

# O(mn) time | O(n) space
def maximalSquare_space_optimized(matrix: List[int]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [0 for _ in range(n+1)]
    prev = 0
    maxSquareLength = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            temp = dp[j]
            if matrix[i-1][j-1] == '1':
                dp[j] = 1 + min(dp[j], prev, dp[j-1])
                maxSquareLength = max(maxSquareLength, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return maxSquareLength * maxSquareLength


def largest_histogram_area(heights: List[int]) -> int:
    maxArea = float('-inf')
    m = len(heights)
    stack = [-1]

    for i in range(m):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            currentHeight = heights[stack.pop()]
            currentWidth = i - stack[-1] - 1
            currLength = min(currentHeight, currentWidth) # This line is the only one changed from maximal rectangle!!
            maxArea = max(maxArea, currLength * currLength)
        stack += i,

    if stack[-1] != -1:
        currentHeight = heights[stack.pop()]
        currentWidth = m - stack[-1] - 1
        currLength = min(currentHeight, currentWidth)
        maxArea = max(maxArea, currLength * currLength)
    return maxArea

# O(mn) time | O(n) space
def maximalSquare_histogram(matrix: List[int]) -> int:
    # Evaluating if histogram concept would apply here
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [0] * n
    maximalRectangleArea = float('-inf') # Following the histogram approach as found in maximal rectangle

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                dp[j] = 1 + dp[j]
            else:
                dp[j] = 0
        maximalRectangleArea = max(maximalRectangleArea, largest_histogram_area(dp))
    return maximalRectangleArea


if __name__ == '__main__':
    matrix1 = [["1","0","1","0","0"], ["1","0","1","1","1"], ["1","1","1","1","1"], ["1","0","0","1","0"]]
    matrix2 = [["0","1"],["1","0"]]
    matrix3 = [["0"]]
    matrix4 = [["1"]]
    assert maximalSquare_naive(matrix1) == maximalSquare(matrix1) == maximalSquare_space_optimized(matrix1) == 4
    assert maximalSquare_naive(matrix2) == maximalSquare(matrix2) == maximalSquare_space_optimized(matrix2) == 1
    assert maximalSquare_naive(matrix3) == maximalSquare(matrix3) == maximalSquare_space_optimized(matrix3) == 0
    assert maximalSquare_naive(matrix4) == maximalSquare(matrix4) == maximalSquare_space_optimized(matrix4) == 1

    # Evaluating maximal square using histogram
    assert maximalSquare_histogram(matrix1) == 4
    assert maximalSquare_histogram(matrix2) == 1
    assert maximalSquare_histogram(matrix3) == 0
    assert maximalSquare_histogram(matrix4) == 1
