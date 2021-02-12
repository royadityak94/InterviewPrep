'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
from typing import List





if __name__ == '__main__':
    n = 3
    expected = ["((()))","(()())","(())()","()(())","()()()"]
    # naive solution
    print(generate_parantheses_naive(n), generate_parantheses_naive(n)==expected)

    # Optimized solution
    print(generate_parantheses_optimized(n), generate_parantheses_optimized(n) == expected)
