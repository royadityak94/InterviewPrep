''' Game of Life
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
'''
from typing import List
from copy import deepcopy

def get_live_neighbors(cBoard, r, c):
    rows, cols = len(cBoard), len(cBoard[0])
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    alive_neighbors = 0
    for neighbor in neighbors:
        _r, _c = r + neighbor[0], c + neighbor[1]
        if _r in range(rows) and _c in range(cols) and abs(cBoard[_r][_c]) == 1:
            alive_neighbors += 1
    return alive_neighbors

# O(mn) time | O(mn) space
def gameOfLife_naive(board: List[List[int]]) -> List[List[int]]:
    '''
        Copy the board over, make changes, repeat!
    '''
    if not board or not len(board):
        return board
    rows, cols = len(board), len(board[0])
    cBoard = deepcopy(board)

    for r in range(rows):
        for c in range(cols):
            alive_neighbors = get_live_neighbors(cBoard, r, c)
            # Rule 1/3
            if cBoard[r][c] == 1 and not (alive_neighbors in range(2, 4)):
                board[r][c] = 0
            # Rule 4
            if cBoard[r][c] == 0 and alive_neighbors == 3:
                board[r][c] = 1
    return board

def gameOfLife_space_optimized(board: List[List[int]]) -> List[List[int]]:
    '''
    Represent with two more states:
    -1 : Currently dead, but previously was alive
    2: Currently alive, but previously was dead
    '''
    if not board or not len(board):
        return board
    rows, cols = len(board), len(board[0])

    for r in range(rows):
        for c in range(cols):
            alive_neighbors = get_live_neighbors(board, r, c)
            # Rule 1/3
            if board[r][c] == 1 and not (alive_neighbors in range(2, 4)):
                board[r][c] = -1
            # Rule 4
            if board[r][c] == 0 and alive_neighbors == 3:
                board[r][c] = 2

    for r in range(rows):
        for c in range(cols):
            if board[r][c] > 0:
                board[r][c] = 1
            else:
                board[r][c] = 0
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
