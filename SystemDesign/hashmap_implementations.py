'''Hashmap Implementations
    Hashmap implementations in python
'''
import mmh3
import math

class ListNode: 
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None 

class HashMap: 
    def __init__(self, elements_count=1e4):
        self.buckets = int(math.sqrt(elements_count))
        self.array = [None for _ in range(self.buckets)]
    
    def get_hash(self, key):
        hash_value = mmh3.hash(key) % self.buckets 
        return hash_value 
    
    def put(self, key, value): 
        index = self.get_hash(key)
        current_node = self.array[index] 

        if not current_node: 
            node = ListNode(key, value)
            self.array[index] = node
            return 
        else: 
            while True: 
                if current_node.key == key:
                    current_node.value = value 
                    break 
                if not current_node.next: 
                    break 
                current_node = current_node.next 
            current_node.next = ListNode(key, value)
    

    def get(self, key): 
        index = self.get_hash(key)
        current_node = self.array[index] 

        if current_node:
            while True: 
                if current_node.key == key: 
                    return current_node.value 
                if not current_node.next: 
                    break 
                current_node = current_node.next
            
        return -1


    def remove(self, key):
        index = self.get_hash(key)
        current_node = previous_node = self.array[index] 

        if current_node:
            if current_node.key == key: 
                self.array[index] = current_node.next 
            else:
                current_node = current_node.next 
                while current_node.next:
                    if current_node.key == key: 
                        previous_node.next = current_node.next
                        break 
                    else:
                        previous_node, current_node = previous_node.next, current_node.next 
        return


def main(): 
    element_set = {'Chennai': 43, 'Kolkata': 32, 'Delhi': 12, 'Mumbai': 19}

    # Initialize the Hashmap 
    hashmap = HashMap()

    for key in element_set: 
        hashmap.put(key, element_set[key])

    # Print Status of elements
    for key in element_set: 
        _value = hashmap.get(key)
        print (f'Current {key} is found with value: {_value}')


    # Delete items 
    for key in ['Delhi', 'Mumbai']:
        hashmap.remove(key)

    # Print Status of elements
    for key in element_set: 
        _value = hashmap.get(key)
        print (f'Current {key} is found with value: {_value}')

    print (hashmap.array)

if __name__ == '__main__': 
    main()