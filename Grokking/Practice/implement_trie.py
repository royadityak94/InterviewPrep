from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isword = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.nodes[char]
        current.isword = True

    def search(self, word):
        current = self.root
        for char in word:
            if not char in current.nodes:
                return False
            current = current.nodes[char]
        return current.isword

    def startsWith(self, word):
        current = self.root
        for char in word:
            if not char in current.nodes:
                return False
            current = current.nodes[char]
        return True

    def delete(self, word):
        current = self.root
        if self.search(word):
            for char in word:
                current = current.nodes[char]
            current.isword = False
        return


def main():
    trie = Trie()

    trie.insert("apple");
    print (trie.search("apple"));   #returns true
    print (trie.search("app"));     # returns false
    print (trie.startsWith("app")); # returns true
    trie.insert("app");
    print (trie.search("app"));     # returns true

main()
