# Python program to check if the paranthesis are balanced
import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Push, Pop, Peek, Display
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return True if self.head is None else False
    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
    def display(self):
        if self.is_empty():
            print ("Stack Underflow")
        else:
            iter_node = self.head
            while iter_node is not None:
                if iter_node.next is not None:
                    print (iter_node.data, "->", end=" ")
                else:
                    print (iter_node.data)
                iter_node = iter_node.next
        return


class Test(unittest.TestCase):
    def test_case1(self):
        myStack = Stack()
        elements = [12, 34, 21, 45, 87, 19, 2]
        for ele in elements:
            myStack.push(ele)
        myStack.display()

        for i in range(len(elements)):
            print ("\nTop element after %d pop = %d" % (i, myStack.peek()))
            myStack.pop()

if __name__ == '__main__':
    unittest.main()
