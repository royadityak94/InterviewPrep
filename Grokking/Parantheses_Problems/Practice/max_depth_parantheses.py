
# Naive Implementation: O(n) time | O(n) space
def max_depth_parantheses(string):
    openingBracket, closingBracket = '(', ')'
    maxDepth = [0]

    for ch in string:
        if ch == openingBracket:
            maxDepth += 0,
        elif ch == closingBracket:
            popped = maxDepth.pop()
            maxDepth[-1] = max(maxDepth[-1], 1 + popped)
    return maxDepth[-1]

# Optimized Implementation: O(n) time | O(1) space
def max_depth_parantheses_optimized(string):
    openingBracket, closingBracket = '(', ')'
    netCount = 0
    maxDepth = float('-inf')

    for ch in string:
        if ch == openingBracket:
            netCount += 1
        elif ch == closingBracket:
            maxDepth = max(maxDepth, netCount)
            netCount -= 1
    return maxDepth if maxDepth > float('-inf') else 0


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
