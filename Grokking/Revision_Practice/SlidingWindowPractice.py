""""Quick practice for all sliding window based logic"""
from typing import List

def test(output, expected, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)


"""Expected Output(EO) and Logic
EO: ("aabccbb" -> 3: 'abc'), ("abccde" -> 3: (abc, cde)), ("abbb" -> 2: (ab))
Logic: 
    Iterate from start to end -> In collision, move `start` to max. of start, v. colliding char's + 1 to right -> Keep adding right char to current end index
"""
def longest_norepeat_substring(input_string: str) -> int:
    ws_start = 0
    character_map = {}
    longest_norepeat_substring_len = -1e100
    for ws_end in range(len(input_string)):
        
        left_char = input_string[ws_start]
        right_char = input_string[ws_end]
        #print (f'start={ws_start}, end={ws_end}, input_string={input_string}, left={left_char}, right={right_char}, cmap={character_map}')
        if right_char in character_map:
            ws_start = max(ws_end, character_map[right_char]+1)
        character_map[right_char] = ws_end
        longest_norepeat_substring_len = max(longest_norepeat_substring_len, (ws_end-ws_start+1))

    return longest_norepeat_substring_len

"""
EO: (([2, 1, 5, 2, 3, 2], 7) -> 2: (5, 2)), (([2, 1, 5, 2, 8], 7) -> 1: (8)), ([3, 4, 1, 1, 6], 8) -> 3: ((3, 4, 1), (1, 1, 6))
Logic: 
    Iterate from start to end -> (base case: if current number > desired sum return 1) -> keep expanding ws_end until max_sum is reach, 
    then -> keep decreasing ws_right until sum is no longer greater than desired sum 
"""
def smallest_contiguous_subarray_for_given_sum(input_arr: List[int], desired_sum: int) -> int: 
    ws_start = ws_end = 0
    input_arr_len = len(input_arr)
    max_array_len = -1

    for ws_end in range(input_arr_len):
        number_right = input_arr[ws_end]
        if number_right >= desired_sum:
            return 1
        current_arr_sum = sum(input_arr[ws_start:ws_end+1])
        while ((current_arr_sum >= desired_sum) and (ws_start < input_arr_len) and (ws_end > ws_start)):
            ws_start += 1
            current_arr_sum = sum(input_arr[ws_start:ws_end+1])
        max_array_len = max(max_array_len, (ws_end-ws_start+1))

    return max_array_len

"""
EO: (([2, 1, 5, 1, 3, 2], 3) -> 9: (5, 1, 3)), (([2, 3, 4, 1, 5], 2) -> 2: (3, 4))
Logic: Initialize the current max for the given window, loop through from left to right, and  find out if another window had a better sum -> sum + (right - left)
"""
def maximum_sum_subarray_size_k(input_arr: List[int], size_k: int) -> int: 
    ws_start = 0
    input_arr_len = len(input_arr)
    if input_arr_len < size_k:
        return -1
    current_sum_for_subarray = max_sum_for_subarray = sum(input_arr[ws_start:ws_start+size_k])

    for ws_end in range(size_k, input_arr_len):
        current_sum_for_subarray = current_sum_for_subarray + (input_arr[ws_end] - input_arr[ws_start])
        max_sum_for_subarray = max(max_sum_for_subarray, current_sum_for_subarray)
        ws_start += 1

    return max_sum_for_subarray

"""
EO: ((['A', 'B', 'C', 'A', 'C'], 2) -> 3: ('C', 'A', 'C')), (['A', 'B', 'C', 'B', 'B', 'C'], 2) -> 5 ('B', 'C', 'B', 'B', 'C'))
Logic: 
    Maintain character map, as soon as count of keys is higher than allowed(diversity_k), remove from left, until it has exactly k
""" 
def max_same_fruits_in_basket_with_diversity(fruits: List[str], diversity_k):
    ws_start = 0
    character_map = {}
    maximum_contained_fruits = -1
    
    for ws_end in range(len(fruits)):
        right_char = fruits[ws_end]
        if right_char not in character_map:
            character_map[right_char] = 0
        if len(character_map) > diversity_k:
            left_char = fruits[ws_start]
            character_map[left_char]  -= 1
            if not character_map[left_char]:
                del character_map[left_char]
            ws_start += 1
        character_map[right_char] += 1
        maximum_contained_fruits = max(maximum_contained_fruits, (ws_end - ws_start + 1))
    return maximum_contained_fruits

