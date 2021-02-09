from heapq import heappush, heappop
# Brute Force Solution: O(N^2)

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def find_next_interval(intervals):
    n = len(intervals)
    maxStartHeap = []
    maxEndHeap = []
    resultant = [-1] * n

    for idx, interval in enumerate(intervals):
        heappush (maxStartHeap, (-interval.start, idx))
        heappush (maxEndHeap, (-interval.end, idx))

    for _ in range(n):
        end, endIdx = heappop(maxEndHeap)

        start, startIdx = None, None
        while maxStartHeap and -maxStartHeap[0][0] >= -end:
            start, startIdx = heappop(maxStartHeap)
        if startIdx is not None:
            resultant[endIdx] = startIdx
            heappush(maxStartHeap, (start, startIdx))
    return resultant





def main():
    result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
