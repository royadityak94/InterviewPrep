from heapq import _siftup, _siftdown, heappush, heappop

class SlidingWindowMedian2:
    # Time Complexity: O(NK), Space : O(K)
    def __init__(self):
        pass
    def find_sliding_window_median(self, arr, k):
        median = []
        for i in range(len(arr)-k+1):
            window = arr[i:i+k]
            list.sort(window)

            if k % 2 == 0:
                median += float((window[k//2] + window[k//2 - 1])/2),
            else:
                median += float(window[k//2]),
        return median

class SlidingWindowMedian:
    # Time Complexity: O(NKlogK), Space : O(K)
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    def find_sliding_window_median(self, arr, k):
        medians = []

        for i in range(len(arr)):
            if (not self.maxHeap) or (arr[i] <= -self.maxHeap[0]):
                heappush(self.maxHeap, -arr[i])
            else:
                heappush(self.minHeap, arr[i])

            self.rebalance()

            if len(self.maxHeap) + len(self.minHeap) == k:
                if k % 2 != 0:
                    medians += float(-self.maxHeap[0]),
                else:
                    medians += float((-self.maxHeap[0] + self.minHeap[0])/2),

                # Delete the outgoing element
                to_remove = arr[i-k+1]
                if to_remove <= -self.maxHeap[0]:
                    self.delete(self.maxHeap, -to_remove)
                else:
                    self.delete(self.minHeap, to_remove)

                self.rebalance()
        return medians

    def rebalance(self):
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def delete(self, heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        del heap[-1]

        if index < len(heap):
            _siftup(heap, index)
            _siftdown(heap, 0, index)



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

    slidingWindowMedian = SlidingWindowMedian2()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian2()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
