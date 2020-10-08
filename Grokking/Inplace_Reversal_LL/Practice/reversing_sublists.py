# Reversing sublist of a given linked list (in-place)
#Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’
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

def reverse_sub_list(head, p, q):
    tail = head
    k = 0
    prev = None
    while k != p:
        prev = head
        head = head.next
        k += 1

    last_node_left = prev
    first_node_right = head

    while k != q:
        next = head.next
        head.next = prev
        prev = head
        head = next
        k += 1

    if last_node_left:
        last_node_left.next = prev
    else:
        tail = prev
    first_node_right.next = head
    return tail


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 1, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
