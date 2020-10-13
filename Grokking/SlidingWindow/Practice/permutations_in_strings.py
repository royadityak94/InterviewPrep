import unittest
from collections import defaultdict

def is_pattern_permutation_of_string(str, pattern):
    # Time Complexity: O(N+N) ~ O(N)
    # Space Complexity: O(M), M=len(pattern)
    charMap = defaultdict(int)

    for ch in pattern:
        charMap[ch] += 1

    ws_start = 0
    matched = 0

    for ws_end in range(len(str)):
        rightChar = str[ws_end]
        if rightChar in charMap:
            charMap[rightChar] -= 1
            if not charMap[rightChar]:
                matched += 1

        if matched == len(charMap):
            return True

        if ws_end >= len(pattern) - 1:
            leftChar = str[ws_start]
            ws_start += 1
            if leftChar in charMap:
                if not charMap[leftChar]:
                    matched -= 1
                charMap[leftChar] += 1
    return False

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertTrue(is_pattern_permutation_of_string('oidbcaf', 'abc'))
    def test_2(self):
        self.assertFalse(is_pattern_permutation_of_string('odicf', 'dc'))
    def test_3(self):
        self.assertTrue(is_pattern_permutation_of_string('bcdxabcdy', 'bcdyabcdx'))
    def test_4(self):
        self.assertTrue(is_pattern_permutation_of_string('aaacb', 'abc'))

if __name__ == '__main__':
    unittest.main()
