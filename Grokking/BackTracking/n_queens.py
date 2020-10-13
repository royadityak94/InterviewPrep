# Ref: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/
# Using the presented algorithm to evaluate my backtrack understanding
from typing import List

def compute_occupied_idxes(board):
    N = len(board)
    occupied_row, occupied_col = [], []
    row = 0
    while row < N:
        col = 0
        flag = False
        while col < N:
            if board[row][col]:
                occupied_row += row,
                occupied_col += col,
                row += 1
                col += 1
                flag = True
                break
            col += 1
        if not flag:
            row += 1
    return occupied_row, occupied_col

def is_cell_attacked(x, y, board):
    N = len(board)
    occupied_row, occupied_col = compute_occupied_idxes(board)
    if x in occupied_row or y in occupied_col:
        return True
    for rw_idx, cl_idx in zip(occupied_row, occupied_col):
        if not abs(rw_idx-x)-abs(cl_idx-y):
            return True
    return False

def n_queens(board, N:int, j:int=0) -> List[List[int]]:
    if j >= len(board):
        return True
    for col in range(len(board)):
        if not is_cell_attacked(len(board)-N, col, board):
            board[len(board)-N][col] = 1
            if n_queens(board, N-1, j+1):
                return True
            board[len(board)-N][col] = 0
    return False

if __name__ == '__main__':
    N = 4
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    print ("Is Positioning Possible? : ", n_queens(board, N))
    print (board)
