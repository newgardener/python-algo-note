"""
Find the maximum number of meetings going on "simultaneously"
"""

# %%
"""
Two-pointer approach for both starts and ends array
Time Complexity: O(NlogN)
Space Complexity: O(N)
"""


def minMeetingRooms(self, intervals: list[list[int]]) -> int:
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])
    # l for starts, r for ends
    l, r = 0, 0
    # rooms: max(# of ongoing meetings)
    rooms, meetings = 0, 0
    while l < len(intervals):
        # case: need a meeting room
        if starts[l] < ends[r]:
            meetings += 1
            l += 1
        # case: meeting ends
        else:
            meetings -= 1
            r += 1
        # update max(# of ongoing meetings)
        rooms = max(rooms, meetings)
    return rooms


# %%
import heapq


"""
Min-heap approach
ㄴ sorting using min-heap O(NlogN)
Time Complexity: O(NlogN)
Space Complexity: O(N)
"""


def minMeetingRooms(self, intervals: list[list[int]]) -> int:
    minHeap = []
    for interval in intervals:
        heapq.heappush(minHeap, (interval[0], 1))  # meeting starts
        heapq.heappush(minHeap, (interval[1], -1))  # meeting ends

    # rooms: max(# of ongoing meetings)
    rooms, meetings = 0, 0
    while minHeap:
        meetings += heapq.heappop(minHeap)[1]
        rooms = max(rooms, meetings)
    return rooms