"""
EO: ((['A', 'B', 'C', 'A', 'C'], 2) -> 3: ('C', 'A', 'C')), (['A', 'B', 'C', 'B', 'B', 'C'], 2) -> 5 ('B', 'C', 'B', 'B', 'C'))
Logic: 
    Maintain character map, as soon as length of window (minus, the frequency of highest repeating character) is higher than allowed(diversity_k), remove from left, until it has exactly k
""" 
def longest_substring_with_same_letters_after_replacement(input_arr: List[chr], replacements_k:int) -> int: 
    longest_substring = 0
    ws_start = 0
    character_map = {}
    max_repeating_character = 0

    for ws_end in range(len(input_arr)):
        right_char = input_arr[ws_end]
        if right_char not in character_map:
            character_map[right_char] = 0
        character_map[right_char] += 1
        max_repeating_character = max(max_repeating_character, character_map[right_char])

        if ((ws_end - ws_start + 1) - max_repeating_character) > replacements_k:
            left_char = input_arr[ws_start]
            character_map[left_char] -= 1
            ws_start += 1 
        longest_substring = max(longest_substring, (ws_end - ws_start + 1))
    return longest_substring

"""
EO: (([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) -> 6: (Replace index(s): 5, 8)), 
([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) -> 9 (Replace index(s): 6, 9, 10))
Logic: 
    As soon as effective window count (= window_length - Max Frequency of one is higher than 'allowed_replacement_k' shrink start until balance is restored)
""" 
def longest_subarrays_with_ones_after_replacement(input_arr: List[int], allowed_replacement_k: int) -> int:
    longest_subarray = 0
    ws_start = 0
    max_count_of_ones = 0

    for ws_end in range(len(input_arr)):
        right_digit = input_arr[ws_end]
        max_count_of_ones = max(max_count_of_ones, input_arr[ws_start:ws_end+1].count(1))
        if ((ws_end-ws_start+1) - max_count_of_ones) > allowed_replacement_k:
            ws_start += 1
        longest_subarray = max(longest_subarray, (ws_end - ws_start + 1))
    return longest_subarray

def main() -> None:
    # Longest No repeat substring
    test(longest_norepeat_substring("aabccbb"), 3, "longest_norepeat_substring - test case 1")
    test(longest_norepeat_substring("abccde"), 3, "longest_norepeat_substring - test case 2")
    test(longest_norepeat_substring("abbb"), 2, "longest_norepeat_substring - test case 3")

    # Smallest Contiguous subarray for a given sum
    test(smallest_contiguous_subarray_for_given_sum([2, 1, 5, 2, 3, 2], 7), 2, "smallest_contiguous_subarray_for_given_sum - test case 1")
    test(smallest_contiguous_subarray_for_given_sum([2, 1, 5, 2, 8], 7), 1, "smallest_contiguous_subarray_for_given_sum - test case 2")
    test(smallest_contiguous_subarray_for_given_sum([3, 4, 1, 1, 6], 8), 3, "smallest_contiguous_subarray_for_given_sum - test case 3")

    # Maximum sum subarray of size 'k'
    test(maximum_sum_subarray_size_k([2, 1, 5, 1, 3, 2], 3), 9, "maximum_sum_subarray_size_k - test case 1")
    test(maximum_sum_subarray_size_k([2, 3, 4, 1, 5], 2), 7, "maximum_sum_subarray_size_k - test case 2")

    # Maximum same fruits in basket with diversity (k)
    test(max_same_fruits_in_basket_with_diversity([*'ABCAC'], 2), 3, "max_same_fruits_in_basket_with_diversity: test case 1")
    test(max_same_fruits_in_basket_with_diversity([*'ABCBBC'], 2), 5, "max_same_fruits_in_basket_with_diversity: test case 2")

    # Longest substring with k distinct characters (k)
    # Same as max_same_fruits_in_basket_with_diversity

    # Longest substring with same letters after replacement with allowed replacement as 'k'
    test(longest_substring_with_same_letters_after_replacement([*'aabccbb'], 2), 5, "longest_substring_with_same_letters_after_replacement - test case 1")
    test(longest_substring_with_same_letters_after_replacement([*'abbcb'], 1), 4, "longest_substring_with_same_letters_after_replacement - test case 2")
    test(longest_substring_with_same_letters_after_replacement([*'abccde'], 1), 3, "longest_substring_with_same_letters_after_replacement - test case 3")

    # Longest subarrays formed of ones after replacement with allowed replacement as 'k' 
    test(longest_subarrays_with_ones_after_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2), 6, "longest_subarrays_with_ones_after_replacement - test case 1")
    test(longest_subarrays_with_ones_after_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3), 9, "longest_subarrays_with_ones_after_replacement - test case 1")

main()
