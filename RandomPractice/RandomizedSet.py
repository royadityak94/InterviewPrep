'''RandomizedSet class
Source: https://leetcode.com/problems/insert-delete-getrandom-o1/
'''
from dataclasses import dataclass 
import random 

@dataclass
class RandomizedSet: 
    def __init__(self):
        self.items = []
        self.item_indexes = {}

    def insert(self, value) -> bool:
        if value in self.item_indexes:
            return False 
        self.items += value, 
        self.item_indexes[value] = len(self.items)-1
        return True 

    def remove(self, value) -> bool: 
        if value not in self.item_indexes:
            return False 
        index_to_remove = self.item_indexes[value]
        last_element = self.items[-1]

        # Swap the last element in the map
        self.item_indexes[last_element] = index_to_remove
        self.items[index_to_remove] = last_element

        # Remove the element from both list and dictionary
        self.item_indexes.pop(value)
        self.items.pop()
        return True

    def get_random(self):
        return random.choice(self.items)

def main():
    randomized_set = RandomizedSet()
    response_1 = randomized_set.insert(1)
    print (f'{response_1}, {randomized_set.items}, {randomized_set.item_indexes}')

    response_2 = randomized_set.remove(2)
    print (f'{response_2}, {randomized_set.items}, {randomized_set.item_indexes}')

    response_3 = randomized_set.insert(2)
    print (f'{response_3}, {randomized_set.items}, {randomized_set.item_indexes}')

    response_4 = randomized_set.get_random()
    print (f'Random value found is {response_4}')
    print (f'{randomized_set.items}, {randomized_set.item_indexes}')

    response_5 = randomized_set.remove(1)
    print (f'{response_5}, {randomized_set.items}, {randomized_set.item_indexes}')

    response_6 = randomized_set.insert(2)
    print (f'{response_6}, {randomized_set.items}, {randomized_set.item_indexes}')

    response_7 = randomized_set.get_random()
    print (f'Random value found is {response_7}, {randomized_set.items}, {randomized_set.item_indexes}')


if __name__ == '__main__':
    main()