"""
Find the maximum number of meetings going on "simultaneously"
"""

# %%
"""
Two-pointer approach for both starts and ends array
"""


def minMeetingRooms(self, intervals: list[list[int]]) -> int:
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])
    # l for starts, r for ends
    l, r = 0, 0
    # res: max(# of ongoing meetings)
    res, cnt = 0, 0
    while l < len(intervals):
        # case: need a meeting room
        if starts[l] < ends[r]:
            cnt += 1
            l += 1
        # case: meeting ends
        else:
            cnt -= 1
            r += 1
        # update max(# of ongoing meetings)
        res = max(res, cnt)
    return res
