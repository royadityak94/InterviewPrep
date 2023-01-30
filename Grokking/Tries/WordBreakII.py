""" Word Break ||
Given an input string, and a dictionary (as list ->), if the input string can be segmented into words that are found in dictionary, 
return all such combinations

{I/P: ('leetcode', ["leet","code"]) -> O/P: ['leet code']}, 
{I/P: ('applepenapple', ["apple","pen"]) -> O/P: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]}, 
{I/P: ('catsandog', ["cats","dog","sand","and","cat"]) -> O/P: []}, 
{I/P: ('catsanddog', ["cats","dog","sand","and","cat"]) -> O/P: ["cats and dog","cat sand dog"]}
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

def word_break_combinations_recursive(root, word, combinations, formed_words):
    if len(word) < 1:
        formed_words += combinations, 
    
    for idx in range(len(word)+1):
        prefix, postfix = word[:idx], word[idx:]
        if root.search(prefix):
            word_break_combinations_recursive(root, postfix, combinations + ' ' + prefix, formed_words)


def word_break_combinations(word, dict_list):
    root = Trie()
    for _word in dict_list:
        root.insert(_word)

    combinations = ''
    formed_words = []

    for idx in range(len(word)):
        combinations += word[idx]
        prefix, postfix = word[:idx+1], word[idx+1:]
        if root.search(prefix):
            word_break_combinations_recursive(root, postfix, combinations, formed_words)
    return formed_words



def main():
    # Initializing logger 
    global logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    word, dict_list = 'catsanddog', ['cats', 'dog', 'sand', 'and', 'cat']
    # ["cats and dog","cat sand dog"]
    logging.info(f'Is word break for {word} possible from list - {dict_list}? {word_break_combinations(word, dict_list)}') 
    

    word, dict_list = 'catsandog', ['cats', 'dog', 'sand', 'and', 'cat']
    logging.info(f'Is word break for {word} possible from list: {dict_list}: {word_break_combinations(word, dict_list)}')

    word, dict_list = 'leetcode', ['leet', 'code']
    logging.info(f'Is word break for {word} possible from list: {dict_list}: {word_break_combinations(word, dict_list)}')

    word, dict_list = 'applepenapple', ['apple', 'pen']
    ["apple and pen"]
    logging.info(f'Is word break for {word} possible from list: {dict_list}: {word_break_combinations(word, dict_list)}')

    word, dict_list = 'applepenapplepen', ['apple', 'pen']
    logging.info(f'Is word break for {word} possible from list: {dict_list}: {word_break_combinations(word, dict_list)}')

main()