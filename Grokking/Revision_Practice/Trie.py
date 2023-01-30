"""Quick Revision of Trie
Basic Concept: TrieNode (formed of children (as dict) and end_of_word marker (as bool), and its value)
Insert: 
    Iterate from root to that character and add the ch in the children
Search: 
    Iterate from root to children, until at that character end of word is found
"""
from collections import defaultdict

class TrieNode: 
    def __init__(self):
        self.children = defaultdict()
        self.is_word = False 
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        head = self.root 
        for ch in word:
            if ch not in head.children:
                head.children[ch] = TrieNode()
            
            head = head.children[ch]
        head.is_word = True 
    
    def search(self, word, startsWith=False):
        head = self.root 
        for ch in word:
            if ch not in head.children:
                return False 
            head = head.children[ch]
        if startsWith:
            return True
        return head.is_word

if __name__ == '__main__':
    words_to_insert = ['apple', 'appd', 'andry', 'ander']
    root = Trie()
    for word in words_to_insert:
        root.insert(word)

    
    # Search for words 
    words_to_search = words_to_insert + ['cat', 'applez', 'appdz', 'andryz', 'zman']
    for word in words_to_search:
        print (f'Word={word} is in Trie: {root.search(word)}')

    # Starts with validation
    word_prefixes_to_find = ['app', 'appd', 'and', 'ande', 'am']
    for word in word_prefixes_to_find:
        print (f'Word Prefix={word} is in Trie: {root.search(word, True)}')
