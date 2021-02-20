# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
# Input: N=2, O/p: (()), ()()
# Input: N=3, O/p: ((())), (()()), (())(), ()(()), ()()()
from collections import deque, Counter

# O(N * 2^N) time | O(N * 2^N) -> Catalan Number: O(4^N / (N ^ .5))
def generate_valid_parentheses(num):
    generated = []
    parantheses = [None for _ in range(num * 2)]
    generate_valid_parentheses_rec(num, 0, 0, parantheses, 0, generated)
    return generated

def generate_valid_parentheses_rec(num, openCount, closeCount, parantheses, currIdx, generated):
    if openCount == num and closeCount == num:
        generated += ''.join(parantheses),
    else:
        if openCount < num:
            parantheses[currIdx] = '('
            generate_valid_parentheses_rec(num, openCount+1, closeCount, parantheses, currIdx+1, generated)
        if openCount > closeCount:
            parantheses[currIdx] = ')'
            generate_valid_parentheses_rec(num, openCount, closeCount+1, parantheses, currIdx+1, generated)

def main():
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))
main()


# ['(())', '()()'], ['((()))', '(()())', '(())()', '()(())', '()()()']
