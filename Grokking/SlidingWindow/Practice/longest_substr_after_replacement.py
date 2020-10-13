# Given a string with lowercase letters only, if you are allowed to replace no more
# than ‘k’ letters with any letter, find the length of the longest substring having
# the same letters after replacement
import unittest
from collections import Counter, defaultdict
from heapq import heappush, heappop

# Without Sliding window
def length_of_longest_substring_archive(str, K):
    # Time Complexity: O(NLogN)
    # Space Complexity: O(N)
    charMap = Counter(str)
    tupleVals = list(map(lambda x: (charMap[x], x), charMap))
    tupleVals.sort(reverse=True)

    highest = tupleVals.pop(0)[0]
    cnt = 0

    while cnt < K:
        popped = tupleVals.pop(0)
        cnt += min(K, popped[0])
        highest += min(K, popped[0])

        if popped[0] > K:
            tupleVals.insert(0, (popped[0]-K, popped[1]))
    return highest

# With Sliding window
def length_of_longest_substring(str, K):
    # Time Complexity: O(N+N) ~ O(N)
    # Space Complexity: O(K) ~ O(26) ~ O(1)
    ws_start = 0
    maxRepeatLetterCount = max_length = float('-inf')
    charMap = defaultdict(int)

    for ws_end in range(len(str)):
        rightChar = str[ws_end]
        charMap[rightChar] += 1
        maxRepeatLetterCount = max(maxRepeatLetterCount, charMap[rightChar])

        # When the window containing a certain set of letters has more than 'K' distinct letter
        if (ws_end-ws_start+1-maxRepeatLetterCount) > K:
            leftChar = str[ws_start]
            charMap[leftChar] -= 1
            if not charMap[leftChar]:
                del charMap[leftChar]
            ws_start += 1
        max_length = max(max_length, (ws_end-ws_start+1))
    return max_length

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(5, length_of_longest_substring('aabccbb', 2))
    def test_2(self):
        self.assertEqual(4, length_of_longest_substring('abbcb', 1))
    def test_3(self):
        self.assertEqual(3, length_of_longest_substring('abccde', 1))

if __name__ == '__main__':
    unittest.main()
