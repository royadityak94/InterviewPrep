# Python implementation of basic queue
import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return True if self.front is None else False
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = self.rear.next
    def dequeue(self):
        if self.is_empty is None:
            return None
        else:
            popped = self.front
            self.front = self.front.next
            popped.next = None
            return popped.data
    def peek(self):
        return self.front.data

    def display(self):
        if self.is_empty():
            print ("Empty Queue")
        else:
            iter_node = self.front
            while iter_node is not None:
                print (iter_node.data, "->", end=" ")
                iter_node = iter_node.next
            print ("")
        return
    def size(self):
        size = 0
        if not self.is_empty():
            iter_node = self.front
            while iter_node is not None:
                size += 1
                iter_node = iter_node.next
        return size


if __name__ == '__main__':
    elements = [2, 4, 1, 6, 5]
    q = Queue()
    for ele in elements:
        q.enqueue(ele)

    q.display()
    print ("Queue size = %d" % q.size())
    for i in range(len(elements)):
        print ("Element popped : %d" % q.dequeue())
    print ("Queue size = %d" % q.size())
