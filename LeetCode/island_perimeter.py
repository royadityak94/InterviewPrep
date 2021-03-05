''' Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''
from collections import deque
from typing import List

# O(mn) time  | O(1) space
def islandPerimeter(grid: List[List[int]]) -> int:
    if not grid or not len(grid[0]):
        return 0
    m, n = len(grid), len(grid[0])
    queue = deque()
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    total_perimeter = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue += (i, j),
                while queue:
                    prev = total_perimeter
                    x, y = queue.popleft()
                    if grid[x][y] == 2:
                        continue
                    grid[x][y] = 2
                    total_perimeter += 4
                    # Check if left is island
                    if y-1 >= 0 and grid[x][y-1] > 0:
                        total_perimeter -= 2
                    # Check if right is island
                    if x - 1 >= 0 and grid[x-1][y] > 0:
                        total_perimeter -= 2

                    for ngh_x, ngh_y in neighbors:
                        _x = x + ngh_x
                        _y = y + ngh_y
                        if _x in range(m) and _y in range(n) and grid[_x][_y] == 1:
                            queue += (_x, _y),
    return total_perimeter

if __name__ == '__main__':
    grid1 = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    grid2 = [[1]]
    grid3 = [[1,0]]
    grid4 = [[1,1,0], [1,1,1]]
    assert islandPerimeter(grid1) == 16
    assert islandPerimeter(grid2) == 4
    assert islandPerimeter(grid3) == 4
    assert islandPerimeter(grid4) == 10
