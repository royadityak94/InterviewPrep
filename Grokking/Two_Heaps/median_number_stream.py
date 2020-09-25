# Design a class to calculate the median of a number stream. The class should have the following two methods:
# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
from heapq import heappush, heappop
import math
import bisect

class MedianOfAStream:
    # Time Complexity: Maintenance: O(logN), Fetch:O(1); Space Complexity: O(N)
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.total = 0

    def insert_num(self, num):
        # TODO: Write your code here
        if (not self.maxHeap) or (-self.maxHeap[0] >= num):
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        # Balancing the min and max Heap
        if len(self.maxHeap) - len(self.minHeap) > 1:
            popped = -heappop(self.maxHeap)
            heappush(self.minHeap, popped)

        elif len(self.minHeap) > len(self.maxHeap):
            popped = heappop(self.minHeap)
            heappush(self.maxHeap, -popped)

        self.total += 1
        print (">> ", self.maxHeap, self.minHeap)

    def find_median(self):
        # TODO: Write your code here
        median = None
        if self.total % 2 != 0:
            median = -self.maxHeap[0]
        else:
            median = (-self.maxHeap[0] + self.minHeap[0])/2
        return median

class MedianOfAStream2:
    def __init__(self):
        self.arr = []

    def insert_num(self, num):
        bisect.insort(self.arr, num)
        print ("After: ", self.arr)

    def find_median(self):
        N = len(self.arr)
        median = None
        if N % 2 != 0:
            median = self.arr[N//2]
        else:
            median = (self.arr[N//2] + self.arr[(N//2) - 1])/2
        return median


def main():
    # Time Complexity: Insertion: O(N), Fetch: O(1); Space: O(N)
    medianOfAStream = MedianOfAStream()

    arr = [4, 7, 1, -2, 20, 12, 13, 5, 3]
    for ele in arr:
        medianOfAStream.insert_num(ele)
        print("The median after inseting " + str(ele) + " is: " + str(medianOfAStream.find_median()))

    # Using 'bisort' algorithm
    medianOfAStream = MedianOfAStream2()
    arr = [4, 7, 1, -2, 20, 12, 13, 5, 3]
    for ele in arr:
        medianOfAStream.insert_num(ele)
        print("The median after inseting " + str(ele) + " is: " + str(medianOfAStream.find_median()))

main()
