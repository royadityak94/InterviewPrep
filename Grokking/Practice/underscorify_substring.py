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

def get_bounds(string, substring):
    intervals = []
    idx = 0
    while idx < len(string):
    	if string[idx: idx+len(substring)] == substring:
    		intervals += (idx, idx+len(substring)),
    		idx += max(1, len(substring)-1)
    	else:
    		idx += 1

    print ("Returned: ", intervals)
    return intervals

def underscorifySubstring(string, substring):
    # Write your code here.
    collapsed_bounds = merge_intervals(get_bounds(string, substring))
    string = list(string)
    to_add = 0

    print (collapsed_bounds)

    for idx_start, idx_end in collapsed_bounds:
    	string.insert(idx_start+to_add, '_')
    	to_add += 1
    	string.insert(idx_end+to_add, '_')
    	to_add += 1

    return ''.join(string)

def main():
    s1 = 'ttttttttttttttbtttttctatawtatttttastvb'
    s2 = 'ttt'
    print (underscorifySubstring(s1, s2))


main()
