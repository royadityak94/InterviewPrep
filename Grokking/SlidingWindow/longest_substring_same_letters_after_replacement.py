# Python progeam to find the longest substring with some 'K' letters replaced from the window.
# Input: "aabccbb", k=2, Output: 5
# Input: "abbcb", k=1, Output: 4
# Input: "abccde", k=1, Output: 3
"""
Problem Statement
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def length_of_longest_substring_with_replacement(input_str, k):
    # Time Complexity: O(N), Space Complexity: O(26) ~ O(1) [Asymptotic equality]
    max_length = 0
    max_same_char_repeating_count = 0
    window_start = 0
    char_map = {}

    for window_end in range(len(input_str)):
        right_char = input_str[window_end]
        if right_char not in char_map:
            char_map[right_char] = 0
        char_map[right_char] += 1

        max_same_char_repeating_count = max(max_same_char_repeating_count, char_map[right_char])

        if ((window_end-window_start+1)-max_same_char_repeating_count > k):
            left_char = input_str[window_start]
            char_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end-window_start+1)

    return max_length

def main():
    test(5, length_of_longest_substring_with_replacement("aabccbb", 2), "Test - 1 (i/p: aabccbb)")
    test(4, length_of_longest_substring_with_replacement("abbcb", 1), "Test - 1 (i/p: abbcb)")
    test(3, length_of_longest_substring_with_replacement("abccde", 1), "Test - 1 (i/p: abccde)")

main()
