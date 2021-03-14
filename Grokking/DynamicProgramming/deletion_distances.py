'''
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:
By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
'''

def deletion_distances(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        dp[i][0] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# Recursion
def deletion_distances_r(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    return deletion_distances_recursive(dp, str1, str2, 0, 0)

def deletion_distances_recursive(dp, str1, str2, i, j):
    if dp[i][j] == -1:
        if i >= len(str1):
            dp[i][j] = len(str2)-j
        elif j >= len(str2):
            dp[i][j] = len(str1)-i
        else:
            with_current = float('inf')
            if str1[i] == str2[j]:
                with_current = deletion_distances_recursive(dp, str1, str2, i+1, j+1)

            withoutI = deletion_distances_recursive(dp, str1, str2, i+1, j)
            withoutJ = deletion_distances_recursive(dp, str1, str2, i, j+1)
            dp[i][j] = min(with_current, 1 + min(withoutI, withoutJ))
    return dp[i][j]

if __name__ == '__main__':
    assert deletion_distances('dog', 'frog') == 3
    assert deletion_distances('dog', 'dog') == 0
    assert deletion_distances('some', 'sime') == 2
    assert deletion_distances('some', 'thing') == 9
    assert deletion_distances('', '') == 0

    # Using plain Recursion
    assert deletion_distances_r('dog', 'frog') == 3
    assert deletion_distances_r('dog', 'dog') == 0
    assert deletion_distances_r('some', 'sime') == 2
    assert deletion_distances_r('some', 'thing') == 9
    assert deletion_distances_r('', '') == 0
