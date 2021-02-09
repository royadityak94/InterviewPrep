# Given a string and a pattern, find all anagrams of the pattern in the given string.

# O(M+N) time | O(N) space
def find_string_anagrams(string, pattern):
    counter = {}
    for ch in pattern:
        if ch not in counter:
            counter[ch] = 0
        counter[ch] += 1

    ws_start = 0
    matched = 0
    matched_idxes = []
    for ws_end in range(len(string)):
        rightChar = string[ws_end]
        if rightChar in counter:
            counter[rightChar] -= 1
            if counter[rightChar] == 0:
                matched += 1

        if matched == len(counter):
            matched_idxes += ws_start,

        if ws_end >= len(pattern)-1:
            leftChar = string[ws_start]
            if leftChar in counter:
                if counter[leftChar] == 0:
                    matched -= 1
                counter[leftChar] += 1
            ws_start += 1
    return matched_idxes


if __name__ == '__main__':
    print (find_string_anagrams('ppqp', 'pq')) # [1, 2]
    print (find_string_anagrams('abbcabc', 'abc')) # [2, 3, 4]
    print (find_string_anagrams('aada', 'da')) # [1, 2]
