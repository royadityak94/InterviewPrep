from heapq import heappush, heappop

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end

def min_meeting_rooms(meetings):
    # Time Complexity: O(NLogN), Space Complexity: O(1)
    meetings.sort(key=lambda meeting: meeting.start)
    min_rooms = float('-inf')
    rooms = []

    for idx in range(len(meetings)):
        meeting = meetings[idx]
        while (rooms and rooms[0] <= meeting.start):
            heappop(rooms)
        heappush(rooms, meeting.end)
        min_rooms = max(min_rooms, len(rooms))

    return min_rooms


def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(1, 4), Meeting(1, 3), Meeting(1, 2), Meeting(3, 5), Meeting(4, 5), Meeting(2, 5)])))

main()
