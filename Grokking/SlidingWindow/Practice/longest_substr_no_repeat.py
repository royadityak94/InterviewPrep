# Given a string, find the length of the longest substring which has no repeating characters.
from collections import defaultdict

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg, expected, output)
    else:
        print ("Failed Test Case: %s" % msg, expected, output)

def longest_substring_no_repeat(input_str):
    # Time Complexity: O(N+N) ~ O(N)
    # Space Complexity: O(K)
    ws_start = 0
    charMap = defaultdict(int)
    longest_substr = float('-inf')

    for ws_end in range(len(input_str)):
        rightChar = input_str[ws_end]
        if rightChar in charMap:
            ws_start = max(ws_start, charMap[rightChar]+1)
        charMap[rightChar] = ws_end
        longest_substr = max(longest_substr, ws_end-ws_start+1)
    return longest_substr

if __name__ == '__main__':
    test(3, longest_substring_no_repeat('aabccbb'))
    test(2, longest_substring_no_repeat('abbbb'))
    test(3, longest_substring_no_repeat('abccde'))
