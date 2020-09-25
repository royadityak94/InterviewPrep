def rotate_oned_array(arr, d):
    if d == 0 or len(arr) == 0:
        return arr
    queue = []
    for i in range(0, d):
        queue += arr[i],

    arr = arr[d:]

    while queue:
        arr.append(queue.pop())

    return arr

def rotateClockwise(A, multiple):
    # Time Complexity: O(NM), Space Complexity: O(1)
    if multiple // 90 < 1:
        return
    # Transpose - Reverse : Everytime for 90 degree gain
    while multiple // 90 >= 1:
        A = list(zip(*A[::-1]))
        multiple = multiple//90

    return A

def transpose (A):
    row, col = len(A), len(A[0])
    for i in range(row):
        for j in range(i, col):
            A[i][j], A[j][i] = A[j][i], A[i][j]

def reverse(A):
    col = len(A[0])
    for i in range(col):
        j, k = 0, col-1
        while j < k:
            A[i][j], A[i][k] = A[i][k], A[i][j]
            j += 1
            k -= 1

def rotate90Clockwise(A):
    # Transpose - Reverse : Everytime for 90 degree gain
    # Time Complexity: O(NM), Space Complexity: O(1)
    transpose (A)
    reverse(A)
    return A


if __name__ == '__main__':
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print ("1", rotate90Clockwise(arr))

    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print ("3:", rotateClockwise(arr, 90))


    print (rotate_oned_array([1, 2, 3, 4, 5, 6, 7], 4))
