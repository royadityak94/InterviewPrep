'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
'''

#
def is_valid_parantheses_string(string: str) -> bool:
    if not string:
        return True
    openingBrackets, closingBrackets = '(', ')'
    stack = []
    stars = []

    for idx, ch in enumerate(string):
        if ch == openingBrackets:
            stack += idx,
        elif ch == '*':
            stars += idx,
        elif ch == closingBrackets:
            if len(stack):
                stack.pop()
            elif len(stars):
                stars.pop()
            else:
                return False
    while stack and stars:
        if stack[-1] < stars[-1]:
            stack.pop()
            stars.pop()
        else:
            break
    return len(stack) == 0


def is_valid_parantheses_string_optimized(string):
    if not string:
        return True

    left = right = 0
    n = len(string)

    for idx, ch in enumerate(string):
        if ch in '(*':
            left += 1
        else:
            left -= 1

        if string[n-idx-1] in '*)':
            right += 1
        else:
            right -= 1

        if left < 0 or right < 0:
            return False
    return True



if __name__ == '__main__':
    # Naive
    assert is_valid_parantheses_string('()') == True
    assert is_valid_parantheses_string('(*)') == True
    assert is_valid_parantheses_string('(*))') == True
    assert is_valid_parantheses_string(')(') == False

    # Optimized
    assert is_valid_parantheses_string_optimized('()') == True
    assert is_valid_parantheses_string_optimized('(*)') == True
    assert is_valid_parantheses_string_optimized('(*))') == True
    assert is_valid_parantheses_string_optimized(')(') == False
