''' Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''
from typing import List

def largestRectangleArea_naive(heights: List[int]) -> int:
    if not heights:
        return 0
    m = len(heights)
    maxArea = float('-inf')

    for i in range(m):
        minHeight = float('inf')
        for j in range(i, m):
            minHeight = min(minHeight, heights[j])
            maxArea = max(maxArea, minHeight * (j-i+1))
    return maxArea

def largestRectangleArea(heights: List[int]) -> int:
    if not heights:
        return 0
    m = len(heights)
    maxArea = float('-inf')
    stack = [-1]
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

if __name__ == '__main__':
    assert largestRectangleArea([2,1,5,6,2,3]) == largestRectangleArea_naive([2,1,5,6,2,3]) == 10
    assert largestRectangleArea([2, 4]) == largestRectangleArea_naive([2, 4]) == 4
