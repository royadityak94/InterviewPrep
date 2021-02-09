from heapq import heappush, heappop
# Brute Force Solution: O(N^2)

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def find_next_interval(intervals):
    n = len(intervals)
    maxStartHeap, maxEndHeap = [], []

    for idx in range(n):
        heappush(maxStartHeap, (-intervals[idx].start, idx))
        heappush(maxEndHeap, (-intervals[idx].end, idx))

    resultant = [-1] * n
    for _ in range(n):
        end, endIdx = heappop(maxEndHeap)

        if -maxStartHeap[0][0] >= -end:
            start, startIdx = heappop(maxStartHeap)

            while -maxStartHeap[0][0] >= -end:
                start, startIdx = heappop(maxStartHeap)
            resultant[endIdx] = startIdx
    return resultant

def main():
    result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
