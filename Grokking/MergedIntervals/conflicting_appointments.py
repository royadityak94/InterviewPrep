
def can_attend_all_appointments(intervals):
    # Time Complexity: O(NLogN) + O(N) ~ O(NlogN), Space Complexity: O(1)
    intervals.sort(key=lambda x: x[0])
    start, end = intervals[0]

    for idx in range(1, len(intervals)):
        interval = intervals[idx]
        if interval[0] <= end:
            return False
        start, end = interval
    return True

def enlist_all_conflicting_appointments(intervals):
    # Time Complexity: O(NLogN), Space Complexity: O(1)
    intervals.sort(key=lambda x: x[0])
    all_conflicting_appointments = []

    start, end = intervals[0]
    for idx in range(1, len(intervals)):
        interval = intervals[idx]
        if interval[0] <= end:
            if [start, end] in intervals and [start, end] not in all_conflicting_appointments:
                all_conflicting_appointments += [start, end],
            all_conflicting_appointments += interval,
            end = max(end, interval[1])
        else:
            start, end = interval

    return all_conflicting_appointments


def main():
    # Check if the appointments are clear
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))

    # Enlist all conflicting appointments
    print("Conflicting appointments: " + str(enlist_all_conflicting_appointments([[1, 5], [2, 3], [4, 6], [7, 7],  [8, 9], [8, 10], [12, 15]])))
    print("Can attend all appointments: " + str(enlist_all_conflicting_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Conflicting appointments: " + str(enlist_all_conflicting_appointments([[4,5], [1,2], [3,6], [5,6], [7,8]])))

main()
