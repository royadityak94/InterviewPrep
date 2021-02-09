
# O(N+M) time | O(M) space
def is_pattern_permutation_of_string(string, pattern):
    counter = {}
    for ch in pattern:
        if ch not in counter:
            counter[ch] = 0
        counter[ch] += 1

    ws_start = 0
    matched = 0
    for ws_end in range(len(string)):
        rightChar = string[ws_end]
        if rightChar in counter:
            counter[rightChar] -= 1
            if counter[rightChar] == 0:
                matched += 1

        if matched == len(counter):
            return True

        if ws_end >= len(pattern) - 1:
            leftChar = string[ws_start]
            ws_start += 1
            if leftChar in counter:
                if counter[leftChar] == 0:
                    matched -= 1
                counter[leftChar] += 1
    return False

if __name__ == '__main__':
    print (is_pattern_permutation_of_string('oidbcaf', 'abc'))
    print (is_pattern_permutation_of_string('odicf', 'dc'))
    print (is_pattern_permutation_of_string('bcdxabcdy', 'bcdyabcdx'))
    print (is_pattern_permutation_of_string('aaacb', 'abc'))
