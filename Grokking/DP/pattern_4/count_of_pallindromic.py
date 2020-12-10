'''
Given a string, find the total number of palindromic substrings in it. Please note we need to find the
total number of substrings and not subsequences.
Ip("abdbca") => 7, {"a", "b", "d", "b", "c", "a", "bdb"}
Ip("cddpd") => 7, {"c", "d", "d", "p", "d", "dd", "dpd"}
Ip("pqr") => 3, {"p", "q", "r"}

Similar Problems: Minimum String insertions to make it pallindromic, check if a string is K-Palindromic
'''
from unittest import TestCase, main

def count_pallindromes_btmup(string):
    # Time: O(N^2) | Space: O(N^2)
    N = len(string)
    dp = [[False for _ in range(N)] for _ in range(N)]

    pallindromes_cnt = 0
    # counting the single length string
    for i in range(N):
        dp[i][i] = True
        pallindromes_cnt += 1

    for startIdx in range(N-1, -1, -1):
        for endIdx in range(startIdx+1, N):
            if string[startIdx] == string[endIdx]:
                if (endIdx == startIdx + 1) or dp[startIdx+1][endIdx-1]:
                    pallindromes_cnt += 1
                    dp[startIdx][endIdx] = True
    return pallindromes_cnt

class Test(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(count_pallindromes_btmup('abdbca'), 7)
    def test_2(self):
        self.assertEqual(count_pallindromes_btmup('cddpd'), 7)
    def test_3(self):
        self.assertEqual(count_pallindromes_btmup('pqr'), 3)

if __name__ == '__main__':
    main()
