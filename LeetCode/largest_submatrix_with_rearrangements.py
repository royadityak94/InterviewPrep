''' Largest Submatrix with Rearrangements
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order. Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

Exactly same logic as: Maximal Rectangle, Histogram w/ largest area
'''
from typing import List

# O(mn*logn) time | O(n) space
def largestSubmatrix(matrix: List[List[int]]) -> int:
    if not matrix or not len(matrix[0]):
        return 0

    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    maxArea = 0

    for r in range(m):
        # Create the histogram representation
        for c in range(n):
            if matrix[r][c] == 1:
                heights[c] += 1
            else:
                heights[c] = 0
        # Sort the histogram, evaluate area
        sortedHistogram = sorted(heights, reverse=True)
        for j, value in enumerate(sorted(heights, reverse=True)):
            maxArea = max(maxArea, value * (j + 1))
    return maxArea

if __name__ == '__main__':
    matrix1 = [[0,0,1], [1,1,1], [1,0,1]]
    matrix2 = [[1,0,1,0,1]]
    matrix3 = [[1,1,0], [1,0,1]]
    matrix4 = [[0,0], [0,0]]
    matrix5 = [[1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1], [1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1], [1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0]]
    assert largestSubmatrix(matrix1) == 4
    assert largestSubmatrix(matrix2) == 3
    assert largestSubmatrix(matrix3) == 2
    assert largestSubmatrix(matrix4) == 0
    assert largestSubmatrix(matrix5) == 40
