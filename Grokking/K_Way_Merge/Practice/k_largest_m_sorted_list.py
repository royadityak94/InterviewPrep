from heapq import heappush, heappop

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __lt__(self, other):
        return self.data > other.data


def return_list_head_ptrs(lists):
    ll_head_ptrs = []

    for list_ in lists:
        head = tail = None
        for ele in list_:
            if not head:
                head = tail = ListNode(ele)
            else:
                tail.next = ListNode(ele)
                tail = tail.next

        ll_head_ptrs += head,

    return ll_head_ptrs


def k_largest_in_m_sortedlist(lists, k):
    ll_head_ptrs = return_list_head_ptrs(lists)
    minElements = []

    for head in ll_head_ptrs:
        heappush(minElements, head)

    tail = None
    counter = 0
    while minElements:
        node = heappop(minElements)
        counter += 1
        if counter == k:
            return node.data

        if not tail:
            tail = node
        else:
            tail.next = node
            tail = tail.next

        if node.next:
            heappush(minElements, node.next)
    return -1

def merge_m_sorted_lists(lists):
    ll_head_ptrs = return_list_head_ptrs(lists)
    minElements = []

    for head in ll_head_ptrs:
        heappush(minElements, head)

    head = tail = None
    counter = 0

    while minElements:
        node = heappop(minElements)
        if not tail:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next

        if node.next:
            heappush(minElements, node.next)
    return head

def main():
    # Merging m sorted lists
    arr = [[9, 8, 5, 2], [12, 11, 10, 9, 8], [1], [23, 21], [2, 1]]
    ll_head = merge_m_sorted_lists(arr)
    while ll_head:
        print (ll_head.data, end=' ')
        ll_head = ll_head.next
    print ()

    # Evaluating kth largest
    arr = [[9, 8, 5, 2], [12, 11, 10, 9, 8], [1], [23, 21], [2, 1]]
    print (k_largest_in_m_sortedlist(arr, 12))

main()
