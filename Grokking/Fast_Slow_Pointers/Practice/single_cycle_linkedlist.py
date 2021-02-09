class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# O(n) time | O(1) space
def has_cycle(head):
    # TODO: Write your code here
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print ("Cycle Length: ", cycle_length(slow))
            return True
    return False

# O(n) time | O(1) space
def cycle_length(head):
    current = head
    length = 0
    while True:
        current = current.next
        length += 1
        if current == head:
            break
    return length


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

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

main()
