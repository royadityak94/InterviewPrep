'''
Given a balanced parentheses string S, compute the score of the string based on the following rule:
() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
'''

# O(n) time | O(n) space
def score_parantheses(string):
    openingBracket, closingBracket = '(', ')'
    finalCount = [0]

    for idx, ch in enumerate(string):
        if ch == openingBracket:
            finalCount += 0,
        elif ch == closingBracket:
            last_depth = finalCount.pop()
            finalCount[-1] += max(1, last_depth*2)
    return finalCount.pop()

# O(n) time | O(1) space
def score_parantheses_optimized(string):
    if not string:
        return 0
    openingBracket, closingBracket = '(', ')'
    netCount = 0
    finalScore = 0

    for idx, ch in enumerate(string):
        if ch == openingBracket:
            netCount += 1
        elif ch == closingBracket:
            netCount -= 1
            if string[idx-1] == openingBracket:
                finalScore += (2 ** netCount)
    return finalScore

if __name__ == '__main__':
    # naive approach
    print (score_parantheses('(())'))
    print (score_parantheses('()(())'))
    print (score_parantheses('((())())'))
    print (score_parantheses('(((((())))))'))

    # optimized approach
    print (score_parantheses_optimized('(())'))
    print (score_parantheses_optimized('()(())'))
    print (score_parantheses_optimized('((())())'))
    print (score_parantheses_optimized('(((((())))))'))
