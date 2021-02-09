'''Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.

Input matrix
0 1 1 1
0 0 1 1
1 1 1 1  // this row has maximum 1s
0 0 0 0

Output: 2
'''

def index_one_row(row, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if (mid==0 or row[mid-1] == 0) and row[mid] == 1:
            return mid
        elif row[mid] == 1:
            high = mid - 1
        else:
            low = mid + 1
    return float('inf')


def rowWithMax1s(mat):
    if not mat:
        return -1
    row, col = len(mat)-1, len(mat[0])-1
    minJ = min(index_one_row(mat[0], 0, col), col+1)
    selected_idx = 0 if minJ <= col else -1

    for r in range(1, row+1):
        if not minJ:
            break
        if minJ <= col and not mat[r][minJ]:
            continue
        currentJ = index_one_row(mat[r], 0, min(col, minJ))
        if currentJ < minJ:
            minJ = currentJ
            selected_idx = r

    return selected_idx

if __name__ == '__main__':
    mat = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    ]
    print ("Index of row with maximum 1s is", rowWithMax1s(mat))
