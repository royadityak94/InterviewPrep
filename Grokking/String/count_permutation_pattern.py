# Given big & small string, find count of total permutations of small string present in the big string

from collections import defaultdict


# O(n) time | O(n + n ~ n) space
def count_permutations(bigStr, smallStr):
    left = 0
    right = 0
    smallStr_map = defaultdict(int)
    for ch in smallStr:
        smallStr_map[ch] += 1
    resultant = []

    tmp_map = defaultdict(int)
    while right < len(bigStr):
        tmp_map[bigStr[right]] += 1
        if (right - left + 1) == len(smallStr):
            if compare_maps(smallStr_map, tmp_map):
                resultant += bigStr[left: right+1],
            tmp_map[bigStr[left]] -= 1
            left += 1
        right += 1
    return resultant

def compare_maps(map1, map2):
    for key in map1:
        if key not in map2 or map2[key] != map1[key]:
            return False
    return True

if __name__ == '__main__':
    print(count_permutations('cbabcacabca', 'abc'))
