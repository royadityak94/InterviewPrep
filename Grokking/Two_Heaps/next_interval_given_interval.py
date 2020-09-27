from heapq import heappush, heappop
# Brute Force Solution: O(N^2)

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def find_next_interval(intervals):
    # Time Complexity: O(NLogN), Space Complexity: O(N)
    N = len(intervals)
    result = [-1] * N
    maxStartHeap, maxEndHeap = [], []

    for idx in range(N):
        heappush (maxStartHeap, (-intervals[idx].start, idx))
        heappush (maxEndHeap, (-intervals[idx].end, idx))

    for _ in range(N):
        topEnd, endIndex = heappop(maxEndHeap)
        if maxStartHeap[0][0] <= topEnd:
            while maxStartHeap and maxStartHeap[0][0] <= topEnd:
                topStart, startIndex = heappop(maxStartHeap)
            result[endIndex] = startIndex
            heappush(maxStartHeap, (topStart, startIndex))

    return result

def main():
    result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
