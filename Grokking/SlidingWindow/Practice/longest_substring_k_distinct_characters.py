# Given a string, find the length of the longest substring in it with no more than K distinct characters
from collections import defaultdict
def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg, expected, output)
    else:
        print ("Failed Test Case: %s" % msg, expected, output)

def longest_substr_kdistinctchars(input_str, K):
    # Time Complexity: O(N), Space Complexity: O(K)
    ws_start = 0
    charMap = defaultdict(int)
    longest_substr = float('-inf')

    for ws_end in range(len(input_str)):
        rightChar = input_str[ws_end]
        charMap[rightChar] += 1

        if len(charMap) > K:
            left_char = input_str[ws_start]
            charMap[left_char] -= 1
            if not charMap[left_char]:
                del charMap[left_char]
            ws_start += 1
        longest_substr = max(longest_substr, ws_end-ws_start+1)
    return longest_substr

if __name__ == '__main__':
    test(4, longest_substr_kdistinctchars('araaci', 2))
    test(2, longest_substr_kdistinctchars('araaci', 1))
    test(5, longest_substr_kdistinctchars('cbbebi', 3))
