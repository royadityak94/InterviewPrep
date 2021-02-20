# Given a string, find all of its permutations preserving the character sequence but changing case.
# Input: "ad52"; Output: "ad52", "Ad52", "aD52", "AD52"
# Input: "ab7c";  Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
from collections import deque


def main():
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))

main()
