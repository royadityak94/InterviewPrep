from heapq import _siftup, _siftdown, heappush, heappop

# O(NK) time | O(K) time; insert: O(log K), remove: O(K)
class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def rebalance_heap(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def remove(self, heap, toRemove):
        index = heap.index(toRemove)
        heap[index] = heap[-1]
        del heap[-1]

        if index < len(heap):
            _siftup(heap, index)
            _siftdown(heap, 0, index)

    def find_sliding_window_median(self, arr, k):
        resultant = [None] * (len(arr)-k+1)
        for i in range(len(arr)):
            if not self.maxHeap or arr[i] > -self.maxHeap[0]:
                heappush(self.minHeap, arr[i])
            else:
                heappush(self.maxHeap, -arr[i])

            self.rebalance_heap()

            if i + 1 >= k:
                if len(self.maxHeap) == len(self.minHeap):
                    resultant[i-k+1] = (-self.maxHeap[0] + self.minHeap[0])/2
                else:
                    resultant[i-k+1] = -self.maxHeap[0]/1.0

                toRemove = arr[i-k+1]
                if toRemove <= -self.maxHeap[0]:
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
