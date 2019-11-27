def greedy_mm(arr, i, j, m, n, product):
    #print (arr, i, j, m, n, product)
    #Base Case
    if i >= m-1 and j >= m-1:
        return product
    elif i >= m-1 or j >= n-1:
        if i < m-1:
            return greedy_mm(arr, i+1, j, m, n, product * arr[i+1][j])
        elif j < n-1:
            return greedy_mm(arr, i, j+1, m, n, product * arr[i][j+1])
    # Divert one way
    if product * arr[i+1][j] >= product * arr[i][j+1]:
        return greedy_mm(arr, i+1, j, m, n, product * arr[i+1][j])
    else:
        return greedy_mm(arr, i, j+1, m, n, product * arr[i][j+1])

if __name__ == '__main__':
    arr = [[-1, 2, 3], [-4, 5, -6], [-7, -8, 9]]
    val = greedy_mm(arr, 0, 0, len(arr), len(arr[0]), arr[0][0])
    print (val)