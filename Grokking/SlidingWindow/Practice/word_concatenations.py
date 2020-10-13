# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.
import unittest
from collections import defaultdict

def find_word_concatenation(str, words):
    # Time Complexity: O(NM*len(words[0])), N=len(str), M=len(words)
    # Space Complexity: O(M) [Worst Case: O(M+N)]
    wordMap = defaultdict(int)
    for word in words:
        wordMap[word] += 1

    words_length, word_length = len(words), len(words[0])
    resulting_idxes = []

    for i in range((len(str)-word_length*words_length)+1):
        seenWords = defaultdict(int)
        for j in range(words_length):
            next_word_idx = i + (word_length)*j
            word = str[next_word_idx:next_word_idx+word_length]
            if word not in wordMap:
                break
            seenWords[word] += 1

            if seenWords[word] > wordMap[word]:
                break

            if j+1 == words_length:
                resulting_idxes += i,
    return resulting_idxes

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual([0, 3], find_word_concatenation('catfoxcat', ["cat", "fox"]))
    def test_2(self):
        self.assertEqual([3], find_word_concatenation('catcatfoxfox', ["cat", "fox"]))

if __name__ == '__main__':
    unittest.main()
