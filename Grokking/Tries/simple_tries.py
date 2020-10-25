# Source: https://leetcode.com/problems/implement-trie-prefix-tree/
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(int) #[None]*26
        self.isEndofWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode() #self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, word):
        pCrawl = self.root
        for level in word:
            index = level
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndofWord = True

    def search(self, word):
        pCrawl = self.root
        for level in word:
            index = level
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl and pCrawl.isEndofWord

    def startsWith(self, word):
        pCrawl = self.root
        for level in word:
            index = level
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print (trie.search("apple"))  #returns true
    print (trie.search("app"))   # returns false
    print (trie.startsWith("app")) # returns true
    trie.insert("app")
    print (trie.search("app")) # returns true
