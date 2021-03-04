'''
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place. A straight forward solution using O(mn) space is probably a bad idea. A simple improvement uses O(m + n) space, but still not the best solution.
'''
from typing import List
from copy import deepcopy

def setZeroes_naive(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not len(matrix[0]):
        return matrix
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
    return matrix

def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not len(matrix[0]):
        return matrix
    m, n = len(matrix), len(matrix[0])
    col0 = False

    for i in range(m):
        if not matrix[i][0]:
            col0 = True
        for j in range(1, n):
            if not matrix[i][j]:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(m)[::-1]:
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0:
            matrix[i][0] = 0
    return matrix

if __name__ == '__main__':
    matrix1 = [[1,1,1], [1,0,1], [1,1,1]]
    expected1 = [[1,0,1], [0,0,0], [1,0,1]]
    matrix2 = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
    expected2 = [[0,0,0,0], [0,4,5,0], [0,3,1,0]]
    assert setZeroes_naive(deepcopy(matrix1)) == expected1
    assert setZeroes_naive(deepcopy(matrix2)) == expected2
    assert setZeroes_naive([[]]) == [[]]

    assert setZeroes(deepcopy(matrix1)) == expected1
    assert setZeroes(deepcopy(matrix2)) == expected2
    assert setZeroes([[]]) == [[]]
