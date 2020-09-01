# Verify if a given linked list is pallindrome or not
# Strategy: Find the middle Node, Reverse the other half, check item by item, and then re-reverse the reversed half.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_ll(head):
    while head is not None:
        print (head.value, end="->")
        head = head.next
    print ()
    return

def reverse_ll(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev, head = head, next
    return prev

def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True
    # Finding the middle node
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    # Reversing the second half
    second_half_reversed = second_half_reversed_copy = reverse_ll(slow)

    # Element-wise Comparison
    while head is not None and second_half_reversed is not None:
        if head.value != second_half_reversed.value:
            return False
        head, second_half_reversed = head.next, second_half_reversed.next

    # Re-reversing the reversed second half
    reverse_ll(second_half_reversed_copy)

    if head is None or second_half_reversed is None:
        return True

    return False

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)
  print_ll(head)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print_ll(head)
  #print_ll(reverse_ll(head))
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

main()
