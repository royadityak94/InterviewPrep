# Python program to implement the balanced paranthesis
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
    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_element = self.head
            self.head = self.head.next
            popped_element.next = None
            return popped_element.data
    def peek(self):
        return None if self.is_empty() else self.head.data

def is_paranthesis_balanced(string):
    base_stack = Stack()
    open_bracket_types = {')': '(', '}': '{', ']': '['}
    open_brackets = [open_bracket_types.get(key) for key in open_bracket_types.keys()]

    for ch in string:
        if ch in open_brackets:
            base_stack.push(ch)
        elif ch in open_bracket_types.keys():
            popped = base_stack.pop()
            if not (open_bracket_types.get(ch) == popped):
                print (popped, open_bracket_types.get(ch))
                return False
        else:
            pass
    return True


if __name__ == '__main__':
    input_str = '(abs)({sc}[)'
    print ("Is String = %s, balanced? - %r" % (input_str, is_paranthesis_balanced(input_str)))
