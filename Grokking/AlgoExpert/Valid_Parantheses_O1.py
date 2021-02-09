'''
    Valid parantheses without stack
'''

def  isParanthesisValid(string):
    if not string:
        return True
    if len(string) % 2:
        return False
    openingBracket, closingBracket = '(', ')'
    left = 0
    for ch in string:
        if ch == closingBracket:
            if not left:
                return False
            left -= 1
        else:
            left += 1

    if left:
        return False

    right = 0
    for ch in string[::-1]:
        if ch == openingBracket:
            if not right:
                return False
            right -= 1
        else:
            right += 1

    if right:
        return False
    return True


if __name__ == '__main__':
    print (isParanthesisValid('(()())()'))
    print (isParanthesisValid('(()(()))()'))
    print (isParanthesisValid('())'))
    print (isParanthesisValid('()(())'))
    print (isParanthesisValid('('))
    print (isParanthesisValid(')'))
