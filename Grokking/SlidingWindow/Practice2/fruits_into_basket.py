# Given an array of characters where each character represents a fruit tree,
# are given two baskets and your goal is to put maximum number of fruits in each basket.
# The only restriction is that each basket can have only one type of fruit.
from collections import defaultdict

# O(n + n ~ n) time | O(1) space
def maximum_fruits_in_two_baskets(baskets):
    ws_start = 0
    counter = defaultdict(int)
    maxFruits = float('-inf')
    for ws_end in range(len(baskets)):
        rightFruit = baskets[ws_end]
        counter[rightFruit] += 1
        if len(counter) > 2:
            leftFruit = baskets[ws_start]
            counter[leftFruit] -= 1
            if not counter[leftFruit]:
                del counter[leftFruit]
            ws_start += 1
        maxFruits = max(maxFruits, (ws_end - ws_start + 1))
    return maxFruits


if __name__ == '__main__':
    print (maximum_fruits_in_two_baskets(['A', 'B', 'C', 'A', 'C'])) # 3
    print (maximum_fruits_in_two_baskets(['A', 'B', 'C', 'B', 'B', 'C'])) # 5
