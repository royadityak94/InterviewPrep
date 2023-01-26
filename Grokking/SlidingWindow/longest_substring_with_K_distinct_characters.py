# Program to implement the longest substring with K distinct character (Hashmap Implementation)
"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def longest_substring_with_K_distinct_characters(input_str, max_distinct_char):
    # Runtime Complexity = O(N+N) ~ O(N)
    window_start = 0
    max_length = 0
    character_map = {}

    for window_end in range(len(input_str)):
        ele_right = input_str[window_end]
        if ele_right not in character_map:
            character_map[ele_right] = 0
        character_map[ele_right] += 1

        while len(character_map) > max_distinct_char:
            ele_left = input_str[window_start]
            character_map[ele_left] -= 1
            if character_map[ele_left] == 0:
                del character_map[ele_left]
            window_start += 1

        max_length = max(max_length, window_end-window_start+1)

    return max_length


def main():
    test(4, longest_substring_with_K_distinct_characters("araaci", 2), "Test - 1")
    test(2, longest_substring_with_K_distinct_characters("araaci", 1), "Test - 2")
    test(5, longest_substring_with_K_distinct_characters("cbbebi", 3), "Test - 3")

main()
