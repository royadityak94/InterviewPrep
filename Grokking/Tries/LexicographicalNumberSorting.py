"""Lexicographical Numbers
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
(n=13 -> [1,10,11,12,13,2,3,4,5,6,7,8,9]), (n=2 -> [1, 2])
"""
from collections import defaultdict

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

def lexicographical_ordering_recursive(head, current_str, result_set):
    if head.is_word:
        result_set += int(current_str), 
    
    for sub_word, sub_trie in head.children.items():
        lexicographical_ordering_recursive(sub_trie, current_str+sub_word, result_set)

def return_lexicographical_ordering(n):
    root = Trie()
    for num in range(1, n+1):
        root.insert(str(num))

    result_set = []
    lexicographical_ordering_recursive(root.root, '', result_set)
    return result_set

def main():
    print (f'Output Values for 13: {return_lexicographical_ordering(13)}')
    print (f'Output Values for 9: {return_lexicographical_ordering(9)}')

main()