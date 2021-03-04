''' Game of Life
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
'''
from typing import List
from copy import deepcopy

def get_live_neighbors(board, row, col):
    m, n = len(board), len(board[0])
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    live_neighbors = 0
    for ngh_x, ngh_y in neighbors:
        _r, _c = row + ngh_x, col + ngh_y
        if _r in range(m) and _c in range(n) and abs(board[_r][_c]) == 1:
            live_neighbors += 1
    return live_neighbors

# O(mn) time | O(mn) space
def gameOfLife_naive(board: List[List[int]]) -> List[List[int]]:
    if not board or not len(board[0]):
        return board
    m, n = len(board), len(board[0])
    cBoard = deepcopy(board)


    for i in range(m):
        for j in range(n):
            live_neighbors = get_live_neighbors(cBoard, i, j)

            # Case 1/3
            if cBoard[i][j] == 1 and  not live_neighbors in range(2, 4):
                board[i][j] = 0
            # Case 4
            if cBoard[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 1
    return board

# O(mn) time | O(1) space
def gameOfLife_space_optimized(board: List[List[int]]) -> List[List[int]]:
    if not board or not len(board[0]):
        return board
    m, n = len(board), len(board[0])

    for i in range(m):
        for j in range(n):
            live_neighbors = get_live_neighbors(board, i, j)
            # Case 1/3
            if board[i][j] == 1 and  not live_neighbors in range(2, 4):
                board[i][j] = -1
            # Case 4
            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 2

    for i in range(m):
        for j in range(n):
            if board[i][j] > 0:
                board[i][j] = 1
            else:
                board[i][j] = 0
    return board




if __name__ == '__main__':
    board1 = [[0,1,0], [0,0,1], [1,1,1], [0,0,0]]
    output1 = [[0,0,0], [1,0,1], [0,1,1], [0,1,0]]
    board2 = [[1,1], [1,0]]
    output2 = [[1,1], [1,1]]
    # Naive approach
    assert gameOfLife_naive(deepcopy(board1)) == output1
    assert gameOfLife_naive(deepcopy(board2)) == output2

    # space optimized
    assert gameOfLife_space_optimized(deepcopy(board1)) == output1
    assert gameOfLife_space_optimized(deepcopy(board2)) == output2
