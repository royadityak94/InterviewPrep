'''
Remove the minimum number of invalid parentheses in order to make the input string valid.
Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).
'''

def isValid(string: str) -> bool:
    openingBrackets, closingBrackets = '(', ')'
    netCount = 0
    for ch in string:
        if ch == openingBrackets:
            netCount += 1
        elif ch == closingBrackets:
            if not netCount:
                return False
            netCount -= 1
    return netCount == 0

def remove_invalid_parantheses(string):
    if isValid(string):
        return ['']
    openingBrackets, closingBrackets = '(', ')'
    output = []
    queue = [string]
    visited = set(queue)
    isFound = False

    while queue:
        current = queue.pop(0)
        if isValid(current):
            output += current,
            isFound = True

        if isFound:
            continue

        for idx, ch in enumerate(current):
            if ch not in (openingBrackets, closingBrackets):
                continue
            others = current[:idx] + current[idx+1:]
            if others not in visited:
                visited.add(others)
                queue += others,

    return output if len(output) else ['']

if __name__ == '__main__':
    print (remove_invalid_parantheses('()())()'))
    print (remove_invalid_parantheses('()()'))
