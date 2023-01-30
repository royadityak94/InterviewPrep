"""Longest Common Prefix of a given array of string

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
{I/P: ["flower","flow","flight"], O/P: "fl"}, {I/P: ["dog","racecar","car"], O/P: ""}
"""
from collections import defaultdict
import logging 

class TrieNode:
    def __init__(self):
        self.children = defaultdict(chr)
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
    
    def get_longest_common_prefix(self):
        longest_prefix = []
        head = self.root 
        while head: 
            children = list(head.children.keys())
            if len(children) > 1:
                break 
            longest_prefix += children[0], 
            head = head.children[children[0]]
        return ''.join(longest_prefix)

def test_scenarios(words):
    root = Trie()
    for word in words: 
        root.insert(word)
    return root.get_longest_common_prefix()


def main():
    # Setup logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    words = ['flower', 'flow', 'flight']
    logging.info (f'Longest Common prefix for {words} is {test_scenarios(words)}')

    words = ["dog","racecar","car"]
    logging.info (f'Longest Common prefix for {words} is {test_scenarios(words)}')

    words = ["appd","apple","appliance", 'appz']
    logging.info (f'Longest Common prefix for {words} is {test_scenarios(words)}')

main()
