'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''
from typing import List

''' Naive Approach:
Trivially we can enumerate every possible rectangle. This is done by iterating over all possible combinations of coordinates (x1, y1) and (x2, y2) and letting them define a rectangle with the coordinates being opposite corners. This is too slow to pass all test cases.

Complexity Analysis
-----------
Time complexity : O(N^3M^3) with N being the number of rows and M the number of columns (Iterating over all possible coordinates is O(N^2M^2), and iterating over the rectangle defined by two coordinates is an additional O(NM)O(NM). O(NM) * O(N^2M^2)).
Space complexity : O(1)O(1).
'''
from typing import List

def compute_max_histogram(heights: List[int]) -> int:
    m = len(heights)
    stack = [-1]
    maxArea = 0
    for i in range(m):
        while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
            currHeight = heights[stack.pop()]
            currWidth = i - stack[-1] - 1
            maxArea = max(maxArea, currHeight * currWidth)
        stack += i,

    while stack[-1] != -1:
        currHeight = heights[stack.pop()]
        currWidth = m - stack[-1] - 1
        maxArea = max(maxArea, currHeight * currWidth)
    return maxArea



def maximalRectangle(matrix: List[int]) -> int:
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    maxArea = 0
    dp = [0 for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                dp[j] = 1 + dp[j]
            else:
                dp[j] = 0
        maxArea = max(maxArea, compute_max_histogram(dp))
    return maxArea



if __name__ == '__main__':
    matrix1 = [["1","0","1","0","0"], ["1","0","1","1","1"], ["1","1","1","1","1"], ["1","0","0","1","0"]]
    matrix2 = []
    matrix3 = [["1", "1"]]
    matrix4 = [["1"]]
    matrix5 = [["0","0"], ["1", "1"]]

    assert maximalRectangle(matrix1) == 6
    assert maximalRectangle(matrix2) == 0
    assert maximalRectangle(matrix3) == 2
    assert maximalRectangle(matrix4) == 1
    assert maximalRectangle(matrix5) == 2
