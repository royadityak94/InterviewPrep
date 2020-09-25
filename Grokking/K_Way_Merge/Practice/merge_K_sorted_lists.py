# Note: Programs in both kth_smallest_in_m_sortedlists and this file are same -
# Demonstrates working with ListNode (this file) and simple array list (next file)
# Given M sorted arrays, finding the K'th smallest number among them

# Python program to implement the merge - K sorted list to merge several sorted arrays
from heapq import heappush, heappop

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __lt__(self, other):
        return self.data < other.data

def initialize_list_nodes():
    l1 = ListNode(2)
    l1.next = ListNode(18)
    l1.next.next = ListNode(20)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(4)
    l3.next.next = ListNode(5)

    return l1, l2, l3

def merge_K_sorted_lists(lists):
    sortedArr = []
    for list in lists:
        heappush(sortedArr, list)

    head = tail = None
    while sortedArr:
        node = heappop(sortedArr)
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next

        if node.next:
            heappush(sortedArr, node.next)
    return head

def convert_lists_linkedlist(lists):
    ll_head_ptr = []

    for list in lists:
        head = tail = None
        for ele in list:
            if not head:
                head = tail = ListNode(ele)
            else:
                tail.next = ListNode(ele)
                tail = tail.next

        ll_head_ptr += head,

    return ll_head_ptr

def main():
    # Way - 1 : Hand-crafted LinkedList
    l1, l2, l3 = initialize_list_nodes()

    result = merge_K_sorted_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result is not None:
        print(str(result.data) + " ", end='')
        result = result.next
    print()

    # Finding kth smallest in the above list
    # l1, l2, l3 = initialize_list_nodes()
    # print ("Kth Smallest = ", find_Ksmallest_Msorted_lists([l1, l2, l3], 5))

    # Way - 2 : Converting list of lists into list of head pointers
    lists = [[2, 18, 20], [3, 6, 7], [1, 4, 5], [1, 1, 1], [24], [12, 13, 15, 17, 19]]
    ll_head_ptr = convert_lists_linkedlist(lists)
    result_arr = merge_K_sorted_lists(ll_head_ptr)
    print("Here are the elements form the merged list (Array-Version): ", end='')
    while result_arr is not None:
        print(str(result_arr.data) + " ", end='')
        result_arr = result_arr.next
    print()



main()
