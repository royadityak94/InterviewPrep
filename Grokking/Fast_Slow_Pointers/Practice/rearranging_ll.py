from __future__ import print_function

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()

def reverse_ll(head):
    current = head
    previous = None
    while current:
        next_ = current.next
        current.next = previous
        previous = current
        current = next_
    return previous

# O(n) time | O(1) space
def reorder(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first_half = head
    second_half = reverse_ll(slow)

    while first_half and second_half:
        next_ = first_half.next
        first_half.next = second_half
        first_half = next_

        next_ = second_half.next
        second_half.next = first_half
        second_half = next_

    if first_half:
        first_half.next = None
    return

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    head.next.next.next.next.next.next = Node(15)
    reorder(head)
    head.print_list()

main()
