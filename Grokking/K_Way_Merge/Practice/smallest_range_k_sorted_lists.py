# Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.
from heapq import heappush, heappop

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __lt__(self, other):
        return self.data < other.data

def return_head_ptrs(lists):
    ll_head_ptrs = []

    for list in lists:
        head = tail = None
        for ele in list:
            if not head:
                head = tail = ListNode(ele)
            else:
                tail.next = ListNode(ele)
                tail = tail.next
        ll_head_ptrs += head,

    return ll_head_ptrs

def smallest_range_k_sortedlists(lists):
    ll_head_ptrs = return_head_ptrs(lists)
    minElements = []
    observedMaximum = float('-inf')

    for head in ll_head_ptrs:
        heappush(minElements, head)
        observedMaximum = max(observedMaximum, head.data)

    range_start, range_end = 0, observedMaximum
    flag = True
    while minElements and flag:
        node = heappop(minElements)
        if  (range_end - range_start) > (observedMaximum - node.data):
            range_start, range_end = node.data, observedMaximum

        if node.next:
            heappush(minElements, node.next)
            observedMaximum = max(observedMaximum, node.next.data)
        else:
            flag = False

    return [range_start, range_end]

def main():
    print (smallest_range_k_sortedlists([[1, 5, 8], [4, 12], [7, 8, 10]]))
    print (smallest_range_k_sortedlists([[1, 9], [4, 12], [7, 10, 16]]))

main()
