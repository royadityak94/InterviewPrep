'''
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as openning parenthesis and '))' as closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.
'''

def min_insertions_1(string):
    stack = []
    opening, closing = '(]'

    # Pre-processing
    insertion_cnt = 0
    string = string.replace('))', closing)
    insertion_cnt += string.count(')')
    string = string.replace(')', closing)


    for idx, ch in enumerate(string):
        if ch == opening:
            stack += idx,
        elif ch == closing:
            if not stack:
                insertion_cnt += 1
            else:
                stack.pop()

    insertion_cnt += (len(stack)*2)
    return insertion_cnt


def min_insertions_2(string):
    opening, closing = '()'
    required = right = 0
    for ch in string:
        if ch == opening:
            if right % 2:
                right -= 1
                required += 1
            right += 2
        elif ch == closing:
            right -= 1
            if right < 0:
                right += 2
                required += 1
    return required + right



if __name__ == '__main__':
    # approach 1
    assert min_insertions_1('(()))') == 1
    assert min_insertions_1('())') == 0
    assert min_insertions_1('))())(') == 3
    assert min_insertions_1('((((((') == 12
    assert min_insertions_1(')))))))') == 5

    # approach 2
    assert min_insertions_2('(()))') == 1
    assert min_insertions_2('())') == 0
    assert min_insertions_2('))())(') == 3
    assert min_insertions_2('((((((') == 12
    assert min_insertions_2(')))))))') == 5
