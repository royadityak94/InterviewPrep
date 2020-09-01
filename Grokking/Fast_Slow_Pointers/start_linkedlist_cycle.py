# Finding the start of a linkedlist cycle
# Idea is to start with 2 pointers, push one pointer one cycle length ahead and wait for them to meet!

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def compute_cycle_length(slow):
    current = slow
    cycle_length = 0
    while current is not None:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length

def find_cycle_length(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return compute_cycle_length(slow)
    return 0

def find_cycle_start(head):
    # Time Complexity: O(N), Space Complexity: O(1)
    pointer1 = pointer2 = head
    cycle_length = find_cycle_length(head) # Cycle length

    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        
    return pointer2

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))



main()
