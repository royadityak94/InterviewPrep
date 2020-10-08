# Design a class to efficiently find the Kth largest element in a stream of numbers
from heapq import heappush, heappop

class KthLargestNumberInStream:
    def __init__(self, nums, k):
        # TODO: Write your code here
        self.k_max_heap = []
        self.k = k

        for ele in nums:
            heappush(self.k_max_heap, ele)
            if len(self.k_max_heap) > k:
                heappop(self.k_max_heap)

    def add(self, num):
        # Time Complexity: O(LogK), Space Complexity: O(K)
        # TODO: Write your code here
        if num > self.k_max_heap[0]:
            heappop(self.k_max_heap)
            heappush(self.k_max_heap, num)
        return self.k_max_heap[0]

def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))
    print("4th largest number is: " + str(kthLargestNumber.add(2)))
    print("4th largest number is: " + str(kthLargestNumber.add(2)))


main()
