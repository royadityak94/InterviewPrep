# Python program to find the missing number in the sequence where each number is repeated
# exactly 'k' times except one which is repeated (k-1) times
# Properties: 1 ^ 0 = 1, 31 ^ 0 = 31

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def missing_number_in_pattern(arr):
    # Time Complexity: O(N), Space Complexity: O(1)
    output = arr[0]
    for i in range(1, len(arr)):
        output ^= arr[i]
    return output

def missing_number_in_pattern_using_hashmap(arr):
    # Time Complexity: O(N), Space Complexity: O(N)
    existing_char_map = {}
    for i in range(len(arr)):
        char = arr[i]
        if char in existing_char_map:
            del existing_char_map[char]
        else:
            existing_char_map[char] = 1

    return existing_char_map.keys()[0]

def main():
    test(4, missing_number_in_pattern([1, 4, 2, 1, 3, 2, 3]), "Test - 1")
    test(9, missing_number_in_pattern([7, 9, 7]), "Test - 2")

    # Using Hashmap
    test(4, missing_number_in_pattern_using_hashmap([1, 4, 2, 1, 3, 2, 3]), "Hashmap Test - 1")
    test(9, missing_number_in_pattern_using_hashmap([7, 9, 7]), "Hashmap Test - 2")

main()
