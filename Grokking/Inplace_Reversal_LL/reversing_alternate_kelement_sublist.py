# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
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

def reverse_alternate_k_elements(head, k):
    # Time Complexity: O(N), Space Complexity: O(1)
    if not head or k < 2:
        return head

    prev, curr = None, head
    while True:
        last_node_left = prev
        last_node_sublist = curr

        cnt = 0
        while curr and cnt < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            cnt += 1

        if last_node_left:
            last_node_left.next = prev
        else:
            head = prev

        last_node_sublist.next = curr

        cnt = 0
        while curr and cnt < k:
            prev, curr, cnt = curr, curr.next, cnt+1

        if not curr:
            break
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()
