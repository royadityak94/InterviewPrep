# Given a string, find all of its permutations preserving the character sequence but changing case.
# Input: "ad52"; Output: "ad52", "Ad52", "aD52", "AD52"
# Input: "ab7c";  Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
from collections import deque

def find_letter_case_string_permutations(str):
    # Time Complexity: O(N*2^N), Space Complexity: O(N*2^N)
    permutations = []
    permutations.append([])

    for idx in range(len(str)):
        queue = deque()

        for set in permutations:
            queue.append(set)

        permutations = []
        while queue:
            current_set = queue.popleft()
            permutations.append(current_set + [str[idx]])
            if str[idx].isalpha():
                permutations.append(current_set+[str[idx].swapcase()])

    permutations = list(map(lambda x: ''.join(x), permutations))

    return permutations

def main():
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))

main()
