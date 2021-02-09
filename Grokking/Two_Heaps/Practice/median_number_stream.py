# Design a class to calculate the median of a number stream. The class should have the following two methods:
# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
from heapq import heappush, heappop
import math
import bisect

# O(logN) time | O(N) space; Median = O(1)
class MedianOfAStream:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def insert_num(self, ele):
        if not self.maxHeap or ele <= -self.maxHeap[0]:
            heappush(self.maxHeap, -ele)
        else:
            heappush(self.minHeap, ele)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

        if ele == -2:
            print (self.maxHeap)
            print (self.minHeap)

    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2
        else:
            return -self.maxHeap[0]/1.0


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
    # Naive Case
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))

    # Time Complexity: Insertion: O(N), Fetch: O(1); Space: O(N)
    medianOfAStream = MedianOfAStream()

    arr = [4, 7, 1, -2, 20, 12, 13, 5, 3]
    for ele in arr[:4]:
        medianOfAStream.insert_num(ele)
        print("The median after inseting " + str(ele) + " is: " + str(medianOfAStream.find_median()))

    # Using 'bisort' algorithm
    medianOfAStream = MedianOfAStream2()
    for ele in arr:
        medianOfAStream.insert_num(ele)
        print("The median after inseting " + str(ele) + " is: " + str(medianOfAStream.find_median()))

main()
