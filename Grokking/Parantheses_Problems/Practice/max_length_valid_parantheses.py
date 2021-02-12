'''
We need to determine the length of the largest valid substring of parentheses from a given string.
'''
# O(n) time | O(n) space
def max_length_balanced(string):
    openingBracket= '('
    closingBracket= ')'
    stack = []
    maxLength = float('-inf')

    for idx, ch in enumerate(string):
        if ch in openingBracket:
            stack += idx,
        elif ch in closingBracket:
            if stack:
                last_idx = stack.pop()
                maxLength = max(maxLength, (idx - last_idx + 1))
    return maxLength if maxLength > float('-inf') else 0

def max_length_balanced_optimizedHelper(string, forward=True):
    openingBracket= '('
    closingBracket= ')'
    left = right = 0
    maxLength = float('-inf')

    for ch in string:
        if ch == openingBracket:
            left += 1
        elif ch == closingBracket:
            right += 1

        if left == right:
            base = right
            if not forward:
                base = left
            maxLength = max(maxLength, base*2)
        elif (forward and right > left) or (not forward and left > right):
            left = right = 0
    return maxLength if maxLength > float('-inf') else 0



# O(n+n ~ n) time | O(1) space
def max_length_balanced_optimized(string):

    leftToRight = max_length_balanced_optimizedHelper(string, True)
    rightToLeft = max_length_balanced_optimizedHelper(string[::-1], False)
    print ("Got: ", leftToRight, rightToLeft)
    return max(leftToRight, rightToLeft)

if __name__ == '__main__':
    # naive case
    # print ("Running Naive Cases")
    assert max_length_balanced('((())') == 4
    assert max_length_balanced('()(()()') == 2
    #
    # # optimized case
    # print ("Running Optimized Cases")
    assert max_length_balanced_optimized('((())') == 4
    assert max_length_balanced_optimized('()(()()') == 4
