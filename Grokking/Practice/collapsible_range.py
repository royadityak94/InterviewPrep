class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print ("[", self.start, ",", self.end, "]", end='')

def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda x: x.start)
    start, end = intervals[0].start, intervals[0].end
    mergedIntervals = []
    for interval in intervals[1:]:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            mergedIntervals += Interval(start, end),
            start, end = interval.start, interval.end
    mergedIntervals += Interval(start, end),
    return mergedIntervals

def main():
    intervals = [Interval(0, 3), Interval(1, 4), Interval(6, 15), Interval(5, 7), Interval(6, 8)]
    for i in merge_intervals(intervals):
        i.print_interval()
    print()

    intervals = [Interval(6, 7), Interval(2, 4), Interval(5, 9), Interval(1, 3)]
    for i in merge_intervals(intervals):
        i.print_interval()
    print()

main()
