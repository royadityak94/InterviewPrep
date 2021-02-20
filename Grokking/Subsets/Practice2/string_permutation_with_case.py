# Given a string, find all of its permutations preserving the character sequence but changing case.
# Input: "ad52"; Output: "ad52", "Ad52", "aD52", "AD52"
# Input: "ab7c";  Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

def find_letter_case_string_permutations(string):
    permutations = [string]
    for i in range(len(string)):
        if string[i].isalpha():
            for j in range(len(permutations)):
                current = list(permutations[j])
                current[i] = current[i].swapcase()
                permutations += ''.join(current),
    return permutations


def main():
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))

    # "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

main()
