

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def search_overlapping_intervals(intervals):
    # Time Complexity: O(NLogN) + O(N) ~ O(NLogN), Space Complexity: O(N)
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x.start)
    overlapping_intervals = []

    start, end = intervals[0].start, intervals[0].end

    for idx in range(1, len(intervals)):
        interval = intervals[idx]
        if interval.start <= end:
            overlapping_intervals += Interval(start, end), Interval(interval.start, interval.end),
            end = max(end, interval.end)
        else:
            start, end = interval.start, interval.end

    return overlapping_intervals


def main():
    print("Overlapping intervals: ", end='')
    for i in search_overlapping_intervals([Interval(1, 4), Interval(2, 5), Interval(6, 7), Interval(8, 12), Interval(11, 16)]):
        i.print_interval()
    print()

main()
