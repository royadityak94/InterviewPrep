class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

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
def is_palindromic_linked_list(head):
    # TODO: Write your code here
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    reversed_head = reverse_ll(slow)
    copyOfReversedHead = reversed_head
    current = head

    while reversed_head:
        if reversed_head.value != current.value:
            return False
        reversed_head = reversed_head.next
        current = current.next

    reverse_ll(copyOfReversedHead)
    return True



def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
