# Given a string with lowercase letters only, if you are allowed to replace no more
# than ‘k’ letters with any letter, find the length of the longest substring having
# the same letters after replacement
from collections import defaultdict

# O(n) | O(1)
def length_of_longest_substring(string, k):
    ws_start = 0
    counter = defaultdict(int)
    longestSubstr = float('-inf')
    maxRepeatingChar = 0

    for ws_end in range(len(string)):
        rightChar = string[ws_end]
        counter[rightChar] += 1
        maxRepeatingChar = max(maxRepeatingChar, counter[rightChar])

        while (ws_end - ws_start + 1 - maxRepeatingChar) > k:
            leftChar = string[ws_start]
            counter[leftChar] -= 1
            ws_start += 1
        longestSubstr = max(longestSubstr, (ws_end - ws_start + 1))
    return longestSubstr


if __name__ == '__main__':
    print (length_of_longest_substring('aabccbb', 2)) # 5
    print (length_of_longest_substring('abbcb', 1)) #4
    print (length_of_longest_substring('abccde', 1)) #3
