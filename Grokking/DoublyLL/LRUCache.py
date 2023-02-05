"""LRU (Least Recently Used)
Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Input: 
instructions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
data = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output: 
[null, null, null, 1, null, -1, null, -1, 3, 4]
"""

class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key 
        self.value = value 
        self.prev = prev 
        self.next = next 

class LRUCache: 
    def __init__(self, maximumSize):
        self.head = self.tail = None
        self.keys = dict()
        self.currentSize = 0
        self.maximumSize = maximumSize # Assumed to be a higher number

    def insert(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
            self.keys[key] = new_node
            self.currentSize += 1
            return 
        if self.currentSize + 1 > self.maximumSize:
            self.delete()

        last = self.tail 
        last.next = new_node
        new_node.prev = last 
        self.tail = new_node
        self.currentSize += 1
        self.keys[key] = new_node
        return 
    
    def delete(self, key=None): # Always from head 
        if not key:
            key = self.head.key 
        print (f"\tDeleting: {key} ")
        first = self.keys[key] 
        second = first.next 
        # Remove dangling pointers
        second.prev = None
        first.next = None 
        
        self.head = second 
        self.currentSize -= 1
        del self.keys[key]
        

    def get(self, key):
        if key not in self.keys:
            return -1
        value = self.keys[key]
        self.delete(key)
        self.insert(key, value)
        return value.value

    def put(self, key, value):
        if key in self.keys:
            self.delete(key)
        self.insert(key, value)
        return 


def main():
    instructions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    data = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    lru = LRUCache(*data[0])

    for idx in range(1, len(instructions)):
        if instructions[idx] == 'put':
            lru.put(*data[idx])
            print (f"\tInserted: {data[idx]}")
        elif instructions[idx] == 'get':
            requesting_for = data[idx]
            print(f'Requested for: {requesting_for}, got: {lru.get(*requesting_for)}')
        
main()