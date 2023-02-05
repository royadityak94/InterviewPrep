"""Implement Doubly LL as a single standalone class"""

class Node: 
    def __init__(self, data):
        self.data = data 
        self.prev = None 
        self.next = None 

class DoublyLL: 
    def __init__(self):
        self.head = self.tail = None 
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = Node(data)
            return 

        current_tail = self.tail 
        current_tail.next = new_node
        new_node.prev = self.tail 
        self.tail = new_node 
        return 

    def delete(self):
        if not self.head:
            return
        second_last = self.tail.prev 
        second_last.next = None 
        self.tail.prev = None 
        self.tail = second_last
        return 

    def deleteFromStart(self):
        if not self.head:
            return
        second = self.head.next 
        second.prev = None 
        self.head.next = None 
        self.head = second
        return 

    def printLL(self, message):
        if message:
            print (message)
        if not self.head:
            return 
        current = self.head 
        while (current):
            print (current.data, end= '->')
            current = current.next
        print ()
        return 


def main():
    doublyll = DoublyLL()
    elements = [5, 4, 3, 2, 1]
    for ele in elements:
        doublyll.insert(ele)

    doublyll.printLL("Full Insertion")
    
    # Remove #2 elements from tail, #1 elements from head 
    doublyll.delete() # Removes 1
    doublyll.printLL("Removed 1 item from tail")
    doublyll.delete() # Removes 2 
    doublyll.printLL("Removed 1 item from tail")
    doublyll.deleteFromStart() # Removes 1
    doublyll.printLL("Removed 1 item from head")


    

main()