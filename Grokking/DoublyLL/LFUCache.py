"""LRU (Least Recently Used)
Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). 
The use counter for a key in the cache is incremented either a get or put operation is called on it.
"""
from collections import Counter

class Node:
    def __init__(self, key, value, prev= None, next= None):
        self.key = key 
        self.value = value 
        self.prev = prev 
        self.next = next 
    def __gt__(self, another_self):
        return self.value > another_self.value

class LFUCache:
    def __init__(self, max_capacity, ):
        self.head = self.tail = None 
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.counter = Counter()

    def insert(self, key, value, current_key_value= 0):
        new_node = Node(key, value)

        # 1st insertion
        if not self.head: 
            self.head = self.tail = new_node
            self.counter[key] = (-1, new_node)
            self.current_capacity += 1
            return 
        # Already at full size
        if key not in self.counter and self.current_capacity + 1 > self.max_capacity:
            self.delete()

        # Pointer adjustment
        last = self.tail
        last.next = new_node
        new_node.prev = last 
        self.tail = new_node
        self.counter[key] = ((current_key_value-1), new_node)
        self.current_capacity += 1 
        return

    def delete(self, key=None):
        node = None
        if not key:
            key, (_, node) = self.counter.most_common(1)[0]
            
        else:
            _, node = self.counter[key]

        prev_node = node.prev 
        next_node = node.next 

        # Correct the node associations
        if prev_node:
            prev_node.next = next_node
        if next_node:  
            next_node.prev = prev_node
        node.prev = node.next = None 

        del self.counter[key]
        self.current_capacity -= 1
        return 
    
    def get(self, key):
        if key not in self.counter:
            return -1 
        count, node = self.counter[key]
        self.insert(key, node.value, count)
        return node.value 

    def put(self, key, value):
        current_key_value = 0
        if key in self.counter:
            current_key_value, _ = self.counter[key]
        self.insert(key, value, current_key_value)
        return

def main():
    instructions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    data = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    lfu = LFUCache(*data[0])

    for idx in range(1, len(instructions)):
        print(f'Current Counter = {lfu.counter}')
        if instructions[idx] == 'put':
            lfu.put(*data[idx])
            print (f"Inserted: {data[idx]}")
        elif instructions[idx] == 'get':
            requesting_for = data[idx]
            print(f'Requested for: {requesting_for}, got: {lfu.get(*requesting_for)}') 

main()