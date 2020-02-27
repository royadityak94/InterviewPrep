# Python program to implement Priority Queue using LinkedList
'''
Only 3 cases exists in Priority Queue based implementations:
1. Empty queue
2. (-:1) New node priority is lower than currently seen priorities
3. Insertion:
    3.A) (-:1,2) Mid-way insertion : Priority is somewhere mid-way
    3.B) (-:1,2) End-way insertion : Highest Priority seen so far - Insert at end.
'''

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty():
            self.front = new_node
            self.rear = self.front
        elif self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            previous, current = None, self.front
            while (current and current.priority <= new_node.priority):
                previous, current = current, current.next
            if current:
                previous.next = new_node
                new_node.next = current
            else:
                self.rear.next = new_node
                self.rear = self.rear.next
        return
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.front
            self.front = self.front.next
            popped_node.next = None
            if self.front is None:
                self.rear = None
            return popped_node.data
    def peek(self):
        return self.front.data

if __name__ == '__main__':
    q = PriorityQueue()
    elements = [(4, 3), (5, 1), (3, 2), (7, 1), (9, 2), (8, 1), (12, 3)]

    for ele, priority in elements:
        q.enqueue(ele, priority)

    for i in range(len(elements)):
        print ("Popped : %d" % q.dequeue() )
