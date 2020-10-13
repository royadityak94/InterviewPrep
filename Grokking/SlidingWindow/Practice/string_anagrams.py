# Given a string and a pattern, find all anagrams of the pattern in the given string.
import unittest
from collections import defaultdict

def find_string_anagrams(str, pattern):
    # Time Complexity: O(N)
    # Space Complexity: O(M), M = len(pattern)
    charMap = defaultdict(int)
    for ch in pattern:
        charMap[ch] += 1
    ws_start = 0
    matched = 0
    resultant_idxes = []

    for ws_end in range(len(str)):
        rightChar = str[ws_end]
        charMap[rightChar] -= 1

        if not charMap[rightChar]:
            matched += 1

        if len(charMap) == matched:
            resultant_idxes += ws_start,

        if ws_end >= len(pattern) - 1:
            leftChar = str[ws_start]
            ws_start += 1
            if leftChar in charMap:
                if not charMap[leftChar]:
                    matched -= 1
                charMap[leftChar] += 1
    return resultant_idxes

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual([1, 2], find_string_anagrams('ppqp', 'pq'))
    def test_2(self):
        self.assertEqual([2, 3, 4], find_string_anagrams('abbcabc', 'abc'))
    def test_3(self):
        self.assertEqual([1, 2], find_string_anagrams('aada', 'da'))

if __name__ == '__main__':
    unittest.main()
