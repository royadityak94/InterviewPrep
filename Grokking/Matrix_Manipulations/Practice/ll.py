
class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def convert_to_ll(arr):
    if not arr:
        return None

    head = tail = LinkedList(arr[0])

    for ele in arr[1:]:
        tail.next = LinkedList(ele)
        tail = tail.next
    return head

def print_ll(head):
    while head:
        print (head.data, end = ' -> ')
        head = head.next
    print()
    return

def delete_ll(head, ele):
    prev = None
    tail = head
    while head:
        if head.data == ele:
            if not prev:
                if not head.next:
                    return None
                else:
                    tail = head.next
            else:
                prev.next = head.next
        prev = head
        head = head.next
    return tail

def reverse_ll(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def main():
    arr = [2, 4, 2, 3, 6, 5, 4, 8, 9, 1, 5, 2]
    head = convert_to_ll(arr)
    print_ll(head)

    head = delete_ll(head, 2) # delete all 4
    print_ll(head)

    print ("----------------------")
    arr = [4]
    head = convert_to_ll(arr)
    print_ll(head)
    head = delete_ll(head, 4) # delete all 4
    print_ll(head)

    # Simple Reversal
    arr = [2, 4, 2, 3, 6, 5, 4, 8, 9, 1, 5, 2]
    head = convert_to_ll(arr)
    print_ll(reverse_ll(head))

main()
