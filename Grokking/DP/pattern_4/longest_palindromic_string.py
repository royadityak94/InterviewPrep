'''
    Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.
    I/p('abdbca') -> 3, 'bdb'
    I/p('cddpd') -> 3, 'dpd'
    I/p('pqr') -> 1, 'p'|'q'|'r'
'''
from unittest import TestCase, main

def find_LPS_length(string):
    # Time: O(3^N), Space: O(N)
    return find_LPS_length_recursive(string, 0, len(string)-1)

def find_LPS_length_recursive(string, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if string[startIdx] == string[endIdx]:
        # case 1: when chars at both end are the same
        remaining = endIdx - startIdx - 1
        if remaining == find_LPS_length_recursive(string, startIdx+1, endIdx-1):
            return remaining+2

    # case 2: when chars at both end are unequal
    c1 =  find_LPS_length_recursive(string, startIdx+1, endIdx)
    c2 = find_LPS_length_recursive(string, startIdx, endIdx-1)
    return max(c1, c2)

def find_LPS_length_td(string):
    # Time: O(N^2), Space: O(N^2 + N) ~ O(N)
    N = len(string)
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    return find_LPS_length_td_recursive(dp, string, 0, N-1)

def find_LPS_length_td_recursive(dp, string, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if not (dp[startIdx][endIdx]+1):
        if string[startIdx] == string[endIdx]:
             # case 1: when chars at both end are the same
             remaining = endIdx - startIdx - 1
             if remaining == find_LPS_length_td_recursive(dp, string, startIdx+1, endIdx-1):
                 dp[startIdx][endIdx] = remaining + 2
                 return dp[startIdx][endIdx]
        # case 2: when chars at both end are unequal
        c1 =  find_LPS_length_td_recursive(dp, string, startIdx+1, endIdx)
        c2 = find_LPS_length_td_recursive(dp, string, startIdx, endIdx-1)
        dp[startIdx][endIdx] = max(c1, c2)
    return dp[startIdx][endIdx]

def find_LPS_length_btmup(string):
    # Time: O(N^2), Space: O(N^2)
    N = len(string)
    dp = [[False for _ in range(N)] for _ in range(N)]

    # Single-length strings are palindromic
    for i in range(N):
        dp[i][i] = True

    maxLength = 1
    for startIdx in range(N-1, -1, -1):
        for endIdx in range(startIdx+1, N):
            if string[startIdx] == string[endIdx]:
                # case 1: when chars at both end are the same
                if (endIdx == startIdx + 1) or dp[startIdx+1][endIdx-1]:
                    dp[startIdx][endIdx] = True
                    maxLength = max(maxLength, endIdx-startIdx+1)
    return maxLength

class Test(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(find_LPS_length('abdbca'), 3)
        self.assertEqual(find_LPS_length_td('abdbca'), 3)
        self.assertEqual(find_LPS_length_btmup('abdbca'), 3)
    def test_2(self):
        self.assertEqual(find_LPS_length('cddpd'), 3)
        self.assertEqual(find_LPS_length_td('cddpd'), 3)
        self.assertEqual(find_LPS_length_btmup('cddpd'), 3)
    def test_3(self):
        self.assertEqual(find_LPS_length('pqr'), 1)
        self.assertEqual(find_LPS_length_td('pqr'), 1)
        self.assertEqual(find_LPS_length_btmup('pqr'), 1)


if __name__ == '__main__':
    main()
