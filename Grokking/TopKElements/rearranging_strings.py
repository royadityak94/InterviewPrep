# Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.
import unittest
from collections import Counter
from heapq import heappush, heappop


def rearrange_string(input):
    # Time Complexity: O(NLogN), Space Complexity: O(N)
    charMap = Counter(input)
    maxHeap = []
    final_str = ''

    for char, freq in charMap.items():
        heappush(maxHeap, (-freq, char))

    prevChar, prevFreq = None, 0
    while maxHeap:
        freq, char = heappop(maxHeap)

        if prevChar and -prevFreq > 0:
            heappush(maxHeap, (prevFreq, prevChar))

        final_str += char
        prevChar, prevFreq = char, freq + 1

    if not (len(final_str) == len(input)):
        return ""
    return final_str

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(rearrange_string("aappp"), "papap")
    def test_2(self):
        self.assertEqual(rearrange_string("Programming"), "gmrPagimnor")

if __name__ == '__main__':
    unittest.main()
