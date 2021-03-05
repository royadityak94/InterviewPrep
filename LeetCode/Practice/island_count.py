'''
N.B - Very frequently asked in interviews
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
from typing import List
from collections import deque
from copy import deepcopy

def numIslands_bfs(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not len(matrix[0]):
        return 0

    m, n = len(matrix), len(matrix[0])
    neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    queue = deque()
    islandCount = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                queue += (i, j),
                islandCount += 1

                while queue:
                    x, y = queue.popleft()
                    matrix[x][y] = '2'
                    for ngh_x, ngh_y in neighbors:
                        _x = x + ngh_x
                        _y = y + ngh_y
                        if _x in range(m) and _y in range(n) and matrix[_x][_y] == '1':
                            queue += (_x, _y),
    return islandCount

def numIslands_dfs(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not len(matrix[0]):
        return 0

    m, n = len(matrix), len(matrix[0])
    neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    stack = deque()
    islandCount = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                stack += (i, j),
                islandCount += 1

                while stack:
                    x, y = stack.pop()
                    matrix[x][y] = '2'
                    for ngh_x, ngh_y in neighbors:
                        _x = x + ngh_x
                        _y = y + ngh_y
                        if _x in range(m) and _y in range(n) and matrix[_x][_y] == '1':
                            stack += (_x, _y),
    return islandCount

if __name__ == '__main__':
    matrix1 = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]
    matrix2 = [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
    # BFS - Arguably best
    assert numIslands_bfs(deepcopy(matrix1)) == 1
    assert numIslands_bfs(deepcopy(matrix2)) == 3

    # DFS - Just for practice
    assert numIslands_dfs(deepcopy(matrix1)) == 1
    assert numIslands_dfs(deepcopy(matrix2)) == 3
