# Python file to check if the paranthesis are balanced
import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Supported Operations: push, pop, peek, is_empty
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
        return
    def pop(self):
        if self.is_empty():
            return None
        else:
            popped = self.head
            self.head = popped.next
            popped.next = None
            return popped.data
    def peek(self):
        return None if self.is_empty() else self.head.data
    def display(self):
        if self.is_empty():
            print ("Stack Underflow !!")
        else:
            iter_node = self.head
            while iter_node != None:
                print (iter_node.data, "-> ", end=" ")
                iter_node = iter_node.next

def is_paranthesis_balanced(str_inp):
    ''' Module to perform paranthesis checking '''
    closed_paranthesis_map = {')':'(', '}': '{', ']':'['}
    open_paranthesis = [closed_paranthesis_map.get(key) for key in closed_paranthesis_map.keys()]

    paranStack = Stack()

    for ch in str_inp:
        if ch in open_paranthesis:
            paranStack.push(ch)
        elif ch in closed_paranthesis_map.keys():

            if closed_paranthesis_map.get(ch) != paranStack.pop():
                return False
        else:
            pass
    return True

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertTrue(is_paranthesis_balanced('{[()]}'))
    def test_case2(self):
        self.assertFalse(is_paranthesis_balanced('1s(45[){[()]}'))


if __name__ == '__main__':
    unittest.main()
