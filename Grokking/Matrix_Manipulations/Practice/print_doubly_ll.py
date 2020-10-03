# Python program to initialize and print doubly ll
class LinkedList:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def convert_to_ll(arr):
    if not arr:
        return None

    prev = None
    head = tail = LinkedList(arr[0])

    for ele in arr[1:]:
        tail.prev = prev
        tail.next = LinkedList(ele)
        prev = tail
        tail = tail.next
    tail.prev = prev
    return head

def print_ll(head):
    if not head:
        return
    print ("---------------------")
    print("Prev\tCurr\tNext")
    while head:
        if not head.prev and not head.next:
            print("%s\t%d\t%s" % (None, head.data, None))
        elif not head.prev:
            print("%s\t%d\t%d" % (None, head.data, head.next.data))
        elif not head.next:
            print("%d\t%d\t%s" % (head.prev.data, head.data, None))
        else:
            print("%d\t%d\t%d" % (head.prev.data, head.data, head.next.data))
        head = head.next
    return

def delete_ll(head, ele):
    if not head:
        return None

    prev = None
    tail = head

    while tail:
        if tail.data == ele:
            if not prev:
                if not tail.next:
                    return None
                else:
                    head = tail.next
            else:
                prev.next = tail.next
            if tail.next:
                tail.next.prev = prev
        else:
            prev = tail
        tail = tail.next
    return

def reverse_ll(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next
    return prev


def main():
    arr = [2, 4, 2, 3, 6, 5, 4, 8, 9, 2, 4, 2]
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


    # Reversing doubly ll
    print (" --------------- Reversed ---------------")
    arr = [2, 4, 2, 3, 6, 5, 4, 8, 9, 3, 6, 1]
    head = convert_to_ll(arr)
    print_ll(head)

    print_ll(reverse_ll(head))

main()
