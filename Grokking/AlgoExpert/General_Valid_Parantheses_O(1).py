'''
    Tried to implement: https://www.geeksforgeeks.org/check-balanced-parentheses-expression-o1-space/
    But left it, instead let's practice the stack version (again!)
'''

def isParanthesisValid(string):
    if not string:
        return True
    if len(string) % 2:
        return False
    openingIdentifiers = ['(', '{', '[']
    closingIdentifiers = [')', '}', ']']
    opening_closingMapper = {')': '(', '}': '{', ']': '['}
    runningStack = []
    for ch in string:
        if ch in openingIdentifiers:
            runningStack += ch,
        elif ch in closingIdentifiers:
            popped = runningStack.pop()
            if popped != opening_closingMapper[ch]:
                return False
    return len(runningStack) == 0


def isParanthesisValid_optimized(string):
    if not string:
        return True
    if len(string) % 2:
        return False

    openingIdentifiers = ['(', '{', '[']
    closingIdentifiers = [')', '}', ']']
    openingCount = 0
    closingCount = 0

    for ch in string:
        if ch in openingIdentifiers:
            openingCount += 1
        elif ch in closingIdentifiers:
            if not openingCount or closingCount+1 > openingCount:
                return False
            closingCount += 1
    return openingCount == closingCount


if __name__ == '__main__':
    print (isParanthesisValid_optimized('(()())[]'))
    print (isParanthesisValid_optimized('((){}()){}'))
    print (isParanthesisValid_optimized('{()())}'))
    print (isParanthesisValid_optimized('()(([]))'))
    print (isParanthesisValid_optimized('([])'))
    print (isParanthesisValid_optimized('([}])'))
