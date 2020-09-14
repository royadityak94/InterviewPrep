# Given a string, find all of its permutations preserving the character sequence but changing case.
# Input: "ad52"; Output: "ad52", "Ad52", "aD52", "AD52"
# Input: "ab7c";  Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
from collections import deque

def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append([])

    for idx in range(len(str)):
        queue = deque()

        for set in permutations:
            queue.append(set)

        new_set = []
        while queue:
            current_set = queue.popleft()
            if str[idx].isalpha():
                for j in range(len(current_set)+1):
                    temp = list(current_set)
                    temp.insert(j, str[idx])
                    new_set.append(temp)
            else:
                temp = list(current_set)
                temp.append(str[idx])
                new_set.append(temp)
        permutations = new_set

    permutations = list(map(lambda x: ''.join(x), permutations))

    return permutations

def main():
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))

    # "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

main()
