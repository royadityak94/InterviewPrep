# Longest no repeat substring program
# Input: "aabccbb", Output: 3, 'abc'
# Input: "abbbb", Output: 2, 'ab'
# Input: "abccde", Output: 3, {'abc', 'cde'}

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def longest_norepeat_substring(input_str):
    max_substring_length = 0
    character_map = {}
    window_start = 0

    for window_end in range(len(input_str)):
        char_right = input_str[window_end]
        if char_right in character_map:
            window_start = max(window_start, character_map[char_right]+1)
        character_map[char_right] = window_end
        max_substring_length = max(max_substring_length, window_end-window_start+1)
    return max_substring_length


def main():
    test(3, longest_norepeat_substring("aabccbb"), "Test - 1 (i/p: aabccbb)")
    test(2, longest_norepeat_substring("abbbb"), "Test - 2 (i/p: abbbb)")
    test(3, longest_norepeat_substring("abccde"), "Test - 3 (i/p: abccde)")

main()
