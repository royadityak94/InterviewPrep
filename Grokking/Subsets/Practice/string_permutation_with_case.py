# Given a string, find all of its permutations preserving the character sequence but changing case.
# Input: "ad52"; Output: "ad52", "Ad52", "aD52", "AD52"
# Input: "ab7c";  Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
from collections import deque

def compare_results(arr1, arr2):
    for ele in arr1:
        if ele in arr2:
            arr2.remove(ele)
    return not (len(arr1) and len(arr2))

def string_permutations_swapcase(string):
    permutations = [string]

    for i in range(len(string)):
        if string[i].isalpha():
            for j in range(len(permutations)):
                current = list(permutations[j])
                current[i] = current[i].swapcase()
                permutations += ''.join(current),
    return permutations


def main():
    expected_1 = ['ad52', 'Ad52', 'aD52', 'AD52']
    expected_2 = ['ab7c', 'Ab7c', 'aB7c', 'AB7c', 'ab7C', 'Ab7C', 'aB7C', 'AB7C']
    obtained_1 = string_permutations_swapcase("ad52")
    obtained_2 = string_permutations_swapcase("ab7c")
    print("String permutations are: " + str(obtained_1), " Matched: ", compare_results(expected_1, obtained_1))
    print("String permutations are: " + str(obtained_2), " Matched: ", compare_results(expected_2, obtained_2))

    # "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

main()
