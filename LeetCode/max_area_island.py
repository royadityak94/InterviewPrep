''' Max Area of Island
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
'''
from typing import List
from collections import deque

# O(nm) time | O(nm) space
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    if not grid or not len(grid[0]):
        return 0
    m, n = len(grid), len(grid[0])
    maxIslandSize = float('-inf')
    neighbors = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    queue = deque()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue += (i, j),
                currIslandSize = 0


                while queue:
                    x, y = queue.popleft()
                    grid[x][y] = 2
                    currIslandSize += 1
                    for ngh_x, ngh_y in neighbors:
                        _x, _y = x + ngh_x, y + ngh_y
                        if _x in range(m) and _y in range(n) and grid[_x][_y] == 1:
                            queue += (_x, _y),
                maxIslandSize = max(maxIslandSize, currIslandSize)
    return maxIslandSize if maxIslandSize > float('-inf') else 0

if __name__ == '__main__':
    matrix1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0], [0,1,0,0,1,1,0,0,1,0,1,0,0], [0,1,0,0,1,1,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    matrix2 = [[0,0,0,0,0,0,0,0]]
    matrix3 = [[0,0,0,0,0,0,0,0], [0,0,0,1,1,0,0,0]]
    # Copy of island count - BFS approach
    assert maxAreaOfIsland(matrix1) == 6
    assert maxAreaOfIsland(matrix2) == 0
    assert maxAreaOfIsland(matrix3) == 2
