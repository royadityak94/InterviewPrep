# Python file for implementing LCA and its variants
# Importing the required packages
import unittest
import numpy as np

def lcs_recursion(a, b, i, j):
    ''' Simple recursion based implementation '''
    if i==0 or j==0:
        return 0
    elif a[i-1] == b[j-1]:
        return (1 + lcs_recursion(a, b, i-1, j-1))
    else:
        return (max(
        lcs_recursion(a, b, i-1, j),
        lcs_recursion(a, b, i, j-1)
        ))

def lcs_recursion_mem(a, b, i, j):
    ''' Memoization variant of lcs_recursion '''
    if memoized_table[i, j] == -1:
        if i==0 or j==0:
            memoized_table[i, j] = 0
        elif a[i-1] == b[j-1]:
            memoized_table[i, j] = (1 + lcs_recursion_mem(a, b, i-1, j-1))
        else:
            memoized_table[i, j] = max(
            lcs_recursion_mem(a, b, i-1, j),
            lcs_recursion_mem(a, b, i, j-1)
            )
    return memoized_table[i, j]

def lcs_recursion_dp(a, b, x, y):
    arr = np.zeros((len(a), len(b)))
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i-1] == b[j-1]:
                arr[i, j] = 1 + arr[i-1, j-1]
            else:
                arr[i, j] = max(arr[i-1, j], arr[i, j-1])
    return arr[x-1, y-1]

class Test(unittest.TestCase):
    def test_lcs_recursion(self):
        str1, str2 = 'DYNAMIC PROGRAMMING', 'ALGORITHMS'
        self.assertEqual(lcs_recursion(str1, str2, len(str1), len(str2)), 4)
    def test_lcs_recursion_mem(self):
        str1, str2 = 'DYNAMIC PROGRAMMING', 'ALGORITHMS'
        global memoized_table
        memoized_table = np.ones((len(str1), len(str2)))*-1
        self.assertEqual(lcs_recursion_mem(str1, str2, len(str1)-1, len(str2)-1), 4)
    def test_lcs_recursion_dp(self):
        str1, str2 = 'DYNAMIC PROGRAMMING', 'ALGORITHMS'
        self.assertEqual(lcs_recursion_dp(str1, str2, len(str1), len(str2)), 4)

if __name__ == '__main__':
    unittest.main()
