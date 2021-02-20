# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
# Input: N=2, O/p: (()), ()()
# Input: N=3, O/p: ((())), (()()), (())(), ()(()), ()()()
from collections import deque, Counter

def generate_valid_parentheses(num):
    generated = []
    current = [None for _ in range(num*2)]
    generate_valid_parentheses_rec(num, 0, 0, current, 0, generated)
    return generated

def generate_valid_parentheses_rec(num, openCount, closeCount, current, currentIdx, generated):
    if openCount == num and closeCount == num:
        generated += ''.join(current),
        return

    if openCount < num:
        current[currentIdx] = '('
        generate_valid_parentheses_rec(num, openCount+1, closeCount, current, currentIdx + 1, generated)
    if openCount > closeCount:
        current[currentIdx] = ')'
        generate_valid_parentheses_rec(num, openCount, closeCount+1, current, currentIdx + 1, generated)

def main():
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))

    #check_unbalanced("(())()(")

main()
