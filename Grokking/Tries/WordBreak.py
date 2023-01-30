""" Word Break 
Given an input string, and a dictionary (as list ->), if the input string can be segmented into words that are found in dictionary, return True, else False

{I/P: ('leetcode', ["leet","code"]) -> O/P: True}, {I/P: ('applepenapple', ["apple","pen"]) -> O/P: True}, 
{I/P: ('catsandog', ["cats","dog","sand","and","cat"]) -> O/P: False}, {I/P: ('catsanddog', ["cats","dog","sand","and","cat"]) -> O/P: True}
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
    
    def search(self, word):
        head = self.root 
        for ch in word: 
            if ch not in head.children:
                return False 
            head = head.children[ch]
        return head.is_word
    
def is_word_break_possible_recursive(root, word, min_word_size=1):
    if len(word) < 1:
        return True

    for idx in range(min_word_size, len(word)+1):  # Can also iterate from (1 to range)
        prefix = word[:idx]
        postfix = word[idx:]
        if root.search(prefix) and is_word_break_possible_recursive(root, postfix, min_word_size):
            return True
    return False


def is_word_break_possible(word, dict_list):
    root = Trie()
    # Insert words from dictionary
    min_word_length = float('inf')
    for _word in dict_list:
        root.insert(_word)
        min_word_length = min(min_word_length, len(_word))
    
    return is_word_break_possible_recursive(root, word, min_word_length)

def main():
    # Initialize logger 
    global logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    word, dict_list = 'catsanddog', ['cats', 'dog', 'sand', 'and', 'cat']
    logging.info(f'Is word break for {word} possible from list: {dict_list}: {is_word_break_possible(word, dict_list)}')

    word, dict_list = 'catsandog', ['cats', 'dog', 'sand', 'and', 'cat']
    logging.info(f'Is word break for {word} possible from list: {dict_list}: {is_word_break_possible(word, dict_list)}')

    word, dict_list = 'leetcode', ['leet', 'code']
    logging.info(f'Is word break for {word} possible from list: {dict_list}: {is_word_break_possible(word, dict_list)}')

    word, dict_list = 'applepenapple', ['apple', 'pen']
    logging.info(f'Is word break for {word} possible from list: {dict_list}: {is_word_break_possible(word, dict_list)}')

    word, dict_list = 'muza', ['apple', 'pen']
    logging.info(f'Is word break for {word} possible from list: {dict_list}: {is_word_break_possible(word, dict_list)}')

main()