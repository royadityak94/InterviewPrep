# Ref : https://www.youtube.com/watch?v=5xuvqBjRkok
# Given an array of unique characters and a string 'str', compute the shortest unique
# string contiaining all the characters in the array
# Example: arr = ['x', 'y', 'z'], str='xyyzyzyx', Output: zyx

def matches_criteria(arr, sub_str):
    charMap = []
    for ch in sub_str:
        if ch in charMap:
            return False
        else:
            if ch in arr:
                charMap += ch,
    if arr.sort() == charMap.sort():
        return True
    return False

def smallest_substring_all_characters_naive(arr, sub_str):
    # Time Complexity: O(NM), N=len(sub_str), M=len(arr)
    # Space Complexity: O(M)
    N = len(arr)
    i = 0
    while i < (len(sub_str)-N+1):
        computed_str = sub_str[i:i+N+1]
        if matches_criteria(arr, computed_str):
            return computed_str
        i += 1
    return ""

def is_valid_window(arr, computed):
    print ("Input to valid window : ", computed)
    seenMap = []
    for ch in computed:
        if ch in arr:
            if ch not in seenMap:
                seenMap += ch,
            else:
                return False
    if len(seenMap) == len(arr):
        print ("This window matched ...", computed, seenMap)
        return True
    return False


def smallest_substring_all_characters(arr, main_str):
    # finding a max value window using left, right pointers and then check if we can shrink it any further
    left, right = 0, 0
    computed = None
    while left <= right and right < len(main_str):
        if main_str[left] not in arr:t
            left += 1
        right += 1

        # Check if all characters are present in the big string
        computed = main_str[left:right+1]
        if is_valid_window(arr, computed):
            print ("Found valid window: ", computed)
            break
        else:
            left += 1

    print ("Obtained window: ", computed)


if __name__ == '__main__':
    arr, str = ['x', 'y', 'z'], 'xyyzyxzyx'
    print (smallest_substring_all_characters_naive(arr, str))
    # Optimized implementations
    print (smallest_substring_all_characters(arr, str))
