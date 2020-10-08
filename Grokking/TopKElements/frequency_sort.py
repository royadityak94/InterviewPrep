# Given a string, sort it based on the decreasing frequency of its characters.
import unittest
from heapq import heappush, heappop
from collections import Counter

def frequency_sort(str):
    # Time Complexity: O(NLOGN), Space Complexity: O(N)
    charMap = Counter(str)
    occurrences = []
    for key in charMap.keys():
        heappush(occurrences, (-charMap[key], key))

    final_str = ''
    while occurrences:
        freq, key = heappop(occurrences)
        final_str += ''.join([key]*-freq)

    return final_str

class Test(unittest.TestCase):
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_1(self):
        self.assertEqual(frequency_sort('Programming'), 'ggmmrrPaino')
    def test_2(self):
        self.assertEqual(frequency_sort('abcbab'), 'bbbaac')

if __name__ == '__main__':
    unittest.main()
