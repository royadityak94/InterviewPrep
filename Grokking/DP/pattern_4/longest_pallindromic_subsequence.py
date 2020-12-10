'''Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence,
elements read the same backward and forward. A subsequence is a sequence that can be derived from another
sequence by deleting some or no elements without changing the order of the remaining elements.
Ex: Inp('abdbca'), O/p: 5 ('abdba')
Ex: Inp('cddpd'), O/p: 3 ('ddd')
Ex: Inp('pqr'), O/p: 1 ('p'/'q'/'r')
'''
from unittest import TestCase, main

def find_longest_pallindromic_subseq(string):
    # Time:  O(2 ^ N), Space: O(N)
    return find_longest_pallindromic_subseq_recursive(string, 0, len(string)-1)

def find_longest_pallindromic_subseq_recursive(string, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    # case 1: when char at both end are equal
    if string[startIdx] == string[endIdx]:
        return 2 + find_longest_pallindromic_subseq_recursive(string, startIdx+1, endIdx-1)

    # case 2: when char at both end are at a mismatch
    c1 = find_longest_pallindromic_subseq_recursive(string, startIdx+1, endIdx)
    c2 = find_longest_pallindromic_subseq_recursive(string, startIdx, endIdx-1)
    return max(c1, c2)

def find_longest_pallindromic_subseq_td(string):
    # Time:  O(2 ^ N), Space: O(N^2 + N) ~ O(N)
    N = len(string)
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    return find_longest_pallindromic_subseq_td_recursive(dp, string, 0, N-1)

def find_longest_pallindromic_subseq_td_recursive(dp, string, startIdx, endIdx):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if not (dp[startIdx][endIdx]+1):
        # case 1: when char at both end are equal
        if string[startIdx] == string[endIdx]:
            dp[startIdx][endIdx] = 2 +  find_longest_pallindromic_subseq_td_recursive(dp, string, startIdx+1, endIdx-1)
        # case 2: when char at both end are at a mismatch
        else:
            c1 = find_longest_pallindromic_subseq_td_recursive(dp, string, startIdx+1, endIdx)
            c2 = find_longest_pallindromic_subseq_td_recursive(dp, string, startIdx, endIdx-1)
            dp[startIdx][endIdx] = max(c1, c2)
    return dp[startIdx][endIdx]

def find_longest_pallindromic_subseq_btmup(string):
    # Time:  O(2 ^ N), Space: O(N^2)
    N = len(string)
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # every sequence with one element is a palindrome of length 1
    for i in range(N):
        dp[i][i] = 1


    for startIdx in range(N-1, -1, -1):
        for endIdx in range(startIdx+1, N):
            if string[startIdx] == string[endIdx]:
                # case 1: when char at both end are equal
                dp[startIdx][endIdx] = 2 + dp[startIdx+1][endIdx-1]
            else:
                # case 2: when char at both end are at a mismatch
                dp[startIdx][endIdx] = max(dp[startIdx+1][endIdx], dp[startIdx][endIdx-1])
    return dp[0][N-1]

class Test(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(find_longest_pallindromic_subseq('abdbca'), 5)
        self.assertEqual(find_longest_pallindromic_subseq_td('abdbca'), 5)
        self.assertEqual(find_longest_pallindromic_subseq_btmup('abdbca'), 5)
    def test_2(self):
        self.assertEqual(find_longest_pallindromic_subseq('cddpd'), 3)
        self.assertEqual(find_longest_pallindromic_subseq_td('cddpd'), 3)
        self.assertEqual(find_longest_pallindromic_subseq_btmup('cddpd'), 3)
    def test_3(self):
        self.assertEqual(find_longest_pallindromic_subseq('pqr'), 1)
        self.assertEqual(find_longest_pallindromic_subseq_td('pqr'), 1)
        self.assertEqual(find_longest_pallindromic_subseq_btmup('pqr'), 1)

if __name__ == '__main__':
    main()
