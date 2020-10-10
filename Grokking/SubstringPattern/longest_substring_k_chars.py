# Longest substring with k distinct characters
from collections import defaultdict

def compute_longest_substr_k_chars(input, k):
    # Time Complexity: O(N), Space Complexity: O(K)
    if len(input) < k or not input or not k:
        return ""

    left = 0
    charFrequency = defaultdict(int)
    max_length = float('-inf')

    for right in range(len(input)):
        right_char = input[right]
        charFrequency[right_char] += 1

        while len(charFrequency) > k:
            left_char = input[left]
            charFrequency[left_char] -= 1
            if not charFrequency[left_char]:
                del charFrequency[left_char]
            left += 1
        max_length = max(max_length, right-left+1)

    return max_length

def compute_longest_substr_without_repeating_characters(input):
    if not input:
        return
    left = 0
    max_length = float('-inf')
    charFrequency = defaultdict(int)

    for right in range(len(input)):
        right_char = input[right]
        charFrequency[right_char] += 1

        while charFrequency[right_char] > 1:
            left_char = input[left]
            charFrequency[left_char] -= 1
            if not charFrequency[left_char]:
                del charFrequency[left_char]
            left += 1
        max_length = max(max_length, right-left+1)
    return max_length

if __name__ == '__main__':
    input = 'aabaaabbssbbbxsdefbbbsssssbbbbbbbb'
    k = 2
    print (compute_longest_substr_k_chars(input, k))
    print ("Longest substring without repeating characters: ",
        compute_longest_substr_without_repeating_characters(input))
