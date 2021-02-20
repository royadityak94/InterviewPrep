'''
Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.
1+2*3 => (7, 9) {1+(2*3) => 7 and (1+2)*3 => 9}
2*3-4-5 => (8, -12, 7, -7, -3) {2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3}
'''

def eval_expressions(string):
    resultant = []
    if not any([opr in string for opr in ('+', '-', '*')]):
        resultant += int(string),
    else:
        for i in range(len(string)):
            chr = string[i]
            if not chr.isdigit():
                left = eval_expressions(string[:i])
                right = eval_expressions(string[i+1:])
                for part1 in left:
                    for part2 in right:
                        if chr == '+':
                            resultant += part1 + part2,
                        elif chr == '-':
                            resultant += part1 - part2,
                        elif chr == '*':
                            resultant += part1 * part2,
    return resultant

if __name__ == '__main__':
    print ("Got: ", eval_expressions('1+2*3'))
    print ("Got: ", eval_expressions('2*3-4-5'))
    assert eval_expressions('1+2*3') == [7, 9]
    assert eval_expressions('2*3-4-5') == [8, -12, 7, -7, -3]
