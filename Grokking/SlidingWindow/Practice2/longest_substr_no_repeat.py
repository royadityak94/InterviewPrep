# Given a string, find the length of the longest substring which has no repeating characters.
from collections import defaultdict

# O(n) time | O(k ~ 26 ~ 1) space 
def longest_substring_no_repeat(string):
    ws_start = 0
    counter = {}
    longestSubstr = float('-inf')

    for ws_end in range(len(string)):
        rightChar = string[ws_end]
        if rightChar in counter:
            ws_start = max(ws_start, counter[rightChar]+1)
        counter[rightChar] = ws_end
        longestSubstr = max(longestSubstr, (ws_end - ws_start + 1))
    return longestSubstr

if __name__ == '__main__':
    print(longest_substring_no_repeat('aabccbb')) #3
    print(longest_substring_no_repeat('abbbb')) #2
    print(longest_substring_no_repeat('abccde')) #3
