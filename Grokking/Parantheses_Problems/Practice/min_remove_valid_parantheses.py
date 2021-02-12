'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
'''

def min_removal_parantheses(string):
    string = list(string)
    openingBrackets, closingBrackets = '()'
    stack = []

    for idx, ch in enumerate(string):
        if ch == openingBrackets:
            stack += idx,
        elif ch == closingBrackets:
            if not stack:
                string[idx] = ''
            else:
                stack.pop()
    while stack:
        string[stack.pop()] = ''
    return ''.join(string)

if __name__ == '__main__':
    assert min_removal_parantheses('lee(t(c)o)de)') in ['lee(t(c)o)de', 'lee(t(co)de)', 'lee(t(c)ode)']
    assert min_removal_parantheses('a)b(c)d') == 'ab(c)d'
    assert min_removal_parantheses('))((') == ''
    assert min_removal_parantheses('(a(b(c)d)') in ['a(b(c)d)', '(ab(c)d)'], "Mismatch in value: "
