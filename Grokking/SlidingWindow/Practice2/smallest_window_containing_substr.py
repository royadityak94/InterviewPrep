
def find_substring(string, pattern):
    counter = {}
    for ch in pattern:
        if ch not in counter:
            counter[ch] = 0
        counter[ch] += 1

    ws_start = 0
    matched = 0
    smallestLength = float('inf')
    optimum_ws_start = None

    for ws_end in range(len(string)):
        rightChar = string[ws_end]
        if rightChar in counter:
            counter[rightChar] -= 1
            if counter[rightChar] == 0:
                matched += 1

        while matched == len(counter):
            current_length = ws_end - ws_start + 1
            if current_length < smallestLength:
                smallestLength = current_length
                optimum_ws_start = ws_start

            leftChar = string[ws_start]
            if leftChar in counter:
                if counter[leftChar] == 0:
                    matched -= 1
                counter[leftChar] += 1
            ws_start += 1

    return string[optimum_ws_start: optimum_ws_start+current_length] \
        if optimum_ws_start is not None else ''


if __name__ == '__main__':
    print (find_substring('aabdec', 'abc')) #abdec
    print (find_substring('abdbca', 'abc')) #bca
    print (find_substring('adcad', 'ac')) #'ca'
