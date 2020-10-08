# Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
          print(temp.value, end=" ")
          temp = temp.next
        print()

def ll_length(head):
    tail, length = head, 0
    while tail:
        length += 1
        tail = tail.next
    return length

def rotate(head, rotations):
    # Time Complexity: O(N), Space Complexity: O(1)
    ll_ = ll_length(head)
    rotations %= ll_

    prev, tail, cnt = None, head, 0
    while cnt < ll_ - rotations:
        prev = tail
        tail = tail.next
        cnt += 1

    prev.next = None
    new_head = tail

    while tail.next:
        tail = tail.next
    tail.next = head

    return new_head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 1)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()

main()
