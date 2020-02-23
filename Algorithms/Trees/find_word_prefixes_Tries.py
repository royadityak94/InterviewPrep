# Python module to implement Trie DS for search, insert
import unittest

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

    def search(self, key):
        pCrawl = self.root
        for level in range(len(key)):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl is not None and pCrawl.isEndOfWord

class Test(unittest.TestCase):
    def test_case1(self):
        keys = ["the","a","there","anaswe","any", "by","their"]
        t = Trie()

        for key in keys:
            t.insert(key)

        # Search for different keys
        self.assertEqual(t.search("the"), True)
        self.assertEqual(t.search("these"), False)
        self.assertEqual(t.search("their"), True)
        self.assertEqual(t.search("thaw"), False)

if __name__ == '__main__':
    unittest.main()
