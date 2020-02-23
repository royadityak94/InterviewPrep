# Python module to implement autocompletion using tries
import unittest
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getNode()
    def getNode(self):
        return TrieNode()
    def _charToIndex(self, ch):
        return ord(ch) - ord('a')
    def insert(self, key):
        pCrawl = self.root
        for level in range(len(key)):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def count_children(self, pCrawl):
        count = 0
        for level in range(26):
            index = self._charToIndex(chr(level))
            if pCrawl.children[index]:
                count += 1
                global idxes
                idxes = index
        return count

    def walkTries(self, pCrawl):
        prefix = ""
        while (self.count_children(pCrawl) == 1 and not pCrawl.isEndOfWord):
            pCrawl = pCrawl.chilren[idxes]
            prefix += chr(97 + idxes)
        return prefix

    def walkTries_main(self, key):
        pCrawl = self.root
        for level in range(len(key)):
            index = self._charToIndex(key[level])
            if pCrawl.children[index]:
                pCrawl = pCrawl.children[index]
            else:
                return ""
        return self.walkTries(pCrawl)


class Test(unittest.TestCase):
    def test_case1(self):
        keys = ["hackerrank", "hackathon", "haccuna", "hubrey", "hack"]
        t = Trie()
        for key in keys:
            t.insert(key)

        print (t.walkTries_main('hac'))

if __name__ == '__main__':
    unittest.main()
