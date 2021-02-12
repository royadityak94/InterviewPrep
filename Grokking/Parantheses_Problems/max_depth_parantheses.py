
# Naive Implementation: O(n) time | O(n) space
def max_depth_parantheses(string):
    openingBracket, closingBracket = '(', ')'
    stack = []
    maxDepth = 0

    for ch in string:
        if ch in openingBracket:
            stack += ch,
        elif ch in closingBracket:
            maxDepth = max(maxDepth, len(stack))
            stack.pop()
    return maxDepth

def max_depth_parantheses_optimized(string):
    openingBracket, closingBracket = '(', ')'
    netCount = maxDepth = 0

    for ch in string:
        if ch == openingBracket:
            netCount += 1
        elif ch == closingBracket:
            maxDepth = max(maxDepth, netCount)
            netCount -= 1
    return maxDepth


if __name__ == '__main__':
    print ("Executing Naive Cases")
    assert max_depth_parantheses('(1+(2*3)+((8)/4))+1') == 3
    assert max_depth_parantheses('(1)+((2))+(((3)))') == 3
    assert max_depth_parantheses('1+(2*3)/(2-1)') == 1
    assert max_depth_parantheses('1') == 0

    print ("Executing Optimized Cases")
    assert max_depth_parantheses_optimized('(1+(2*3)+((8)/4))+1') == 3
    assert max_depth_parantheses_optimized('(1)+((2))+(((3)))') == 3
    assert max_depth_parantheses_optimized('1+(2*3)/(2-1)') == 1
    assert max_depth_parantheses_optimized('1') == 0
