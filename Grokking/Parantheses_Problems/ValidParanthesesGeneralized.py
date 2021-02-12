
# Naive Case: O(n) time | O(n) space
def valid_parantheses_naive(string: str) -> bool:
    if not string:
        return True
    elif (len(string) % 2):
        return False
    mapper = {')': '(', ']': '[', '}': '{'}
    closingBrackets = mapper.keys()
    openingBrackets = list(map(lambda key: mapper[key], mapper))
    stack = []
    for ch in string:
        if ch in openingBrackets:
            stack += ch,
        elif ch in closingBrackets:
            if (not stack) or stack.pop() != mapper[ch]:
                return False
    return len(stack) == 0

# N.B This fails for example 12 -
# https://afteracademy.com/blog/check-for-balanced-parentheses-in-an-expression (O(N^2) time | O(1) space)
def valid_parantheses_optimized(string: str) -> bool:
    if not string:
        return True
    elif (len(string) % 2):
        return False

    mapper = {')': '(', ']': '[', '}': '{'}

    for closingBrackets, openingBrackets in mapper.items():
        netCount = 0
        for ch in string:
            if ch in openingBrackets:
                netCount += 1
            elif ch in closingBrackets:
                if (not netCount):
                    return False
                netCount -= 1

        if netCount:
            return False
    return True

if __name__ == '__main__':
    # Read all parantheses from the file
    all_parantheses = []
    with open('examples_parantheses_general.txt') as file:
        file_contents = file.read()
        for line in file_contents.split('\n'):
            all_parantheses += line,

    assert len(all_parantheses) > 0
    matched = 0

    # Naive case
    for idx, input_str in enumerate(all_parantheses):
        naive_result = valid_parantheses_naive(input_str)
        optimized_result = valid_parantheses_optimized(input_str)
        if naive_result != optimized_result:
            print (idx, naive_result, optimized_result, sep='\t')
            print (input_str)
        else:
            matched += 1
    print ("Matched: %d out of %d" % (matched, len(all_parantheses)))
