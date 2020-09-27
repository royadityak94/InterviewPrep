import bisect

def insert(intervals, new_interval):
    # Time Complexity: ~O(N), Space Complexity: O(N)
    if not len(intervals):
        return [new_interval],

    # Step - 1 : inserting at appropriate index in the input interval
    #start, end = intervals[0][0], intervals[0][1]
    idx = 0
    while new_interval[0] > intervals[idx][0]:
        idx += 1
    intervals.insert(idx, new_interval)
    #  bisect.insort(intervals, new_interval) <- Easy-peezee
    mergedIntervals = []
    start, end = intervals[0]
    for idx in range(1, len(intervals)):
        interval = intervals[idx]
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            mergedIntervals += [start, end],
            start, end = interval

    mergedIntervals += [start, end],
    return mergedIntervals


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))

main()
