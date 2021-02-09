from heapq import _siftup, _siftdown, heappush, heappop

class SlidingWindowMedian:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def rebalance_heap(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def getMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap)/2
        else:
            return -self.maxHeap[0]/1.0

    def remove(self, heap, toRemove):
        index = heap.index(toRemove)
        heap[index] = heap[-1]
        del heap[-1]
        if index < len(heap):
            _siftup(heap, index)
            _siftdown(heap, 0, index)


    def find_sliding_window_median(self, arr, k):
        resultant = [None] * (len(arr)-k+1)
        for ele in arr:
            if not self.maxHeap or ele <= -self.maxHeap[0]:
                heappush(self.maxHeap, -ele)
            else:
                heappush(self.minHeap, ele)
            self.rebalance_heap()

            if i + 1 >= k:
                resultant[i-k+1] = self.getMedian()
                toRemove = arr[i-k+1]

                if self.maxHeap and toRemove <= -self.maxHeap:
                    self.remove(self.maxHeap, -toRemove)
                else:
                    self.remove(self.minHeap, toRemove)
            self.rebalance_heap()
        return resultant

def main():
    # Using 2 two heap pattern: Time: O(NK), Space: O(K)
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))

    print ('-----------------------------------------------------')


main()
