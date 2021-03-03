'''
Applications of XOR to problem-solving
'''
import random
from typing import List

def swap_arr(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def get_random_arr():
    k = random.randint(5, 10)
    arr = random.sample(range(0, k), k)
    del_idx = random.randint(0, len(arr)-1)
    missing = arr[del_idx]
    swap_arr(del_idx, len(arr)-1, arr)
    arr.pop()
    return arr, missing

# O(1) time | O(1) space
def swap(a:int, b:int):
    a = a ^ b
    b = b ^ a
    a = a ^ b
    return a, b

# O(n) time | O(1) space
def single_missing_number(arr: List[int]) -> int:
    missing = 0
    for ele in arr:
        missing ^= ele
    return missing

# O(n) time | O(1) space
def missing_number_range(arr: List[int]) -> int:
    n = len(arr) # range: [0, n] with 1 element missing, else actual size=n+1
    resultant = n
    for idx, ele in enumerate(arr):
        resultant ^= idx
        resultant ^= ele
    #print ("Got missing as: ", resultant)
    return resultant

# O(1) time | O(1) space
def opposite_signs(num1: int, num2: int) -> bool:
    # xor of two numbers with opposite sign is always negative
    return (num1 ^ num2) < 0

if __name__ == '__main__':
    # Swapping two numbers using xor
    assert swap(10, 20) == (20, 10)

    # Single Missing number in array: All numbers present in pair except for one
    arr = [random.randint(1, 20) for _ in range(10)] * 2
    assert single_missing_number(arr[:-1]) == arr[-1]

    # Detecting if two integers have opposite signs
    assert opposite_signs(-5, 5) == True
    assert opposite_signs(5, 7) == False
    assert opposite_signs(-4, -4) == False

    # Missing number - Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    arr, missing = get_random_arr()
    assert missing_number_range(arr) == missing
