from heapq import heappush, heappop

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __lt__(self, other):
        return self.data < other.data

def return_ll_head_ptrs(lists):
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

def k_smallest_sorted(arr, k):
    # Time Complexity: O(min(K, N) * KlogN), Space Complexity: O(N)
    ll_head_ptrs = return_ll_head_ptrs(arr)
    minElements = []

    for head in ll_head_ptrs:
        heappush(minElements, head)

    count = 0
    tail = None
    while minElements:
        node = heappop(minElements)
        count += 1
        if count == k:
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
    input_mat = [[2, 6, 8], [3, 7, 10], [5, 8, 11]]

    for i in range(9):
        print (i+1, k_smallest_sorted(input_mat, i+1))

main()
