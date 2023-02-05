""" Flatten a multilevel doubly LL
Source: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child 
pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. 
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the 
example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, 
doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before 
curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.
"""

class Node: 
    def __init__(self, val, prev, next, child):
        self.val = val 
        self.prev = prev 
        self.next = next 
        self.child = child 

''' Core Logic 
Visit along the head, until the child node points to non-null. 
If that happens, traverse along child but put the current node next in stack to come back to
'''

class FlattenMultilevel:
    def __init__(self):
        self.head = self.tail = None 

    def insert(self, data, prev, next, child, tail=None):
        new_node = Node(data, prev, next, child)
        if not tail:
            current = self.tail 
        current.next = new_node
        new_node.prev = current
        self.tail = current
        return

    def flatten(self):
        current = self.head 
        stack = []
        while stack or current: 
            if current: 
                if not current.child:
                    next_ = current.next 
                    next_.prev = current
                    current.next = current 
                else:
                    stack += current.next, 
                    current = current.child.next
            else: 
                current = stack.pop()
        return self.head 


