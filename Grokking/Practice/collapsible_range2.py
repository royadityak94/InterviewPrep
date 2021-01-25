
def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda x: x[0])
    start, end = intervals[0]
    mergedIntervals = []
    for curr_s, curr_e in intervals[1:]:
        if curr_s <= end:
            end = max(end, curr_e)
        else:
            mergedIntervals += (start, end),
            start, end = curr_s, curr_e
    mergedIntervals += (start, end),
    return mergedIntervals

def main():
    intervals = [(0, 3), (1, 4), (6, 15), (5, 7), (6, 8)]
    intervals2 = [(6, 7), (2, 4), (5, 9), (1, 3)]
    print (merge_intervals(intervals))
    print (merge_intervals(intervals2))

main()
