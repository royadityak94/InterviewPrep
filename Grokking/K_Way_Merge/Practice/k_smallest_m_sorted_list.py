from heapq import heappush, heappop

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __lt__(self, other):
        return self.data < other.data


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


def k_smallest_in_m_sortedlist(lists, k):
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

def main():
    arr = [[2, 6, 8], [3, 6, 7], [1, 3, 4]]
    print (k_smallest_in_m_sortedlist(arr, 5))

    arr = [[5, 8, 9], [1, 7]]
    print (k_smallest_in_m_sortedlist(arr, 3))

    arr = [[2, 6, 8], [3, 6, 7], [1, 3, 4]]
    print (k_smallest_in_m_sortedlist(arr, 5))

main()
