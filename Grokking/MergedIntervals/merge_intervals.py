
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge(intervals):
    # Time Complexity: O(NLogN) + O(N) ~ O(NLogN), Space Complexity: O(N)
    if len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda x: x.start)
    mergedIntervals = []
    start, end = intervals[0].start, intervals[0].end

    for idx in range(1, len(intervals)):
        interval = intervals[idx]
        if interval.start <= end: # Overlapping intervals
            end = max(end, interval.end)
        else: # Non-overlapping intervals
            mergedIntervals += Interval(start, end),
            start, end = interval.start, interval.end

    mergedIntervals += Interval(start, end),
    return mergedIntervals

def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4)]):
        i.print_interval()
    print()

main()
