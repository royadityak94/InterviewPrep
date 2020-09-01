# Note: Programs in both kth_smallest_in_m_sortedlists and this file are same -
# Demonstrates working with ListNode (this file) and simple array list (next file)
# Given M sorted arrays, finding the K'th smallest number among them

# Python program to implement the merge - K sorted list to merge several sorted arrays
from __future__ import print_function
from heapq import heappush, heappop

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None
    # Used by heap
    def __lt__(self, other):
        return self.value < other.value

def merge_K_sorted_lists(lists):
    # Time Complexity: O(NLogK), Space Complexity: O(K)
    minElements = []
    for root in lists:
        heappush(minElements, root)

    head = tail = None
    while minElements:
        node = heappop(minElements)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next

        if node.next is not None:
            heappush(minElements, node.next)

    return head

def find_Ksmallest_Msorted_lists(lists, k):
    # Time Complexity: O(NLogK), Space Complexity: O(K)
    minElements = []
    for root in lists:
        heappush(minElements, root)

    head = tail = None
    while minElements:
        node = heappop(minElements)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next
        if node.next is not None:
            heappush(minElements, node.next)


    # Finding the kth smallest element
    current_count = 0
    while current_count < k-1:
        head = head.next
        current_count += 1

    return head.value

def initialize_list_nodes():
    l1 = ListNode(2)
    l1.next = ListNode(18)
    l1.next.next = ListNode(20)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    return l1, l2, l3

def main():
    l1, l2, l3 = initialize_list_nodes()

    result = merge_K_sorted_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result is not None:
        print(str(result.value) + " ", end='')
        result = result.next
    print()

    # Finding kth smallest in the above list
    l1, l2, l3 = initialize_list_nodes()
    print ("Kth Smallest = ", find_Ksmallest_Msorted_lists([l1, l2, l3], 5))

main()
