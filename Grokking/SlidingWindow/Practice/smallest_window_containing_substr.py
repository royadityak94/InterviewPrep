import unittest
from collections import defaultdict

def find_substring(str, pattern):
    # Time Complexity: O(N+M)
    # Space Complexity: O(M) [Special Case: O(N) when pattern = permutation(str)]
    charMap = defaultdict(int)
    for ch in pattern:
        charMap[ch] += 1

    ws_start = 0
    matched = 0
    substr_start = 0
    ws_length = float('inf')

    for ws_end in range(len(str)):
        rightChar = str[ws_end]

        if rightChar in charMap:
            charMap[rightChar] -= 1
            if charMap[rightChar] >= 0:
                matched += 1

        while matched == len(pattern):
            if ws_length > (ws_end-ws_start+1):
                ws_length = ws_end-ws_start+1
                substr_start = ws_start

            leftChar = str[ws_start]
            ws_start += 1
            if leftChar in charMap:
                if not charMap[leftChar]:
                    matched -= 1
                charMap[leftChar] += 1

    if ws_length > len(str):
        return ""
    return str[substr_start:substr_start+ws_length]

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual('abdec', find_substring('aabdec', 'abc'))
    def test_2(self):
        self.assertEqual('bca', find_substring('abdbca', 'abc'))
    def test_3(self):
        self.assertEqual('', find_substring('adcad', 'abc'))

if __name__ == '__main__':
    unittest.main()
