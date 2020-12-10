'''
    Given a string, we want to cut it into pieces such that each piece is a palindrome.
    Write a function to return the minimum number of cuts needed.
    IP('abdbca') -> 3 ["a", "bdb", "c", "a"]
    IP('cddpd') -> 2 ["c", "d", "dpd"]
    IP('pqr') -> 2 ["p", "q", "r"]
    IP('pp') -> 0 [] (No need to cut 'pp' as it's already pallindrome)
'''
from unittest import TestCase, main

def find_MPP_cuts(string):
    return find_MPP_cuts_recursive(string, 0, len(string)-1)

def find_MPP_cuts_recursive(string, startIdx, endIdx):
    if startIdx >= endIdx or isPallindrome(string, startIdx, endIdx):
        return 0

    minimumCuts = endIdx - startIdx
    for i in range(startIdx, endIdx+1):
        if isPallindrome(string, startIdx, i):
            minimumCuts = min(minimumCuts, 1+find_MPP_cuts_recursive(string, i+1, endIdx))
    return minimumCuts

def isPallindrome(string, x, y):
    while x < y:
        if string[x] != string[y]:
            return False
        x += 1
        y -= 1
    return True

def find_MPP_cuts_td(string):
    N = len(string)
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    dpPartition = [[-1 for _ in range(N)] for _ in range(N)]
    return find_MPP_cuts_td_recursive(dp, dpPartition, string, 0, N-1)

def find_MPP_cuts_td_recursive(dp, dpPartition, string, startIdx, endIdx):
    if startIdx >= endIdx or isPallindromeDp(dpPartition, string, startIdx, endIdx):
        return 0
    if not (dp[startIdx][endIdx]+1):
        minimumCuts = endIdx - startIdx
        for i in range(startIdx, endIdx+1):
            if isPallindromeDp(dpPartition, string, startIdx, i):
                minimumCuts = min(minimumCuts, 1 + find_MPP_cuts_td_recursive(dp, dpPartition, string, i+1, endIdx))
        dp[startIdx][endIdx] = minimumCuts
    return dp[startIdx][endIdx]

def isPallindromeDp(dp, string, x, y):
    if not (dp[x][y]+1):
        dp[x][y] = 1
        i, j = x, y
        while i < j:
            if string[i] != string[j]:
                dp[x][y] = 0
                break
            i += 1
            j -= 1
            if i < j and dp[i][j] != -1:
                dp[x][y] = dp[i][j]
                break
    return True if dp[x][y] == 1 else False

class Test(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(find_MPP_cuts("abdbca"), 3)
        self.assertEqual(find_MPP_cuts_td("abdbca"), 3)
    def test_2(self):
        self.assertEqual(find_MPP_cuts("cdpdd"), 2)
        self.assertEqual(find_MPP_cuts_td("cdpdd"), 2)
    def test_3(self):
        self.assertEqual(find_MPP_cuts("pqr"), 2)
        self.assertEqual(find_MPP_cuts_td("pqr"), 2)
    def test_4(self):
        self.assertEqual(find_MPP_cuts("pp"), 0)
        self.assertEqual(find_MPP_cuts_td("pp"), 0)
    def test_5(self):
        self.assertEqual(find_MPP_cuts("madam"), 0)
        self.assertEqual(find_MPP_cuts_td("madam"), 0)


if __name__ == '__main__':
    main()
