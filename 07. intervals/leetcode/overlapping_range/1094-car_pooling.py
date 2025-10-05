"""
Similar to meeting room ii problem
ㄴ with capacity constraint added

# Take-away: hard to set one standard either startTime, endTime
=> iterate through startTime, endTime sorted array each using two-pointer
"""


def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
    starts = sorted([(trip[1], trip[0]) for trip in trips])
    ends = sorted([(trip[2], -trip[0]) for trip in trips])

    l, r = 0, 0
    cnt = 0
    while l < len(trips):
        if starts[l][0] < ends[r][0]:
            cnt += starts[l][1]
            l += 1
        else:
            cnt += ends[r][1]
            r += 1
        if cnt > capacity:
            return False
    return True

# time stamping approach
def _carPooling(trips: list[list[int]], capacity: int) -> bool:
    timeline = []
    for trip in trips:
        timeline.append((trip[1], trip[0]))  # pick up
        timeline.append((trip[2], -trip[0]))  # drop off

    timeline.sort()

    cnt = 0
    for time, passenger in timeline:
        cnt += passenger
        if cnt > capacity:
            return False
    return True


