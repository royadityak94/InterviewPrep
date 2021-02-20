'''
Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.
1+2*3 => (7, 9) {1+(2*3) => 7 and (1+2)*3 => 9}
2*3-4-5 => (8, -12, 7, -7, -3) {2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3}
'''

def eval_expressions(string):
    return eval_expressions_rec(string)

def eval_expressions_rec(input):
    resultant = []
    if not  any([opr in input for opr in ['+', '-', '*']]):
        resultant += int(input),
        return resultant

    for idx in range(len(input)):
        if not input[idx].isdigit():
            left = eval_expressions_rec(input[:idx])
            right = eval_expressions_rec(input[idx+1:])
            for part1 in left:
                for part2 in right:
                    if input[idx] == '+':
                        resultant += part1 + part2,
                    elif input[idx] == '-':
                        resultant += part1 - part2,
                    elif input[idx] == '*':
                        resultant += part1 * part2,
    return resultant



if __name__ == '__main__':
    # print ("Got: ", eval_expressions('1+2*3'))
    # print ("Got: ", eval_expressions('2*3-4-5'))
    assert eval_expressions('1+2*3') == [7, 9]
    assert eval_expressions('2*3-4-5') == [8, -12, 7, -7, -3]
