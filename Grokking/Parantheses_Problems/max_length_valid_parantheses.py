'''
We need to determine the length of the largest valid substring of parentheses from a given string.
'''
# O(n) time | O(n) space
def max_length_balanced(string):
    if not string:
        return 0
    openingBracket, closingBracket = '(', ')'
    maxLength = float('-inf')
    stack = []

    for idx, ch in enumerate(string):
        if ch == openingBracket:
            stack += idx,
        elif ch == closingBracket:
            prev_idx = stack.pop()
            maxLength = max(maxLength, (idx-prev_idx+1))
    return maxLength if maxLength > float('-inf') else 0

def return_max_length(string:str, forward: bool = True) -> int:
    openingBracket, closingBracket = '(', ')'
    maxLength = float('-inf')
    left = right = 0
    for ch in string:
        if ch == openingBracket:
            left += 1
        elif ch == closingBracket:
            right += 1

        if left == right:
            maxLength = max(maxLength, left*2)
        elif forward:
            if right > left:
                left = right = 0
        elif left > right:
            left = right = 0
    return maxLength if maxLength > float('-inf') else 0

# O(n) time | O(1) space
def max_length_balanced_optimized(string):
    if not string:
        return 0

    maxLengthForward = return_max_length(string, True)
    maxLengthReverse = return_max_length(string[::-1], False)
    return max(maxLengthForward, maxLengthReverse)

if __name__ == '__main__':
    # naive case
    assert max_length_balanced('((())') == 4
    # optimized case
    assert max_length_balanced_optimized('((())') == 4
    assert max_length_balanced_optimized('()(()()') == 2
