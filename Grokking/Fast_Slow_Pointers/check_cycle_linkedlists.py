# Fast & Slow Pointers (Hare & Tortoise Algorithm): Algo proves that two pointers are bound to meet: fast-pointer catched up with slow pointer once both pointers are in a cyclic loop!
# Determine if a linkedlist has cycle or not, given its head.

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    # Time Complexity: O(N), Space Complexity: O(1)
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

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
    # Time Complexity: O(N), Space Complexity: O(1)
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return compute_cycle_length(slow)
    return 0

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

main()
