'''
Given a balanced parentheses string S, compute the score of the string based on the following rule:
() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
'''

# O(n) time | O(n) space
def score_parantheses(string):
    if not string:
        return 0

    openingBracket, closingBracket = '(', ')'
    finalCount = [0]

    for ch in string:
        if ch in openingBracket:
            finalCount += 0,
        else:
            last_depth = finalCount.pop()
            finalCount[-1] += max(1, 2*last_depth)
    return finalCount.pop()

# O(n) time | O(1) space
def score_parantheses_optimized(string):
    if not string:
        return 0

    openingBracket, closingBracket = '(', ')'
    netCount, finalScore = 0, 0

    for idx, ch in enumerate(string):
        if ch == openingBracket:
            netCount += 1
        elif ch == closingBracket:
            netCount -= 1
            if string[idx-1] == openingBracket:
                finalScore += (1 << netCount)
    return finalScore

if __name__ == '__main__':
    # naive approach
    print (score_parantheses('(())'))
    print (score_parantheses('()(())'))
    print (score_parantheses('((())())'))
    print (score_parantheses('((()))'))
    print (score_parantheses('(((((()))))'))

    # optimized approach
    print (score_parantheses_optimized('(())'))
    print (score_parantheses_optimized('()(())'))
    print (score_parantheses_optimized('((())())'))
    print (score_parantheses_optimized('((()))'))
    print (score_parantheses_optimized('(((((()))))'))
