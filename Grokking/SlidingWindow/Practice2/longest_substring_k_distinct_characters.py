# Given a string, find the length of the longest substring in it with no more than K distinct characters
from collections import defaultdict

# O(n + n ~ n) time | O(k) space
def longest_substr_kdistinctchars(string, k):
    longestFound = float('-inf')
    ws_start = 0
    counter = defaultdict(int)
    for ws_end in range(len(string)):
        rightChar = string[ws_end]
        counter[rightChar] += 1

        while len(counter) > k:
            leftChar = string[ws_start]
            counter[leftChar] -= 1
            if not counter[leftChar]:
                del counter[leftChar]
            ws_start += 1
        longestFound = max(longestFound, (ws_end-ws_start+1))
    return longestFound

if __name__ == '__main__':
    print (longest_substr_kdistinctchars('araaci', 2)) # 4
    print (longest_substr_kdistinctchars('araaci', 1)) # 2
    print (longest_substr_kdistinctchars('cbbebi', 3)) # 5
