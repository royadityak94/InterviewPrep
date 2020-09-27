

# def custom_range(*interval):
#     return range(interval[0], interval[1]+1)
#
custom_range = lambda *interval: range(interval[0], interval[1]+1)

def merge(intervals_a, intervals_b):
    interval_intersection = []
    i = j = 0
    while (i < len(intervals_a) and (j < len(intervals_b))):
        a_overlaps_b = intervals_a[i][0] in custom_range(*intervals_b[j])
        b_overlaps_a = intervals_b[j][0] in custom_range(*intervals_a[i])

        if (a_overlaps_b or b_overlaps_a):
            interval_intersection += [max(intervals_a[i][0], intervals_b[j][0]), \
                min(intervals_a[i][1], intervals_b[j][1])],

        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1
    return interval_intersection


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))

main()
