
# Naive Case: O(n) time | O(n) space
def valid_parantheses_naive(string):
    openingBracket, closingBracket = '(', ')'
    stack = []

    for ch in string:
        if ch == openingBracket:
            stack += ch,
        elif ch == closingBracket:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# Naive Case: O(n) time | O(1) space
def valid_parantheses_optimized(string):
    openingBracket, closingBracket = '(', ')'
    netCount = 0

    for ch in string:
        if ch == openingBracket:
            netCount += 1
        elif ch == closingBracket:
            if not netCount:
                return False
            netCount -= 1
    return netCount == 0


if __name__ == '__main__':
    # Read all parantheses from the file
    all_parantheses = []
    with open('examples_parantheses.txt') as file:
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
        else:
            matched += 1
    print ("Matched: %d out of %d" % (matched, len(all_parantheses)))
