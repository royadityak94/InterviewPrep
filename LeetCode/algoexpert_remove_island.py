'''Remove Islands
Goal: Remove all '1s' that is not in island with the bordering (row, column)
[[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1]] -> [[1, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1],[0, 0, 0, 0, 1, 0],[1, 1, 0, 0, 1, 0],[1, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 1]]
'''
from typing import List
from collections import deque
import numpy as np


def removeIslands(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not len(matrix[0]):
        return matrix
    m, n = len(matrix), len(matrix[0])
    neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    queue = deque()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                isRowBorder = (i == 0 or i == m-1)
                isColBorder = (j==0 or j == n-1)
                if not (isRowBorder or isColBorder):
                    continue
                queue += (i, j),
                while queue:
                    x, y = queue.popleft()
                    matrix[x][y] = 2
                    for ngh_x, ngh_y in neighbors:
                        _x, _y = x + ngh_x, y + ngh_y
                        if _x in range(m) and _y in range(n) and matrix[_x][_y] == 1:
                            queue += (_x, _y),

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                matrix[i][j] = 1
            elif matrix[i][j] == 1:
                matrix[i][j] = 0
    return matrix

if __name__ == '__main__':
    matrix1 = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1]]
    expected1 = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1]]
    matrix2 = [[1, 1, 1, 1, 1],[1, 0, 0, 0, 1],[1, 0, 0, 0, 1],[1, 0, 0, 0, 1],[1, 0, 1, 0, 1],[1, 0, 1, 0, 1],[1, 0, 1, 1, 1],[1, 0, 1, 0, 1]]
    expected2 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 0, 1, 0, 1]]
    matrix3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    expected3 =  [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    assert removeIslands(matrix1) == expected1
    assert removeIslands(matrix2) == expected2
    assert removeIslands(matrix3) == expected3

    np.testing.assert_array_equal(removeIslands(matrix1), expected1)
    np.testing.assert_array_equal(removeIslands(matrix2), expected2)
    np.testing.assert_array_equal(removeIslands(matrix3), expected3)
