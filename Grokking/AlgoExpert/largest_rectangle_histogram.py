''' Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''
from typing import List

# O(m^2) time | O(1) space
def largestRectangleArea_naive(heights: List[int]) -> int:
    maxArea = 0
    m = len(heights)

    for i in range(m):
        minHeight = float('inf')
        for j in range(i, m):
            minHeight = min(minHeight, heights[j])
            maxArea = max(maxArea, minHeight*(j-i+1))
    return maxArea

# O(m) time | O(m) space
def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    m = len(heights)
    stack = [-1]

    for i in range(m):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            currentHeight = heights[stack.pop()]
            currentWidth = i - stack[-1] - 1
            maxArea = max(maxArea, currentWidth * currentHeight)
        stack += i,

    if stack[-1] != -1:
        currentHeight = heights[stack.pop()]
        currentWidth = m - stack[-1] - 1
        maxArea = max(maxArea, currentWidth * currentHeight)
    return maxArea

if __name__ == '__main__':
    assert largestRectangleArea([2,1,5,6,2,3]) == largestRectangleArea_naive([2,1,5,6,2,3]) == 10
    assert largestRectangleArea([2, 4]) == largestRectangleArea_naive([2, 4]) == 4
