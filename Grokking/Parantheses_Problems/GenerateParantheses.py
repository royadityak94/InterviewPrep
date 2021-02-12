'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
from typing import List

def isValid(sequence: List[str]) -> bool:
    netCount = 0
    for ch in sequence:
        if ch in '(':
            netCount += 1
        else:
            if not netCount:
                return False
            netCount -= 1
    return netCount == 0

# O(n * (2 ^ (2n))) time | O(2 ^ (2n)) space
def generate_parantheses_naive(n: int) -> List[int]:
    combinations = []
    generate_parantheses_naiveHelper([], n, combinations)
    return combinations

def generate_parantheses_naiveHelper(arr: List[int], n: int, combinations: List[int]):
    if len(arr) == 2*n:
        if isValid(arr):
            combinations += ''.join(arr),
    else:
        for ch in ['(', ')']:
            arr += ch,
            generate_parantheses_naiveHelper(arr, n, combinations)
            arr.pop()

# O((4^n)/(n^.5)) time | O((4^n)/(n^.5)) space
def generate_parantheses_optimized(n:int) -> List[int]:
    combinations = []
    generate_parantheses_optimizedHelper('', n, n, combinations)
    return combinations

def generate_parantheses_optimizedHelper(string: str, low: int, high: int, combinations: List[int]):
    if low > high or low < 0 or high < 0:
        return

    if low == high == 0:
        combinations += string,
        return
    generate_parantheses_optimizedHelper(string+'(', low-1, high, combinations)
    generate_parantheses_optimizedHelper(string+')', low, high-1, combinations)







if __name__ == '__main__':
    n = 3
    expected = ["((()))","(()())","(())()","()(())","()()()"]
    # naive solution
    print(generate_parantheses_naive(n), generate_parantheses_naive(n)==expected)

    # Optimized solution
    print(generate_parantheses_optimized(n), generate_parantheses_optimized(n) == expected)
