""""Practice linkedlist based fast and slow pointers"""

# Node implementation with next and value
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next 

# iterate using .next until current is None, and keep printing using .value
def print_ll(head) -> None:
    while (head):
        print (head.value, end='->')
        head = head.next 
    print ()

# Start with a node in the cycle, keep iterating until current = head, and the counter value is the cycle length
def compute_cycle_length(head):
    current = head 
    cycle_length = 0
    while True:
        cycle_length += 1
        current = current.next 
        if current == head:
            break 
    return cycle_length

# Use fast and slow pointers, to meet at the cycle 
def find_cycle_length(head):
    slow = fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return compute_cycle_length(slow)
    return 0


# Compute middle node by using fast move to end, and wherever slow is, that's the middle
def compute_middle_node(head):
    slow = fast = head 
    while fast and fast.next: 
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast: 
            break 
    return slow 

# Prev will become head, Head will become next -> (prev, head, next): prev = head, head = next
def reverse_ll(head):
    prev = None 
    while head: 
        next = head.next 
        head.next = prev 
        prev = head
        head = next 
    return prev 

# Get cycle length, move fast pointer 'cycle length' ahead. Use slow pointer to meet with fast
def print_start_of_cycle(head, cycle_length):
    slow = fast = head 
    while cycle_length:
        fast = fast.next 
        cycle_length -= 1
    while slow != fast: 
        slow = slow.next 
        fast = fast.next 
    return slow.value

# Find middle node, reverse from middle, compare (beginning to middle) with reveresed (middle to next)
def is_palindromic_linked_list(head):
    middle_node = compute_middle_node(head)
    reversed_second_half = reverse_ll(middle_node)

    while (head and reversed_second_half):
        if (head.value != reversed_second_half.value):
            return False 
        head = head.next 
        reversed_second_half = reversed_second_half.next 
    
    if (not head) and (not reversed_second_half):
        return True 
    return False

def squared(num):
    sum_of_squared_digits = 0
    while num:
        num, rem = divmod(num, 10)
        sum_of_squared_digits += (rem * rem)
    return sum_of_squared_digits 

def is_happy_number(num):
    fast = slow = num 
    while True: 
        slow = squared(slow)
        fast = squared(squared(fast))
        if fast == slow: 
            break
    return slow == 1

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Print Linkedlist
    print_ll(head)

    # Find cycle of LinkedList -> Traverse fast and slow pointer until they meet (that's where cycle is) -> compute the length following it
    head.next.next.next.next.next.next = head.next.next
    print ('Cycle Length = %d' % find_cycle_length(head))
    print ('Cycle Start: %d' % print_start_of_cycle(head, find_cycle_length(head)))


    # Check if a linkedlist is pallindrome -> Find middle, reverse from midlle, then compare
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    # Happy Number (using fast and slow pointers) -> 
    """Happy Number is such that when squared for its digit iteratively, it ultimately returns 1 
    Ex: 19, (1 + 81 = 82) -> (64 + 4 68) -> (36+64=100) -> (1+0+0 = 1)
    32, (9+4 = 13) -> (1 + 9 = 10) -> (1 + 0 = 0) 
    33 -> Not Happy Number
    """
    print (f'Is Happy Number: {is_happy_number(19)}') # True
    print (f'Is Happy Number: {is_happy_number(32)}') # True
    print (f'Is Happy Number: {is_happy_number(33)}') # False

main()