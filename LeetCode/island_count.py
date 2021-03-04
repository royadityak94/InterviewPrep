'''
N.B - Very frequently asked in interviews
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
from typing import List
from collections import deque
from copy import deepcopy

def numIslands_bfs(grid: List[List[str]]) -> List[List[str]]:
    if not grid or not len(grid):
        return 0
    island_cnt = 0
    m, n = len(grid), len(grid[0])
    queue = deque()
    neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                queue += (i, j),
                grid[i][j] = '2'

                while queue:
                    row, col = queue.popleft() # if pop(0) <- DFS
                    for ngh_x, ngh_y in neighbors:
                        _i, _j = row + ngh_x, col + ngh_y
                        if _i in range(m) and _j in range(n) and grid[_i][_j] == '1':
                            queue += (_i, _j),
                            grid[_i][_j] = '2' # Marking as visited, alternately can maintain a set
                island_cnt += 1
    return island_cnt

def traverse_dfs(i, j, grid):
    m, n = len(grid), len(grid[0])
    grid[i][j] = '2'
    neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for ngh_x, ngh_y in neighbors:
        _i, _j = i + ngh_x, j + ngh_y
        if _i in range(m) and  _j in range(n) and grid[_i][_j] == '1':
            traverse_dfs(_i, _j, grid)

def numIslands_dfs(grid: List[List[int]]) -> List[List[int]]:
    if not grid or not len(grid):
        return
    island_cnt = 0
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                traverse_dfs(i, j, grid)
                island_cnt += 1
    return island_cnt

if __name__ == '__main__':
    matrix1 = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]
    matrix2 = [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
    # BFS - Arguably best
    assert numIslands_bfs(deepcopy(matrix1)) == 1
    assert numIslands_bfs(deepcopy(matrix2)) == 3

    # DFS - Just for practice
    assert numIslands_dfs(deepcopy(matrix1)) == 1
    assert numIslands_dfs(deepcopy(matrix2)) == 3
