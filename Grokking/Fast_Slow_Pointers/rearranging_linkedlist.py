# Verify if a given linked list is pallindrome or not
# Strategy: Find the middle Node, Reverse the other half, check item by item, and then re-reverse the reversed half.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print (temp.value, end=" ")
            temp = temp.next
        print()

def add_to_ll(arr):
    head = Node(arr[0])
    start = head
    for ele in arr[1:]:
        start.next = Node(ele)
        start = start.next
    return head

def reverse_ll(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev, head = head, next
    return prev

def reorder_1(head):
    # Time Complexity: O(N), Space Complexity: O(1)
    if head is None or head.next is None:
        return head
    # Finding the middle node
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reversing the second half
    reversed_half = reverse_ll(slow)

    while head is not None and reversed_half is not None:
        tmp = head.next
        head.next = reversed_half
        head = tmp

        tmp = reversed_half.next
        reversed_half.next = head
        reversed_half = tmp

    if head is not None:
        head.next = None

def reorder_2(head):
    # Time Complexity: O(N), Space Complexity: O(1)
    if head is None or head.next is None:
        return head
    # Finding the middle node
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    first_half, second_half = head, slow.next

    while first_half is not None and second_half is not None:
        temp = first_half.next
        first_half.next = second_half
        first_half = temp

        temp = second_half.next
        second_half.next = first_half
        second_half = temp

    if first_half is not None:
        first_half.next = None

def main():
    # Deploying first pattern
    # Op : 2, 10, 4, 8, 6
    head = add_to_ll([2, 4, 6, 8, 10, 12])
    head.print_list()
    reorder_1(head)
    head.print_list()

    # Deploying second pattern
    # Op : 2, 8, 4, 10, 6
    head = add_to_ll([2, 4, 10, 15, 18, 20])
    head.print_list()
    reorder_2(head)
    head.print_list()

main()
