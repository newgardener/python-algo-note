"""
Similar to meeting room ii problem
ㄴ with capacity constraint added
"""


def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
    starts = sorted([(trip[1], trip[0]) for trip in trips])
    ends = sorted([(trip[2], -trip[0]) for trip in trips])

    l, r = 0, 0
    total, cnt = 0, 0
    while l < len(trips):
        if starts[l][0] < ends[r][0]:
            cnt += starts[l][1]
            l += 1
        else:
            cnt += ends[r][1]
            r += 1
        total = max(total, cnt)
        if total > capacity:
            return False
    return True
